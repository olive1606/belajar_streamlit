import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Superstore Dashboard")

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQMqC_6fkaH6oZweJDIIYFDdE9o3P3G1hB0OKLzkGGf0pB-FjWJoAMoYca2iXV2ID5dE7hoklCSx6hE/pub?gid=0&single=true&output=csv")

df

df['order_year'] = df['order_date'].dt.year
CURR_YEAR = df['order_year'].max()
PREV_YEAR = CURR_YEAR - 1

mx_data = pd.pivot_table(data=df,index='order_year',aggfunc={'sales':np.sum,'profit':np.sum,'order_id':pd.Series.nunique,'customer_id':pd.Series.nunique}).reset_index()



