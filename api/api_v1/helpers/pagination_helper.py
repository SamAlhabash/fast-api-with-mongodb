from math import floor


def get_total_pages(total_count: int, page_size: int) -> int:
    return total_count / page_size if \
        floor(total_count / page_size) == (total_count / page_size) \
        else floor(total_count / page_size) + 1
