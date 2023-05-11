def convert_country_value(df1,df2,column_old,column_new):
	df1 = df1.merge(df2[[column_old, column_new]], on=column_old, how='left')
	df1[column_new] = df1[column_new].fillna('Others')
	df1[column_old] = df1[column_new]
	df1 = df1.drop(column_new, axis=1)

	return df1


def convert_category_value(df1,df2,column_old,column_new):
	df1 = df1.merge(df2[[column_old, column_new]], on=column_old, how='left')
	df1[column_old] = df1[column_new]
	df1 = df1.drop(column_new, axis=1)

	return df1
