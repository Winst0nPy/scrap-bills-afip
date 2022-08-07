import glob
import fitz
import fitz_handler as fh
from pandas_handler import *
from ScrapFacturaA import ScrapFacturaA
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)
    array = []
    for file in source_files:
        with fitz.open(file) as doc:
            page = doc[0]

            blocks = fh.get_page_blocks(page)
            blocks = fh.round_all_coordinates_in_blocks(blocks)
            fh.sort_blocks_by_y0(blocks)

            scrap = ScrapFacturaA(blocks)
            scrap.scrap()
            scrap.print_scrap()
            # array.append(scrap.obj)

    # array_to_excel(array, 'test.xlsx')


if __name__ == '__main__':
    main()
