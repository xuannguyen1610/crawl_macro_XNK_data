import pandas as pd
from ValueConverter import convert_country_value, convert_category_value


def convert_excel_content():
	file_data_raw = r"C:\Users\Admin\Downloads\Macro_data\T3_2023\ket_qua_xkt3.xlsx"
	df1 = pd.read_excel(file_data_raw,na_values=['NULL', 'None', 'N/A', '#N/A'])
	df1['value'] = df1['value'].fillna(0)
	df_country = pd.read_excel(r"C:\Users\Admin\Downloads\Macro_data\_country__varchar_99.xlsx")
	df_category = pd.read_excel(r"C:\Users\Admin\Downloads\Macro_data\macro_type_group.xlsx")



	df1_new = convert_country_value(df1,df_country,"country_old","country_new")
	data_XNK = convert_category_value(df1_new,df_category,"category_old","category_new")

	return data_XNK

