#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data from the indexed dataset with hypermedi
        metadata.

        Args:
            index (int): The start index for the page (0-indexed).
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing index, next_index, page_size,
            and data.
        """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        max_index = len(indexed_data) - 1

        if index is None:
            index = 0
        else:
            assert index <= max_index, "Index out of range"

        next_index = min(index + page_size, max_index + 1)
        page_data = [indexed_data[i] for i in range(index, next_index)]

        hypermedia_data = {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data
        }

        return hypermedia_data
