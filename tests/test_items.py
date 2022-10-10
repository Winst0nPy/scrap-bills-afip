import glob
import fitz
from Handlers import handle_fitz as fh
from ScrapItems import ScrapItems
from config import *


def main():
    source_files = glob.glob(SAMPLE_PATH)
    file = source_files[0]
    with fitz.open(file) as doc:
        page = doc[0]
        blocks = fh.get_blocks_and_round_sorted(page, 'y0')
        words = fh.get_words_and_round_sorted(page, 'y0')
        for key, item in fh.group_words_by_y0_and_sort_x0(words).items():
            print(key, item)



if __name__ == '__main__':
    main()
