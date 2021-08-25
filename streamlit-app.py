
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import graph_objects as go
import seaborn as sns 
import altair as alt
from streamlit.proto.Markdown_pb2 import Markdown


merged = pd.read_csv('merged_df.csv')


rad = st.sidebar.radio('Navigation', ['HOME', 'Visualization1', 'Visualization2', 'Visualization3', 'Visualization4'])

if rad == 'HOME':
    st.title('DISTRIBUTION OF PERSONS WITH ALBINISM IN 2018/2019')
    st.subheader('The merged dataframe')
    merged

if rad == 'Visualization1':
    selected_cols = st.sidebar.multiselect('Select Column', merged.columns)

    st.subheader('The visualization on distribution of Total Support products distibuted vs the Estmated Number of Support Products to be distributed')
    st.markdown('Select Total products and Estimated total product on the side bar to display the visualization')

    fig = px.line(merged, x = 'County', y = selected_cols)
    st.plotly_chart(fig)

if rad == 'Visualization2':
    st.header("INCREASE IN NUMBER OF PWA 2018/2019")
    st.markdown('Click the button bellow to view the graph')
    if st.button('Graph'):
        pop_chart = go.Figure(data=[go.Bar(name = 'No_PWA_2018', x = merged['County'], y = merged['No_(PWA)_2018']),
        go.Bar(name = 'No_PWA_2019', x = merged['County'], y = merged['No_PWA()_2019'])
        ])
        st.plotly_chart(pop_chart)

if rad == 'Visualization3':
    st.header('PWA by Gender')
    st.markdown('Click the button bellow to view the pie chart')
    if st.button('Pie Chart'):
        df = merged[['Total_Male_PWA', 'Total_Female_PWA']].sum().to_frame().reset_index()
        df.columns = ['Gender', 'Total Number']
        gender_pie =  px.pie(df, values = 'Total Number', names = 'Gender')
        st.plotly_chart(gender_pie)


if rad == 'Visualization4':
    st.header('Distribution of products per type')
    st.markdown('Click the button bellow to view the bar chart')
    if st.button('Barh Chart'):
        df1 = merged[['Sunsreen_Lotions', 'Lip_Care', 'AfterSun_Lotions', 'Caps', 'Long_Sleeved_Tshirts']].sum().to_frame().reset_index()
        df1.columns = ['Product', 'Number']
        product_bar = px.bar(df1, x='Number', y= 'Product', orientation='h', color='Product')
        st.plotly_chart(product_bar)
