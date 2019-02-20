import pandas as pd

def get_df(fn:str):
    # print("Hellow World!")
    df = pd.read_excel(fn)
    return df

def make_xlsx(fn:str, df:pd.DataFrame):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(fn, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Testing', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

if __name__ == "__main__":
    # execute only if run as a script
    filename = 'TestBook.xlsx'
    df = get_df(filename)
    print(df.head())
    make_xlsx('NewBook.xlsx', df)
