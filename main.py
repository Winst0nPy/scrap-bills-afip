import glob
import fitz
import pandas as pd
from Handlers import handle_fitz as fh
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
            item_id = bill.cuit_emisor + bill.nro_comprobante

            for item in bill_items:
                items.append({**{'id': item_id}, **item.to_dict()})

    bills_df = pd.DataFrame(bills)
    items_df = pd.DataFrame(items)

    writer = pd.ExcelWriter('comprobantes_afip.xlsx', engine='xlsxwriter')
    bills_df.to_excel(writer, sheet_name='comprobantes', index=False)
    items_df.to_excel(writer, sheet_name='items', index=False)
    writer.save()


if __name__ == '__main__':
    main()
