import pandas as pd

def get_df(fn):
    # print("Hellow World!")
    df = pd.read_excel(fn)
    return df

if __name__ == "__main__":
    # execute only if run as a script
    filename = 'TestBook.xlsx'
    df = get_df(filename)
    print(df.head())
