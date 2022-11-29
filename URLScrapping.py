# Import the libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Extract the HTML and create a BeautifulSoup object
url = 'https://www.tripadvisor.in/Hotels-g294201-Cairo_Cairo_Governorate-Hotels.html'

user_agent = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
               'Accept-Language': 'en-US, en;q=0.5'})
def createSoup(url):
    page = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup
# Find and extract the data elements.
soup= createSoup(url)

hotels = []
for name in soup.findAll('div', {'class': 'listing_title'}):
    hotels.append(name.text.strip())
#ratings
ratings = []
for rating in soup.findAll('a', {'class': 'ui_bubble_rating'}):
    ratings.append(rating['alt'])
#number of reviews
Numberreviews = []
for review in soup.findAll('a', {'class': 'review_count'}):
    Numberreviews.append(review.text.strip())
#prices
prices = []
for p in soup.findAll('div', {'class': 'price-wrap'}):
    prices.append(p.text.replace('₹', '').strip())
#links
#function to crawl reviews from links and add it to a csv file
reviews=[]
links=[]
def crawlReviews(url):
    soup=createSoup(url)
    for review in soup.findAll('q', {'class': 'QewHA H4 _a'}):
       # print(review.text)
        reviews.append(review.text)
        links.append(url) #using link as a reference key for hotels
#websites
websites=[]
for w in soup.findAll('div', {'class': 'listing_title'}):
    linksForReviews="https://www.tripadvisor.in"+ w.a.get("href")
    websites.append(linksForReviews)
    crawlReviews(linksForReviews) #reviews being crawled per link
# Create the dictionary one for info per hotel, and one for reviews
dict = {'Hotel Names': hotels, 'Ratings': ratings, 'Number of Reviews': Numberreviews, 'Prices': prices, 'links': websites}
dict2= {'hotel Names':links, 'Review': reviews}

# Create the dataframe.
cairo = pd.DataFrame.from_dict(dict)
review = pd.DataFrame.from_dict(dict2)
cairo.head(10)

# Convert dataframe to CSV file.
cairo.to_csv('hotels.csv', index=False, header=True)
review.to_csv('hotelReview.csv', index=False, header=True)