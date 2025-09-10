#!/usr/bin/python3
"""
Lazy pagination generator for user_data table
"""

import seed


def paginate_users(page_size, offset):
    """Fetch a single page of users with LIMIT + OFFSET."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that lazily fetches pages of users from user_data.
    Uses only one loop.
    """
    offset = 0
    while True:  # only one loop allowed
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
