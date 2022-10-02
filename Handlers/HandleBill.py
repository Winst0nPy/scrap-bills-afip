import pandas as pd
from Entity.Bill import Bill
from IPython.display import display, HTML


class HandleBill:
    def __init__(self, bill: Bill):
        self.bill = bill
        self.df = pd.DataFrame.from_dict(bill.to_dict())

    def print_dataframe(self):
        display(HTML(self.df.to_html()))


