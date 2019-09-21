import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://weather.com/zh-CN/weather/5day/l/5a59130c02eacb2a84e8edc0e8869ccb7c07b4b720e26568c354d113608dc6a4')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(class_="twc-table")
items = week.find_all(class_="clickable closed")

day = [item.find(class_="date-time").get_text() for item in items]
day_detail = [item.find(class_="day-detail clearfix").get_text() for item in items]
description = [item.find(headers="description").get_text() for item in items]
hilo = [item.find(headers="hi-lo").get_text() for item in items]
precip = [item.find(headers="precip").get_text() for item in items]
wind = [item.find(headers="wind").get_text() for item in items]
humidity = [item.find(headers="humidity").get_text() for item in items]

weather_stuff = pd.DataFrame (
    {
        '白天':day,
        '日期':day_detail,
        '说明':description,
        '高／低':hilo,
        '降雨概率':precip,
        '风力':wind,
        '湿度':humidity,
    })
print(weather_stuff)
weather_stuff.to_csv('weather.csv')
