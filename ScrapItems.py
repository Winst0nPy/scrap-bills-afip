import Handlers.handle_fitz as fh
import patterns as pa
from config import *
from ScrapItem import ScrapItem
from Entity.Item import Item


class ScrapItems:

    def __init__(self, page_blocks):
        self.page_blocks = page_blocks
        self.default_result = [Item()]

    def scrap(self) -> str | list[Item]:
        coor = COOR_FACTURAS_A['articulos']

        try:
            items_y0 = fh.get_coordinate_by_list_anchors(ARTICULOS_ANCHOR_Y0, self.page_blocks)[3]
        except IndexError:
            return self.default_result

        block_of_items = fh.get_blocks_in_coordinate(coor['x0'], coor['x1'], items_y0, coor['y1'], self.page_blocks)
        rows = fh.find_blocks_by_pattern(pa.is_item_row, block_of_items)

        if len(rows) == 1:
            item = fh.get_text_from_blocks(block_of_items)
            if len(item) == 1:
                item = item[0]
            else:
                item = [' '.join([x for sublist in item[:-1] for x in sublist])] + item[-1]

            return [ScrapItem(item).scrap()]

        elif len(rows) > 1:
            items = []
            for block in block_of_items:
                b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
                item = fh.get_text_in_coordinate(coor['x0'], coor['x1'], b_y0, b_y1, block_of_items)
                if item:
                    item = [' '.join(item[:-7])] + item[len(item)-7:]
                    items.append(item)

            return [ScrapItem(item).scrap() for item in items]

