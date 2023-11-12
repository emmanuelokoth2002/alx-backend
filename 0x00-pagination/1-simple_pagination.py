#!/usr/bin/env python3
'''
Simple helper function and Server class for paginating a database of popular
baby names.
'''
from typing import Tuple, List
import csv


def calculate_pagination_indexes(page: int, page_size: int) -> Tuple[int, int]:
    '''Calculate and return the start and end indexes for pagination.'''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class BabyNameServer:
    """Server class for paginating a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def load_dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_paginated_data(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Retrieve a paginated subset of the dataset.'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = calculate_pagination_indexes(page, page_size)
        dataset = self.load_dataset()

        try:
            paginated_data = [dataset[i] for i in range(start_index, end_index)]
        except IndexError:
            paginated_data = []

        return paginated_data
