# (x0, y0, x1, y1, "lines in the block", block_no, block_type)
import math


def print_page_blocks_by_keyword(page, keyword_to_search: str) -> None:
    page_text = page.get_textpage()
    text = page_text.extractBLOCKS()
    for x in text:
        x0, y0, x1, y1, word, block_no, block_type = x
        if keyword_to_search in word:
            text_to_show = f'y0:{math.floor(y0)} y1:{math.floor(y1)} x0:{math.floor(x0)} x1:{math.floor(x1)}, word: {repr(word)} '
            print(text_to_show)


def get_page_block(page):
    return page.get_textpage().extractBLOCKS()

