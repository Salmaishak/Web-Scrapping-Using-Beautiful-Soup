#in aim to clean the previous code and scrape everything
import csv
from urllib.parse import urljoin

# Extract the HTML and create a BeautifulSoup object
import SoupCreation

url = 'https://www.tripadvisor.in/Hotels-g294201-Cairo_Cairo_Governorate-Hotels.html'

#Scrap Hotel Name
def HotelScrapping(url): #note: change the name of the url since it shadows the parameters
        #names
        tempsoup = SoupCreation.createSoup(url)
        for name in tempsoup.find('div', {'class': 'jvqAy'}):
           return name.text
#Scrap Hotel Ratings (out of 5)
def Ratings(url):
    tempsoup = SoupCreation.createSoup(url)
    try:
        for rating in tempsoup.find('div', {'class': 'grdwI P'}):
           return rating.text
    except:
        return ""

#Gets All Hotels Links
def getAllHotels(soup):
    websites=[]
    for w in soup.findAll('div', {'class': 'listing_title'}):
        linksForReviews = "https://www.tripadvisor.in" + w.a.get("href")
        websites.append(linksForReviews)
    return websites

#Scrap Number of reviews
def numOfReviews(url):
    # number of reviews
    tempsoup = SoupCreation.createSoup(url)
    try:
        for review in tempsoup.find('span', {'class': 'qqniT'}):
          return review.text.strip()
    except:
       return ""


#Scrap Prices of Hotel
def Prices(url):
    tempsoup = SoupCreation.createSoup(url)
    try:
        for p in tempsoup.find('div', {'class': 'hhlrH w pUBNi'}):
          return p.text.replace('Â', '').strip()
    except:
         return ""

#Scrap Hotel Aminities
def Aminities(url):
    aminities = ""
    for am in soup.findAll('div', {'class': 'yplav f ME H3 _c'}):
        aminities = aminities + ',' + am.text
        #we seperate aminities from eachother using a comma
    return aminities

#Scrap Hotel's Location
def Location(url):
        tempSoup = SoupCreation.createSoup(url)
        try:
            for loc in tempSoup.find('span', {'class': 'fHvkI PTrfg'}):
               return loc.text
        except:
                return ""

#Scrap Hotel's Description
def Description(url):
        tempSoup = SoupCreation.createSoup(url)
        try:
            for descr in tempSoup.find('div', {'class': 'fIrGe _T'}):
                return descr.text
        except:
            return ""

#Write inside the CSV file
def WriteInCsv(hotel):
    with open('HotelsAll1.csv', mode='a', newline='',encoding='UTF-8') as Hotels:
        writer = csv.writer(Hotels, delimiter=',')
        writer.writerow(hotel)

#Initiate Column Names for CSV
def initalColumns():
    columns=['name','ratings','prices','aminities','location','description']
    with open('HotelsAll3.csv', mode='a', newline='', encoding='UTF-8') as Hotels:
        writer = csv.writer(Hotels, delimiter=',')
        writer.writerow(columns)

#Main Function
initalColumns()
while True:
    #this loop is made to go through all pages
    soup = SoupCreation.createSoup(url)
    #using function get All hotels we get all links to each hotel
    websites=getAllHotels(soup)
    #this for loop scrap each hotel's information
    for site in websites:
        hotels=[]
        hotels.append(HotelScrapping(site))
        hotels.append(Ratings(site))
        hotels.append(Prices(site))
        hotels.append(Aminities(site))
        hotels.append(Location(site))
        hotels.append(Description(site))
        print("hi site for loop ")
        try:
            WriteInCsv(hotels)
        except:
            print(site +"---> ERROR")
    #this if condition gets the next page and changes the url to it
    next_page = soup.find('a', {'class': 'next'})
    if (next_page):
        next_url = next_page.get('href')
        url = urljoin(url, next_url)
        print(url)
    else:
        break
    #if no more pages exist break