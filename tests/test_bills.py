import glob
import fitz
import pandas as pd
from Handlers import handle_fitz as fh
from ScrapBill import ScrapBill
from config import *


def main():
    source_files = glob.glob(SOURCE_PATH)
    bills = []
    for file in source_files:
        print(file)
        with fitz.open(file) as doc:
            page = doc[0]
            blocks = fh.get_blocks_and_round_sorted(page, 'y0')
            words = fh.get_words_and_round_sorted(page, 'y0')
            sb = ScrapBill(words, blocks)
            bill = sb.scrap()
            print(bill, '\n')
            bills.append(bill.to_dict())

    bills_df = pd.DataFrame(bills)
    writer = pd.ExcelWriter('comprobantes_afip.xlsx', engine='xlsxwriter')
    bills_df.to_excel(writer, sheet_name='comprobantes', index=False)
    writer.save()


if __name__ == '__main__':
    main()
