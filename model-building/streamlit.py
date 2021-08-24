from altair.vegalite.v4.schema.channels import Y
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import altair as alt
# reading the csv file

merged = pd.read_csv('merged_df.csv')


# Developing an app (streamlit)

st.title('DISTRIBUTION OF PERSONS WITH ALBINISM IN 2018/2019 ')
st.subheader('The merged dataframe')
merged

st.sidebar.header('INPUT PARAMETER')
counties = merged.County
selected_counties = st.sidebar.multiselect('Counties', counties)

# heatmap
st.markdown('The visualization on distribution of PWA are as shown bellow. click on the  the heatmap to vie the visualizations')
if st.button('Bar graph'):
    st.header('A bar graph showing the increase in number of persons with albinisn in the 2018/2019')
    chart = alt.Chart(merged).mark_line().encode(
    x = alt.X('County'),
    y = alt.Y('Total_No_Products')
    ).properties(title='The Total Products Distributed VS the Estimated Number of Prodycts to be Distributed')
    st.altair_chart(chart, use_container_width = True)



