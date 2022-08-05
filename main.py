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
            blocks = fh.get_page_blocks(page)
            blocks = fh.round_all_coordinates_in_blocks(blocks)
            fh.sort_page_block_by_y0(blocks)
            anchor = fh.get_coordinate_by_anchors(['Código', 'Producto / Servicio'], blocks)
            # print(anchor)
            # fh.print_page_blocks(blocks)
            scrap = ScrapFacturaA(blocks)
            scrap.scrap()
            # scrap.print_scrap()


if __name__ == '__main__':
    main()
