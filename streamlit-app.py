
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import graph_objects as go
import seaborn as sns 
import altair as alt


merged = pd.read_csv('merged_df.csv')


rad = st.sidebar.radio('Navigation', ['HOME', 'Visualization1', 'Visualization2', 'Visualization3'])

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
    cols= merged[['Sunsreen_Lotions', 'Lip_Care', 'AfterSun_Lotions', 'Caps', 'Long_Sleeved_Tshirts']].sum()
    st.subheader('fgh')
    st.markdown('sjnkbj')
    df = merged[['Total_Male_PWA', 'Female_Pop']].sum()
    gender = st.sidebar.multiselect('Select Column', df.columns)
    st.title('Average prices of various commodities')
    st.subheader('Products grouped into various categories')
    st.bar_chart(df)