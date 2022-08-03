import glob
import fitz
from ScrapBillAFIP import ScrapBillAFIP
import fitz_handler
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)
    scraper = ScrapBillAFIP()
    for file in source_files:
        with fitz.open(file) as doc:
            fitz_handler.print_page_blocks(doc[0])

    # scraper.print_scrap()

if __name__ == '__main__':
    main()
