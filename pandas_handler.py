import pandas as pd


def array_to_excel(array: dict[list[any]], filename, path='.\\'):
    df = pd.DataFrame(data=array)
    df.to_excel(path + filename, index=False)
