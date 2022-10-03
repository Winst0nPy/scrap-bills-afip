import glob
import fitz
from Handlers import handle_fitz as fh
from Handlers.HandleBill import HandleBill
from Handlers.HandleItems import HandleItems
from ScrapBill import ScrapBill
from ScrapItems import ScrapItems
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)
    bills = []
    items = []

    for index, file in enumerate(source_files):
        print(index, file, '\n')

        with fitz.open(file) as doc:
            page = doc[0]
            blocks = fh.get_page_blocks(page)
            blocks = fh.round_all_coordinates_in_blocks(blocks)
            fh.sort_blocks_by('block_no', blocks)

            sb, si = ScrapBill(blocks), ScrapItems(blocks)
            bill, bill_items = sb.scrap(), si.scrap()
            bills.append(bill.to_dict())
            try:
                item_id = bill.cuit_emisor + bill.nro_comprobante
            except TypeError:
                item_id = ""

            for item in bill_items:
                items.append({**{'id': item_id}, **item.to_dict()})

    hb = HandleBill(bills)
    hi = HandleItems(items)


if __name__ == '__main__':
    main()
