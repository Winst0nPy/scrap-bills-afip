# (x0, y0, x1, y1, "lines in the block", block_no, block_type)
import math
from operator import itemgetter

block_values = {
        "x0": 0,
        "y0": 1,
        "x1": 2,
        "y1": 3,
        "word": 4,
        "block_no": 5
    }


def print_page_blocks_by_keyword(keyword_to_search: str, blocks) -> None:
    for x in blocks:
        x0, y0, x1, y1, word, block_no, block_type = x
        if keyword_to_search in word:
            text_to_show = f'y0:{math.floor(y0)} y1:{math.floor(y1)} x0:{math.floor(x0)} x1:{math.floor(x1)}, word: {repr(word)} '
            print(text_to_show)


def print_page_blocks(blocks):
    for block in blocks:
        x0, y0, x1, y1, word, block_no, block_type = block
        text_to_show = f'y0:{y0} y1:{y1} x0:{x0} x1:{x1}, block_no: {block_no} word: {word} '
        print(text_to_show)
    print('\n')


def round_all_coordinates_in_blocks(blocks):
    return [(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1), [w for w in word.split('\n') if w], block_no, block_type)
            for x0, y0, x1, y1, word, block_no, block_type in blocks]


def get_page_blocks(page):
    return page.get_textpage().extractBLOCKS()


def get_page_words(page):
    return page.get_textpage().extractWORDS()


def sort_blocks_by(option: str, blocks: tuple[any]):
    blocks.sort(key=itemgetter(block_values[option]))


def get_text_in_coordinate(x0, x1, y0, y1, blocks) -> list[str]:
    aux_lst = []

    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if are_between([b_x0, b_x1], x0, x1) and are_between([b_y0, b_y1], y0, y1):
            aux_lst += text

    return aux_lst if len(aux_lst) >= 1 else None


def get_blocks_in_coordinate(x0, x1, y0, y1, blocks) -> list[str]:
    aux_lst = []
    
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if are_between([b_x0, b_x1], x0, x1) and are_between([b_y0, b_y1], y0, y1):
            aux_lst.append(block)

    return aux_lst

            
def is_between(n: int, start: int, end: int) -> bool:
    return start <= n <= end


def are_between(array: list[int], start: int, end: int) -> bool:
    return all([is_between(n, start, end) for n in array])


def get_coordinate_by_list_anchors(anchors: list[str], blocks: list[tuple]) -> tuple[any]:
    for block in blocks:
        word = block[4]
        if all([anchor in word for anchor in anchors]):
            return block


def get_text_from_blocks(blocks):
    return [block[4] for block in blocks]


def is_keyword_in_blocks(keyword, blocks):
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if keyword in text:
            return True
    return False


def find_block_by_keyword(keyword, blocks):
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if any([keyword in w for w in text]):
            return block


def find_words_to_the_right_of_block(block, blocks, correction_factor):
    b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
    return get_text_in_coordinate(b_x1, find_max_x1_in_blocks(blocks), b_y0 - correction_factor, b_y1 + correction_factor, blocks)


def find_max_x1_in_blocks(blocks):
    return max([block[3] for block in blocks])


def find_block_by_keywords(keywords, blocks) -> tuple[any]:
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if all([keyword in text for keyword in keywords]):
            return block


def find_blocks_by_pattern(pattern, blocks):
    anchors = []
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if pattern(block):
            anchors.append(block)
    return anchors if len(anchors) >= 1 else None


def get_all_blocks_by_block_value(attribute: str, value: int, blocks: tuple[any]):
    return [block for block in blocks if block[block_values[attribute]] == value]

