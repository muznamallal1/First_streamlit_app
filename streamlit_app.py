
import streamlit

streamlit.title('My Moms new Healthy diner')


streamlit.header('Breakfast Favorites')

streamlit.text('  🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('  🥗 Kale, Spinach and Rocket SMoothie')

streamlit.text('  🐔Hard boiled Free Range eggs')
streamlit.text(' 🥑🍞 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#lets pick a list here so they can picka fruit
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


streamlit.dataframe(my_fruit_list)





