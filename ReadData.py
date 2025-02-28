import sqlite3
import pandas as pd


conn = sqlite3.connect("inventory.db")  


df = pd.read_sql_query("SELECT * FROM inventory", conn)  


conn.close()

print(df)
