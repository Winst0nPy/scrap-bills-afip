import glob
import fitz
from ScrapBillAFIP import ScrapBillAFIP
import fitz_handler
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)

    for file in source_files:
        with fitz.open(file) as doc:
            page = doc[0]
            scraper = ScrapBillAFIP(fitz_handler.get_page_block(page))
            fitz_handler.print_page_blocks_by_keyword(page, 'COD.')
            scraper.print_page_block()


if __name__ == '__main__':
    main()
