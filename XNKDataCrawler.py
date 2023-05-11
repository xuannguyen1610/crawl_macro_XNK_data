from XNKDataService import convert_excel_to_datalist
from XNKDataRepository import insert_data_to_database
from ExcelUtil import convert_excel_content


year = '2023'
month = '4'
code = 'NHAP_KHAU'
continent = ''

isDebug = False
if isDebug:
	data_XNK = convert_excel_content()
	data_XNK.to_excel("check_data_XNK.xlsx", index=False)
else:
	data_list = convert_excel_to_datalist(year,month,code,continent)
	insert_data_to_database(data_list)