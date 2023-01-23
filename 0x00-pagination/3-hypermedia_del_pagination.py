#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self):
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10):
        """
        Deletion-resilient hypermedia pagination
        """
        value = 0
        assert value <= index < len(self.dataset())
        indexedDataset = self.indexed_dataset()
        indexedPage = {}
        token = index
        while len(indexedPage) < page_size and token < len(self.dataset()):
            if token in indexedDataset:
                indexedPage[token] = indexedDataset[token]
            token += 1
        page = list(indexedPage.values())
        dictionary = {
            "index": index,
            "data": page,
            "page_size": len(page),
            "next_index": max(indexedPage) + 1,
        }
        return dictionary
