#!/usr/bin/env python3
"""Return a tuple of start and end indexes for pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes for the given page
        and page_size.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
