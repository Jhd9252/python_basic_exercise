#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic requests and BS4 via DataquestIO
Download info from National Weather Forecast for New York City
Created on Sat Jun 13 18:39:47 2020
"""

#imports
import requests
from bs4 import BeautifulSoup

#download the html page
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994')

#create a BeautifulSoup Object to parse
soup = BeautifulSoup(page.content, 'html.parser')


#find the element that contains the extended 7 day forecast and assign to variable. Inspect
seven_day = soup.find(id = 'seven-day-forecast')
forecast_items = seven_day.find_all(class_= 'tombstone-container') #make sure it is class_ to not cause conflict

#print the first item in pretty
tonight = forecast_items[0]
print(tonight.prettify())

#want to extract critical information, such as name of the item, description, short descript, and temp
period = tonight.find(class_='period-name').get_text() #pulling text from this area
short_desc = tonight.find(class_ = 'short-desc').get_text()
temp = tonight.find(class_ = 'temp').get_text()
print(period)
print(short_desc)
print(temp)

img = tonight.find('img')
desc = img['title']
print(desc)

#now we want to iterate through and pull this info for the rest of the tombstone containers
#select all items with the class 'period-name' inside the class 'tombstone-container' in seven_day
#use list comprehension to call get_text() on the BeautifulSoup object 

period_tags = seven_day.select('.tombstone-container .period-name')
periods = [pt.get_text() for pt in period_tags]

#use the same techniques to grab the other 3 fields (short_desc, temp, desc)
short_descs = [sd.get_text() for sd in seven_day.select('.tombstone-container .short-desc')]
temps = [t.get_text() for t in seven_day.select('.tombstone-container .temp')]
descs = [d['title'] for d in seven_day.select('.tombstone-container img')]


#combine the data into a Pandas DataFrame to analyze it. 
#DF is a object from pandas that stores tabular data
#pass in the info we have into the DF object as part of a dictionary. 
#each dicionary key will be a column in the DF and each list will be the values in the column. 

import pandas as pd
weather = pd.DataFrame({'periods': periods, 'short_desc':short_descs, 'temp': temps, 'desc': descs})
print(weather)

#optional analysis on data. 
#regular expression and the Series.str.extract method to pull the numeric temp values
temp_nums = weather['temp'].str.extract("(?P<temp_num>\d+)", expand = False)
weather['temp_num'] = temp_nums.astype('int')
print(temp_nums)

#find the means of the high and low temps
print(weather['temp_num'].mean())








