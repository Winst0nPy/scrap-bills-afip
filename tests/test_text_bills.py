import glob
import fitz
from Handlers import handle_fitz as fh
from ScrapBill import ScrapBill
from ScrapItems import ScrapItems
from config import *


def main():
    source_files = glob.glob(SAMPLE_PATH)

    for file in source_files:
        with fitz.open(file) as doc:
            page = doc[0]
            blocks = fh.get_blocks_and_round_sorted(page, 'y0')
            words = fh.get_words_and_round_sorted(page, 'y0')
            for k, v in fh.group_words_by_y0_and_x0(words).items():
                print(k, v)


if __name__ == '__main__':
    main()
