#python code here

import streamlit
import pandas as pd
import requests
  
streamlit.title('My Parents new healthy Diner')
streamlit.header('Breakfast')
streamlit.text('🥣 Blueberry Oats')
streamlit.text('🐔 Hard Boiled Eggs')
streamlit.text('🥗 Kale Smoothie')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit',inplace=True)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# pandas deals with json
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# and we output it
streamlit.dataframe(fruityvice_normalized)
