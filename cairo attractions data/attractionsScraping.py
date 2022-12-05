import csv
from urllib.parse import urljoin

# Extract the HTML and create a BeautifulSoup object
import SoupCreation
url = 'https://www.tripadvisor.com/Attractions-g294201-Activities-oa90-Cairo_Cairo_Governorate.html'
def AttractionScrapping(url): #note: change the name of the url since it shadows the parameters
        #names
        tempsoup = SoupCreation.createSoup(url)
        for name in tempsoup.find('div', {'class': 'nrbon'}):
           #print(name.text)
           return name.text
# AttractionScrapping(url)
def Ratings(url):
    tempsoup = SoupCreation.createSoup(url)
    try:
        for rating in tempsoup.find('div', {'class': 'biGQs _P fiohW hzzSG uuBRH'}):
           #print(rating.text)
           return rating.text
    except:
        return ""
# Ratings(url)
def getAllAttractions(soup):
    websites=[]
    for w in soup.findAll('div', {'class': 'alPVI eNNhq PgLKC tnGGX'}):
        linksForReviews = "https://www.tripadvisor.in" + w.a.get("href")
        websites.append(linksForReviews)
    return websites
# soup = SoupCreation.createSoup(url)
# getAllAttractions(soup)
def numOfReviews(url):
    # number of reviews
    tempsoup = SoupCreation.createSoup(url)
    try:
        for review in tempsoup.find('span', {'class': 'yyzcQ'}):
          #print(review.text.strip())
          return review.text.strip()
    except:
       return ""
# print(numOfReviews(url))
def openingHours(url):
    tempsoup = SoupCreation.createSoup(url)
    try:
        for openingHour in tempsoup.find('span', {'class': 'EFKKt'}):
          #print(openingHour.text.strip())
          return openingHour.text.strip()
    except:
       return ""
def InterestCategory(url):
    tempsoup = SoupCreation.createSoup(url)
    try:
        for about in tempsoup.find('div', {'class': 'fIrGe _T bgMZj'}):
           #print(about.text)
           return about.text
    except:
        return ""
def WriteInCsv(interest):
    with open('interestsAll1.csv', mode='a', newline='',encoding='UTF-8') as interests:
        writer = csv.writer(interests, delimiter=',')
        writer.writerow(interest)
def initalColumns():
    columns=['Name','Ratings','No. of reviews','Opening hours','Category']
    with open('interestsAll1.csv', mode='a', newline='', encoding='UTF-8') as Interests:
        writer = csv.writer(Interests, delimiter=',')
        writer.writerow(columns)
#################################################################################
##main 

#initalColumns()
while True:
    soup = SoupCreation.createSoup(url)
    websites=getAllAttractions(soup)
    index=1
    for site in websites:
        attractions=[]
        attractions.append(AttractionScrapping(site))
        attractions.append(numOfReviews(site))
        attractions.append(Ratings(site))
        attractions.append(openingHours(site))
        attractions.append(InterestCategory(site))
        print(f"done website {index} ")
        index=index+1
        try:
            WriteInCsv(attractions)
        except:
            print(site +"---> ERROR")
    next_page = soup.find('a', {'class': 'BrOJk u j z _F wSSLS tIqAi unMkR'})
    if (next_page):
        next_url = next_page.get('href')
        url = urljoin(url, next_url)
        print(url)
    else:
        break
