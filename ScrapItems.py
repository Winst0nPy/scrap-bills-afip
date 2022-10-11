import Handlers.handle_fitz as fh
from config import *
from ScrapItem import ScrapItem
from Entity.Item import Item


class ScrapItems:

    def __init__(self, blocks, words):
        self.blocks = blocks
        self.words = words
        self.sorted_words_by_y0_and_x0 = fh.group_words_by_y0_and_sort_x0(words)
        self.default_result = [Item()]

    def scrap(self) -> list[Item]:
        pass

    def find_position_of_all_rows_in_words(self):
        pass

    def find_row(self):
        pass

    