import streamlit as st
from annotated_text import annotated_text
from api import fetch_weather ,fetch_news

def format_date(date_string):
    year = date_string[:4]
    month = date_string[4:6]
    day = date_string[6:8]
    return f"{year}-{month}-{day}"

def main():
    st.title("Jabar Information App 🌡️📰")
    annotated_text(
    "Made by: ",
    ("Dhewa Radya", "1202213086"),
    " & ",
    ("Andhika Idham", "1202213203"),
    ".")
    st.caption("@JabarDigitalService pls recruit kami")
    st.divider()
    
    if 'last_city' not in st.session_state:
        st.session_state.last_city = ""

    city = st.text_input("Enter city name (West Java only):")
    if city and st.session_state.last_city != city:
      st.session_state.last_city = city
      weather_data = fetch_weather(city)
      news_data = fetch_news(city)

      if 'error' in weather_data:
          st.error(weather_data['error'])
      else:
          weather_info = weather_data.get('data', {})
        
          st.write(f"City: {weather_info.get('description', '')}, {weather_info.get('domain', '')}")
          st.divider()

          st.subheader("Weather Information in {}".format(city))
          daily_data = weather_info.get('params', [])
          max_temperatures = {}
          min_temperatures = {}
          for data in daily_data:
              if data.get('id') == 'tmax':
                  for time_data in data.get('times', []):
                      max_temperatures[time_data.get('datetime', '')] = time_data.get('celcius', '')
              elif data.get('id') == 'tmin':
                  for time_data in data.get('times', []):
                      min_temperatures[time_data.get('datetime', '')] = time_data.get('celcius', '')

          for date in max_temperatures.keys():
              max_temp = max_temperatures.get(date)
              min_temp = min_temperatures.get(date)
              formatted_date = format_date(date)
              st.write(f"Date: {formatted_date}, Max Temperature: {max_temp}, Min Temperature: {min_temp}")
              
      st.divider()

      st.subheader("Latest News in {}".format(city))
      if 'error' in news_data:
          st.error(news_data['error'])
      else:
          articles = news_data.get('xml', {}).get('pencarian', {}).get('item', [])
          if not articles:
              st.write("No news available in {}.".format(city))
          else:
              for article in articles:
                  st.write(f"**{article['title']}**")
                  st.write(article['link'])

if __name__ == "__main__":
    main()
