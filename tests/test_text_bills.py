import glob
import fitz
from Handlers import handle_fitz as fh
from ScrapBill import ScrapBill
from ScrapItems import ScrapItems
from config import *


def main():
    source_files = glob.glob(SAMPLE_PATH)
    file = source_files[0]

    with fitz.open(file) as doc:
        page = doc[0]
        blocks = fh.get_page_blocks(page)
        blocks = fh.round_all_coordinates_in_blocks(blocks)
        fh.sort_blocks_by('block_no', blocks)

        filtered_blocks = fh.find_block_by_keywords(['CUIT'], blocks)
        print(filtered_blocks)


if __name__ == '__main__':
    main()
