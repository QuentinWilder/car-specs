import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Car Specs around the World")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)
df_cars['continent'] = df_cars['continent'].apply(lambda x: x.strip(' .'))

# sidebar selectbox
continent_options = ["All"]
for cont in df_cars['continent'].unique():
    continent_options.append(cont)

selected_continent = st.sidebar.selectbox(
    label="Select a Region", options=continent_options
    )

if selected_continent != "All":
    df_cars = df_cars[df_cars['continent'] == selected_continent]

# figure 1
st.header("Correlation Heatmap")

fig1, ax1 = plt.subplots(figsize=(10,6))
ax1 = sns.heatmap(df_cars.corr(), annot=True, vmin=-1, vmax=1, cmap=sns.color_palette('Spectral', 8))
st.pyplot(fig=fig1)

# figure 2
st.header("Horsepower Distribution")

ax2 = sns.displot(df_cars, x=df_cars['hp'], hue=df_cars['continent'])
st.pyplot(fig=ax2)

