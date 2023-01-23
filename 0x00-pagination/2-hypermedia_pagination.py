#!/usr/bin/env python3
"""
Simple helper function
Classes:
    Server
Functions:
    dataset(object) -> list(list)
    get_page(object, integer, integer) -> list(list)
    index_range(integer, integer) -> tuple(integer, integer)
"""
import csv
import math
from typing import List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return page of dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        all_data = self.dataset()
        try:
            page, page_size = index_range(page, page_size)
            filter_data = all_data[page:page_size]
            return filter_data
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        method that takes the same arguments (and defaults) as get
        _page and returns a dictionary containing the following key-value
        pairs
        """
        listpage_filtered = self.get_page(page, page_size)
        total_page = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_page else None
        prev_page = page - 1 if page != 1 else None
        hypermedia = {
            "page_size": len(listpage_filtered),
            "page": page,
            "data": listpage_filtered,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_page,
        }
        return hypermedia
