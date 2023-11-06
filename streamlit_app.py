#python code here

import streamlit
import pandas as pd

  
streamlit.title('My Parents new healthy Diner')
streamlit.header('Breakfast')
streamlit.text('🥣 Blueberry Oats')
streamlit.text('🐔 Hard Boiled Eggs')
streamlit.text('🥗 Kale Smoothie')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
