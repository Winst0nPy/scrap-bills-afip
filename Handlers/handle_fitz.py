# (x0, y0, x1, y1, "lines in the block", block_no, block_type)
import math
import regex as re
from operator import itemgetter

block_values = {
        "x0": 0,
        "y0": 1,
        "x1": 2,
        "y1": 3,
        "word": 4,
        "block_no": 5
    }

words_values = {
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
    return [(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1), ' '.join([w for w in word.split('\n') if w]), block_no, block_type)
            for x0, y0, x1, y1, word, block_no, block_type in blocks]


def round_all_coordinates_in_words(words):
    # (x0, y0, x1, y1, "word", block_no, line_no, word_no)
    return [(math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1), ' '.join([w for w in word.split('\n') if w]), block_no, line_no, word_no)
            for x0, y0, x1, y1, word, block_no, line_no, word_no in words]


def get_page_blocks(page):
    return page.get_textpage().extractBLOCKS()


def get_page_words(page):
    return page.get_textpage().extractWORDS()


def get_page_in_json(page):
    return page.get_textpage().extractJSON()


def get_page_in_dict(page):
    return page.get_textpage().extractDICT()


def sort_blocks_by(option: str, blocks: list[tuple]):
    blocks.sort(key=itemgetter(block_values[option]))


def sort_words_by(option: str, words: list[tuple]):
    words.sort(key=itemgetter(block_values[option]))


def get_text_in_coordinate(x0, x1, y0, y1, blocks) -> str:
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if are_between([b_x0, b_x1], x0, x1) and are_between([b_y0, b_y1], y0, y1):
            return text
    return ""


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
        if keyword in text:
            return block


def find_words_to_the_right_of_block(block, blocks, correction_factor):
    b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
    return get_text_in_coordinate(b_x1, find_max_x1_in_blocks(blocks), b_y0 - correction_factor, b_y1 + correction_factor, blocks)


def find_max_x1_in_blocks(blocks):
    return max([block[3] for block in blocks])


def find_block_by_keywords(keywords, blocks) -> tuple[any]:
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if all([bool(re.search(keyword, ' '.join(text))) for keyword in keywords]):
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


def find_text_by_pattern_first_appear(pattern, blocks):
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if pattern(text):
            return text[0]


def get_text_by_block_no(n, blocks):
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        if block_no == n:
            return text


def group_blocks_by_y0(blocks) -> dict:
    group = {}
    for block in blocks:
        b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
        line = group.get(b_y0, [])
        line.append(text)
        group[b_y0] = line
    return group

def group_words_by_y0_and_x0(words) -> dict:
    group = {}
    for word in words:
        x0, y0, x1, y1, text, block_no, line_no, word_no = word
        line = group.get(y0, [])
        line.append((x0, text))
        group[y0] = line

    for key, value in group.items():
        value.sort(key=itemgetter(0))
        group[key] = [word[1] for word in value]

    return group


def group_words_by_y0_and_x0_with_error_margin(words, margin: int) -> dict:
    group = {}
    for word in words:
        x0, y0, x1, y1, text, block_no, line_no, word_no = word
        line = group.get(y0, [])
        line.append((x0, text))
        group[y0] = line

    for key, value in group.items():
        value.sort(key=itemgetter(0))
        group[key] = [word[1] for word in value]

    keys_to_delete = []
    for key, value in group.items():
        if key + margin in group:
            group[key] = group[key + margin] + value
            keys_to_delete.append(key + margin)

    for keys in keys_to_delete:
        del group[keys]

    return group


def get_blocks_and_round_sorted(page, sort) -> list[tuple]:
    blocks = round_all_coordinates_in_blocks(get_page_blocks(page))
    sort_blocks_by(sort, blocks)
    return blocks


def get_words_and_round_sorted(page, sort) -> list[tuple]:
    words = round_all_coordinates_in_words(get_page_words(page))
    sort_words_by(sort, words)
    return words


def group_words_by_y0_and_sort_x0(words):
    group = {}
    for word in words:
        x0, y0, x1, y1, text, block_no, line_no, word_no = word
        line = group.get(y0, [])
        line.append((x0, text))
        group[y0] = line

    for key, value in group.items():
        value.sort(key=itemgetter(0))

    return group

