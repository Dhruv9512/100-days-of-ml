import cx_Oracle
import pandas as pd
conn = conn = cx_Oracle.connect("HR/Mrdhruv123@//localhost:1521/orclpdb")


df=pd.read_sql_query('select * from employees',conn)

print(df.head())