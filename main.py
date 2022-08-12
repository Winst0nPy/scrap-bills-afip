import glob
import fitz
import fitz_handler as fh
from pandas_handler import *
from ScrapFacturaA import ScrapFacturaA
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)
    array = []
    for index, file in enumerate(source_files):
        print(index, file, '\n')
        with fitz.open(file) as doc:
            page = doc[0]
            blocks = fh.get_page_blocks(page)
            blocks = fh.round_all_coordinates_in_blocks(blocks)
            fh.sort_blocks_by('block_no', blocks)
            # fh.print_page_blocks(blocks)
            scrap = ScrapFacturaA(blocks)
            scrap.scrap()
            scrap.print_scrap()
            # array.append(scrap.obj)

    # array_to_excel(array, 'test.xlsx')


if __name__ == '__main__':
    main()
