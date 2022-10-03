from Entity.Item import Item
import pandas as pd
from IPython.display import display, HTML


class HandleItems:
    def __init__(self, items: list[dict]):
        self.items = items
        self.df = pd.DataFrame(items)

    def print_dataframe(self):
        display(HTML(self.df.to_html()))
