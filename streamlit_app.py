
import streamlit

import snowflake.connector
from urllib.error import URLError
import pandas



streamlit.title('My Moms new Healthy diner')


streamlit.header('Breakfast Favorites')

streamlit.text('  🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('  🥗 Kale, Spinach and Rocket SMoothie')

streamlit.text('  🐔Hard boiled Free Range eggs')
streamlit.text(' 🥑🍞 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list= my_fruit_list.set_index('Fruit')

#lets pick a list here so they can picka fruit
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create code function
def get_fruityvice_date(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return streamlit.dataframe(fruityvice_normalized) 

#new section
streamlit.header("Fruityvice Fruit Advice!")
try:  
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit for info")

  else:
    back_from_function=get_fruityvice_date(fruit_choice)
    streamlit.dataframe(back_from_function)

#streamlit.text(fruityvice_response.json())

except URLError as e:
  streamlit.error()


#snowflake functions:
def get_fruit_load_list():
    my_cur.execute("SELECT * from fruit_load_list")
    return  my_cur.fetchall()



#Allow end user
def insert_row_snowflake(new_fruit):
    with  my_cnx.cursor() as my_cur:
          my_cur.execute("Insert into fruit values:('from streamlit')")
          return "thanks for adding" + new_fruit




#streamlit.stop()

#add button
if streamlit.button('Get fruit Load List'):
    my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

    

add_my_fruit=streamlit.text_input('What fruit do you want to add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)

streamlit.header("The fruit list contains:")






