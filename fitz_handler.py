# (x0, y0, x1, y1, "lines in the block", block_no, block_type)
import math


def print_page_blocks_by_keyword(blocks, keyword_to_search: str) -> None:
    for x in blocks:
        x0, y0, x1, y1, word, block_no, block_type = x
        if keyword_to_search in word:
            text_to_show = f'y0:{math.floor(y0)} y1:{math.floor(y1)} x0:{math.floor(x0)} x1:{math.floor(x1)}, word: {repr(word)} '
            print(text_to_show)


def print_page_blocks(blocks):
    for x in blocks:
        x0, y0, x1, y1, word, block_no, block_type = x
        text_to_show = f'y0:{math.floor(y0)} y1:{math.floor(y1)} x0:{math.floor(x0)} x1:{math.floor(x1)}, word: {repr(word)} '
        print(text_to_show)


def round_all_coordinates_in_blocks(blocks):
    return [(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1), word, block_no, block_type)
            for x0, y0, x1, y1, word, block_no, block_type in blocks]


def get_page_block(page):
    return page.get_textpage().extractBLOCKS()


def sort_page_block(blocks):
    blocks.sort(key=lambda x: x[3])


def join_block_by_coordinate(coordinate, blocks):
    dictionary = {}
    pass
