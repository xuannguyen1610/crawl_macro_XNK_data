import mysql.connector

'''mydb = mysql.connector.connect(
    host="139.59.101.51",
    user="xuanprovjp",
    password="AWX03kgd1QjMTSgZsUBAxxz1QDw",
    database="stock"
)
'''

mydb = mysql.connector.connect(
    host="157.230.244.233",
    user="stock_admin",
    password="aVBrVDczZzJ5OUVma3JR",
    database="stock"
)

def insert_data_to_database(data_list):
    cursor = mydb.cursor()
    add_data_query = "INSERT INTO macro_type_data (type_group, year, month, value, code, continent, country) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE value = VALUES(value)"

    for data in data_list:
        params = (data.type_group, data.year, data.month, data.value, data.code, data.continent, data.country)
        cursor.execute(add_data_query, params)

    mydb.commit()
    cursor.close()
