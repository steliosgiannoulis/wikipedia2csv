# This is a piece of code that I found online for webscrapping using Beautiful soup

# This is a quick way to convert an online table to a dataframe and consequerntly to csv

# Stelios Giannoulis - November 2022


# Let's import all the libaries we need.
# for performing your HTTP requests
import requests  

# for xml & html scrapping 
from bs4 import BeautifulSoup 

# for table analysis
import pandas as pd

# write to csv
import csv

# Time
import time


wikipedia_url= "https://en.wikipedia.org/wiki/Prefectures_of_Greece"
print(wikipedia_url)

# Session helps to object allows you to persist certain parameters across requests
# By default, Request will keep waiting for a response indefinitely. Therefore, it is advised to set the timeout parameter.
# If the request was successful, you should see the reponse output as '200'.
s = requests.Session()
response = s.get(wikipedia_url, timeout=10)
#response2 = s.get(url2, timeout=5)
response

# parse response content to html
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

# to view the content in html format
pretty_soup = soup.prettify()
#print(pretty_soup)

# title of Wikipedia page
soup.title.string

# find all the tables in the html
all_tables=soup.find_all('table')
#print(all_tables)

right_table=soup.find('table',{"class": 'wikitable sortable'})
#print(right_table)

# Number of columns in the table
for row in right_table.findAll("tr"):
    cells = row.findAll('td')

len(cells)

# number of rows in the table including header
rows = right_table.findAll("tr")
len(rows)

# header attributes of the table
header = [th.text.rstrip() for th in rows[0].find_all('th')][0:]
print(header)
print('------------')
print(len(header))

lst_data = []
for row in rows[2:]:
            data = [d.text.rstrip() for d in row.find_all('td')]
            lst_data.append(data)

# select also works as find_all
lst_data1 = []
for row in rows[2:]:
            data = [d.text.rstrip() for d in row.select('td')]
            lst_data1.append(data)


# length of each record
len(lst_data1[0])

lst_data1 = pd.DataFrame(lst_data1, columns=header)
df = lst_data1.copy()
df