# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SalesSuccess Dashboard", layout="wide")

# Load data
df = pd.read_csv('data/sales_data_sample.csv')

st.title("📊 SalesSuccess: Sales Performance Dashboard")

st.sidebar.header("Filters")
region = st.sidebar.multiselect("Select Region", options=df["REGION"].unique(), default=df["REGION"].unique())
df_filtered = df[df["REGION"].isin(region)]

# Metrics
st.metric("Total Revenue", f"${df_filtered['SALES'].sum():,.2f}")
st.metric("Avg Order Value", f"${df_filtered['SALES'].mean():,.2f}")
st.metric("Total Orders", f"{df_filtered.shape[0]}")

# Charts
st.subheader("Revenue by Product Line")
fig1, ax1 = plt.subplots()
df_filtered.groupby("PRODUCTLINE")["SALES"].sum().sort_values().plot(kind='barh', ax=ax1)
st.pyplot(fig1)

st.subheader("Monthly Sales Trend")
df_filtered['MONTH'] = pd.to_datetime(df_filtered['ORDERDATE']).dt.to_period('M')
monthly_sales = df_filtered.groupby('MONTH')['SALES'].sum()
fig2, ax2 = plt.subplots()
monthly_sales.plot(ax=ax2)
st.pyplot(fig2)
