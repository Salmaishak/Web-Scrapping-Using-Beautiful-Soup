# Import the libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Extract the HTML and create a BeautifulSoup object.
url = ('https://www.tripadvisor.in/Attractions-g294201-Activities-oa0-Cairo_Cairo_Governorate.html')

user_agent = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
			'Accept-Language': 'en-US, en;q=0.5'})

def get_page_contents(url):
    page = requests.get(url, headers = user_agent)
    return BeautifulSoup(page.text, 'html.parser')

soup = get_page_contents(url)

# Find and extract the data elements.
attractions = []
reviews=[]
for name in soup.findAll('div',{'class':'XfVdV o AIbhI'}):
   attractions.append(name.text)
for review in soup.findAll('span',{'class':'biGQs _P pZUbB biKBZ osNWb'}):
    reviews.append(review.text.strip())
# Create the dictionary.
dict = {'Attraction name':attractions, 'Number of reviews': reviews}

# Create the dataframe.
cairo = pd.DataFrame.from_dict(dict)
cairo.head(10)

# Convert dataframe to CSV file.
cairo.to_csv('attractions.csv', index=False, header=True)