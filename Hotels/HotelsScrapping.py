# Import the libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import SoupCreation
import csv

# Extract the HTML and create a BeautifulSoup object
url = 'https://www.tripadvisor.in/Hotels-g294201-Cairo_Cairo_Governorate-Hotels.html'

# Find and extract the data elements.
soup= SoupCreation.createSoup(url)
#names
hotels = []
for name in soup.findAll('div', {'class': 'listing_title'}):
    hotels.append(name.text.replace('Sponsored', '').strip())



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
    prices.append(p.text.replace('Â', '').strip())


#links
reviews=[]
links=[]
def crawlReviews(urls):
    for url in urls:
        tempSoup= SoupCreation.createSoup(url)
        for review in tempSoup.findAll('q', {'class': 'QewHA H4 _a'}):
            reviews.append(review.text)
            links.append(url) #using link as a reference key for hotels
#websites
websites=[]
for w in soup.findAll('div', {'class': 'listing_title'}):
    linksForReviews="https://www.tripadvisor.in"+ w.a.get("href")
    websites.append(linksForReviews)
    #crawlReviews(linksForReviews) #reviews being crawled per link

location=[]
def crawlLocation(urls):
    for url in urls:
        tempSoup = SoupCreation.createSoup(url)
        for loc in tempSoup.find('span', {'class': 'fHvkI PTrfg'}):
            location.append(loc.text)
           # print(loc.text)


#crawling for reviews and locations are seperated in a temp Soup because they go in each link
crawlReviews(websites)
crawlLocation(websites)

dict = {'Hotel Names': hotels, 'Ratings': ratings, 'Number of Reviews': Numberreviews, 'Prices': prices, 'links': websites,'location':location}
dict2= {'hotel Names':links, 'Review': reviews}

# Create the dataframe.
cairo = pd.DataFrame.from_dict(dict)
review = pd.DataFrame.from_dict(dict2)
cairo.head(10)

# Convert dataframe to CSV file.
cairo.to_csv('hotels.csv', index=False, header=True)
review.to_csv('hotelReview.csv', index=False, header=True)