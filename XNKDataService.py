from XNKDataModel import XNK_Data
from ExcelUtil import convert_excel_content

data_list = []

def convert_excel_to_datalist(year,month,code,continent):
    df = convert_excel_content()
    for index, row in df.iterrows():
        data = XNK_Data(int(row['category_old']), year, month, row['value']/1000000, code, continent, row['country_old'])
        data_list.append(data)

    return data_list
