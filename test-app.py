import json
import streamlit as st
import requests
import xml.etree.ElementTree as ET

def fetch_news(city):
    url = "https://indonesia-news.p.rapidapi.com/search/kompas"
    querystring = {"command": city, "page": "1", "limit": "10"}
    headers = {
        "X-RapidAPI-Key": "de85987dc7msha94ae4463722f1ep1b6118jsn8fa2737f13af",
        "X-RapidAPI-Host": "indonesia-news.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    
    print("Response Status Code:", response.status_code)  # Print status code for troubleshooting
    print("Response Content:", response.text)  # Print response content for troubleshooting
    
    if response.status_code == 200:
        response_news = response.json()
        return response_news
      
    else:
        return {"error": f"Failed to fetch news. Status code: {response.status_code}"}

def main():
    st.title("City News App")

    city = st.text_input("Enter city name:", "bandung")
    news_data = fetch_news(city)

    st.subheader("Latest News")
    if 'error' in news_data:
        st.error(news_data['error'])
    else:
        articles = news_data.get('xml', {}).get('pencarian', {}).get('item', [])
        if not articles:
            st.write("No news available for the specified city.")
        else:
            for article in articles:
                st.write(f"**{article['title']}**")
                st.write(article['link'])

if __name__ == "__main__":
    main()