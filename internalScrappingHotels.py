# Import the libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Extract the HTML and create a BeautifulSoup object
url = ('https://www.tripadvisor.in/Hotels-g294201-Cairo_Cairo_Governorate-Hotels.html')

user_agent = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
               'Accept-Language': 'en-US, en;q=0.5'})

page = requests.get(url, headers=user_agent)
soup = BeautifulSoup(page.text, 'html.parser')


for name in soup.findAll('div', {'class': 'listing_title'}):
    print(name.a.get("href"))

