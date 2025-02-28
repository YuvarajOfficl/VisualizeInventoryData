import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect("inventory.db")


df = pd.read_sql_query("SELECT * FROM inventory", conn)


st.title("📊 Inventory Monitoring Dashboard")


vendor_filter = st.selectbox("Select Vendor:", ["All"] + list(df["vendor"].unique()))
item_filter = st.selectbox("Select Item:", ["All"] + list(df["item"].unique()))
location_filter = st.selectbox("Select Location:", ["All"] + list(df["location"].unique()))


filtered_df = df.copy()
if vendor_filter != "All":
    filtered_df = filtered_df[filtered_df["vendor"] == vendor_filter]
if item_filter != "All":
    filtered_df = filtered_df[filtered_df["item"] == item_filter]
if location_filter != "All":
    filtered_df = filtered_df[filtered_df["location"] == location_filter]


st.subheader("📈 Inventory Trend Over Time")
plt.figure(figsize=(8, 4))
sns.lineplot(data=filtered_df, x="month", y="quantity", hue="item", marker="o")
plt.xlabel("Month")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
st.pyplot(plt)


st.subheader("📋 Filtered Inventory Data")
st.dataframe(filtered_df)
