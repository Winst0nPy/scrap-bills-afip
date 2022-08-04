import glob
import fitz
from ScrapFacturaA import ScrapFacturaA
import fitz_handler as fh
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)

    for file in source_files:
        with fitz.open(file) as doc:
            page = doc[0]
            block = fh.get_page_block(page)
            block = fh.round_all_coordinates_in_blocks(block)
            fh.sort_page_block(block)
            fh.print_page_blocks(block)
            fh.print_page_blocks_by_keyword(block, 'COD.')


if __name__ == '__main__':
    main()
