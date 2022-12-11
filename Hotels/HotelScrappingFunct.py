#in aim to clean the previous code and scrape everything
import csv
from urllib.parse import urljoin

# Extract the HTML and create a BeautifulSoup object
import SoupCreation


urls=['https://www.tripadvisor.in/Hotels-g294201-Cairo_Cairo_Governorate-Hotels.html',
      'https://www.tripadvisor.in/Hotels-g297555-Sharm_El_Sheikh_South_Sinai_Red_Sea_and_Sinai-Hotels.html',
      'https://www.tripadvisor.in/Hotels-g294205-Luxor_Nile_River_Valley-Hotels.html',
      'https://www.tripadvisor.in/Hotels-g297549-Hurghada_Red_Sea_and_Sinai-Hotels.html']
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
        for p in tempsoup.find('div', {'data-sizegroup': 'hr_chevron_prices'}):
          return p.text
    except:
       try:
           for pr in tempsoup.find('div',{'class':'JPNOn b Wi'}):
               return pr.text
       except:
           return""

#Scrap Hotel Aminities
def Aminities(url):
    aminities=""
    tempSoup = SoupCreation.createSoup(url)
    for am in tempSoup.findAll('div', {'data-test-target': 'amenity_text'}):
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
file_name='HotelsHurgada2'
count=1;
#Write inside the CSV file
def WriteInCsv(hotel):
    with open(file_name+".csv", mode='a', newline='',encoding='UTF-8') as Hotels:
        writer = csv.writer(Hotels, delimiter=',')
        writer.writerow(hotel)

#Initiate Column Names for CSV
def initalColumns():
    columns=['name','ratings','prices','aminities','location','description']
    with open(file_name+".csv", mode='a', newline='', encoding='UTF-8') as Hotels:
        writer = csv.writer(Hotels, delimiter=',')
        writer.writerow(columns)


#Main Function
initalColumns()
url=urls[3]
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
        try:
            WriteInCsv(hotels)
        except:
            print(site +"---> ERROR")
    #this if condition gets the next page and changes the url to it
    next_page = soup.find('a', {'class': 'next'})
    print(next_page.get('href'))
    if (next_page):
        next_url = next_page.get('href')
        url = urljoin(url, next_url)
        print(url)
    else:
        break
    #if no more pages exist break
