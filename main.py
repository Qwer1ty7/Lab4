import pandas as pd
import mysql.connector
#xlsx

query = "SELECT * FROM test"

conn = mysql.connector.connect(user='sql11479622', password='tUR6XY1ZJF',
                              host='sql11.freemysqlhosting.net',
                              database='sql11479622')
print('connected')
data = pd.read_sql(query, conn)
print('queried')
#data.to_csv('exported_data.csv', index = False)
data.to_excel('exported_data.xlsx')
conn.close()