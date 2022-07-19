import streamlit
import pandas
import requests


streamlit.title('wszystko gra')
streamlit.header('nagłówek')
streamlit.text('zwykly tekst')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
