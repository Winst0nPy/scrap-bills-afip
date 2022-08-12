import pandas as pd


def array_to_excel(array: list[dict], filename, path='.\\'):
    df = pd.DataFrame(data=array)
    df.to_excel(path + filename, index=False)
