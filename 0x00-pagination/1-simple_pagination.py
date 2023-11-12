#!/usr/bin/env python3
'''
function
'''
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    return a tuple
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


class Server:
    """
    Server class.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cache dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' page the dataset '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        page_range = index_range(page, page_size)
        start = page_range[0]
        end = page_range[1]
        data = self.dataset()
        try:
            data = [data[i] for i in range(start, end)]
        except IndexError:
            data = []
        return data
