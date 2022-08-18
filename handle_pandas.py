import pandas as pd


def array_to_excel(array: list[dict], filename, path='.\\', sheet_name=None):
    df = pd.DataFrame(data=array)
    if sheet_name:
        df.to_excel(path + filename, index=False, sheet_name=sheet_name)
    else:
        df.to_excel(path + filename, index=False)
