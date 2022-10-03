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
        fh.sort_blocks_by('y0', blocks)
        words = fh.get_page_words(page)
        words = fh.round_all_coordinates_in_words(words)
        fh.sort_words_by('y0', words)
        for k, v in fh.group_words_by_y0_and_x0(words).items():
            print(k, v)


if __name__ == '__main__':
    main()
