import pandas as pd
from IPython.display import display, HTML


class HandleBillData:
    def __init__(self, data: dict[any]):
        self.data = data
        self.df = pd.DataFrame.from_dict(data)

    def print_dataframe(self):
        display(HTML(self.df.to_html()))


