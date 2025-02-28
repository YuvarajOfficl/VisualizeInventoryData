import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect("inventory.db")

df = pd.read_sql_query("SELECT * FROM inventory", conn)

conn.close()

print(df)

plt.figure(figsize=(10, 5))
sns.barplot(x="month", y="quantity", hue="vendor", data=df)
plt.title("Inventory Levels Over Time")
plt.xlabel("Month")
plt.ylabel("Quantity")
plt.legend(title="Vendor")
plt.show()
