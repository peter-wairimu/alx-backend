

import { createClient, print } from 'redis';
import { promisify } from 'util';
import express from 'express';


const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4,
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10,
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2,
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5,
    },
];

function getItemById(id) {
    const result = listProducts.filter((item) => item.itemId === id)[0];
    console.log(result)
    return result
}


const app = express();
const port = 1245;

const notFound = { status: 'Product not found' };

app.listen(port, () => {
    console.log(`listen`);
});

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function reserveStockById(id, stock) {
    client.set(`item.${id}`, stock);
}

async function getCurrentReservedStockById(id) {
    const stock = await getAsync(id);
    return stock;
}



app.get('/list_products/:id', async (req, res) => {
    const id = Number(req.params.id);
    const item = getItemById(id);

    if (!item) {
        res.json(notFound);
        return;
    }

    const currentStock = await getCurrentReservedStockById(id);
    if (!currentStock) {
        await reserveStockById(id, item.stock);
        item.currentQuantity = item.stock;
    } else item.currentQuantity = currentStock;
    res.json(item);
});


app.get('/reserve_product/:id', async (req, res) => {
    const id = Number(req.params.id);
    const item = getItemById(id);
    const noStock = { status: 'Not enough stock available', id };
    const reservationConfirmed = { status: 'Reservation confirmed', id };

    if (!item) {
        res.json(notFound);
        return;
    }

    let currentStock = await getCurrentReservedStockById(id);
    if (currentStock === null) currentStock = item.stock;

    if (currentStock <= 0) {
        res.json(noStock);
        return;
    }

    reserveStockById(id, Number(currentStock) - 1);

    res.json(reservationConfirmed);
});
