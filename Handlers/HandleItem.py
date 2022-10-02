from Entity.Item import Item
import pandas as pd
from IPython.display import display, HTML


class HandleItem:
    def __init__(self, item: Item):
        self.item = item
        self.df = pd.DataFrame.from_dict(item.to_dict())

    def print_dataframe(self):
        display(HTML(self.df.to_html()))

