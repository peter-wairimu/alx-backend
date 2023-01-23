#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function named index_range that takes two integer arguments page
    and page_size
    Parameters:
        page (int): index start number
        page_size (int): index end number
    Returns:
        return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes
    """
    start_index = page
    end_index = page_size
    result = ((end_index * (start_index - 1)), end_index * page)
    return result
