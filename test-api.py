import streamlit as st
import requests
import xml.etree.ElementTree as ET


url = "https://indonesia-news.p.rapidapi.com/search/kompas"
querystring = {"command": 'bandung', "page": "1", "limit": "10"}
headers = {
		"X-RapidAPI-Key": "de85987dc7msha94ae4463722f1ep1b6118jsn8fa2737f13af",
		"X-RapidAPI-Host": "indonesia-news.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)

print("XML Response:", response.text)