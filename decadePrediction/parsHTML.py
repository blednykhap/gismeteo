
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

url = 'https://www.gismeteo.ru/weather-moscow-4368/10-days/'
response = requests.get(url=url, headers=headers)
soupParser = BeautifulSoup(response.text, 'html.parser')
widgetItems = soupParser.find('div', class_='widget-items')

today = date.today()
arrayDays = ["day"]
for dayData in widgetItems.contents[0].find_all('a', class_='row-item'):
    #attribute = dayData.find('div', class_='date').text
    #position = attribute.find(' ')
    #if position != -1: day = attribute[0:position]
    #else: day = attribute
    #print(today)
    arrayDays.append(today.strftime("%Y-%m-%d"))
    today = today + timedelta(days=1)
print(arrayDays)

arrayCloudiness = ["cloudiness"]
for dayData in widgetItems.contents[1].find_all('div', class_='row-item'):
    attribute = dayData.find('div', class_='weather-icon tooltip').attrs['data-text']
    arrayCloudiness.append(attribute)
print(arrayCloudiness)

arrayMaxTemperature = ["maxTemp"]
arrayMinTemperature = ["minTemp"]
for dayData in widgetItems.contents[2].find_all('div', class_='value style_size_m'):
    maxTemp = dayData \
        .find('div', class_='maxt') \
        .find('span', class_='unit unit_temperature_c') \
        .text
    minTemp = dayData \
        .find('div', class_='mint') \
        .find('span', class_='unit unit_temperature_c') \
        .text
    arrayMaxTemperature.append(maxTemp.replace(',','.'))
    arrayMinTemperature.append(minTemp.replace(',','.'))
print(arrayMaxTemperature)
print(arrayMinTemperature)

arrayMsWind = ["msWind"]
arrayKmhWind = ["kmhWind"]
for dayData in widgetItems.contents[3].find_all('div', class_='row-item'):
    msWind = dayData.find('span', class_="wind-unit unit unit_wind_m_s")
    kmhWind = dayData.find('span', class_="wind-unit unit unit_wind_km_h")
    if msWind != None: msWindVal = msWind.text
    else: msWindVal = ''
    if kmhWind != None: kmhWindVal = kmhWind.text
    else: kmhWindVal = ''
    arrayMsWind.append(msWindVal.replace(',','.'))
    arrayKmhWind.append(kmhWindVal.replace(',','.'))
print(arrayMsWind)
print(arrayKmhWind)

arrayRain = ["rain"]
for dayData in widgetItems.contents[4].find_all('div', class_='row-item'):
    rain = dayData.find('div', class_="item-unit")
    arrayRain.append(rain.text.replace(',','.'))
print(arrayRain)

file = csv.writer(open('d:\\temp\\htmldata.csv', 'w', newline='', encoding='utf-8'))

for i in range(0, 10):
    file.writerow([arrayDays[i], arrayCloudiness[i], arrayMaxTemperature[i], arrayMinTemperature[i],
                  arrayMsWind[i], arrayKmhWind[i], arrayRain[i]])
