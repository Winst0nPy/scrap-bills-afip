import pandas as pd
from Entity.Bill import Bill
from IPython.display import display, HTML


class HandleBill:
    def __init__(self, bill: list[dict]):
        self.bill = bill
        self.df = pd.DataFrame(bill)

    def print_dataframe(self):
        display(HTML(self.df.to_html()))


