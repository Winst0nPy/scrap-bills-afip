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
        text_to_show = f'y0:{y0} y1:{y1} x0:{x0} x1:{x1}, word: {word} '
        print(text_to_show)


def round_all_coordinates_in_blocks(blocks):
    return [(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1), [w for w in word.split('\n') if w], block_no, block_type)
            for x0, y0, x1, y1, word, block_no, block_type in blocks]


def get_page_blocks(page):
    return page.get_textpage().extractBLOCKS()


def sort_page_block(blocks):
    blocks.sort(key=lambda x: x[3])


def get_text_in_coordinates(x0, x1, y0, y1, blocks) -> list[str]:
    aux_lst = []

    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if are_between([b_x0, b_x1], x0, x1) and are_between([b_y0, b_y1], y0, y1):
            aux_lst += text

    return aux_lst if len(aux_lst) > 1 else None


def is_between(n, start, end) -> bool:
    return start <= n <= end


def are_between(array, start, end) -> bool:
    return all([is_between(n, start, end) for n in array])
