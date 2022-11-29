from bs4 import BeautifulSoup
import requests
from Restaurant import Restaurant


def getHTMLdocument(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': 'foo'})
    return response.text


URL = "https://www.tripadvisor.com/Restaurants-g294201-zfp19-Cairo_Cairo_Governorate.html"

home_html_document = getHTMLdocument(URL)
soup = BeautifulSoup(home_html_document, 'lxml')

Restaurants = soup.findAll("a", {"class": "Lwqic Cj b"})
print(len(Restaurants))
first_part_of_uri_restaurant = "https://www.tripadvisor.com/"

for restaurant in Restaurants:
    rest = Restaurant()
    restaurant_url = first_part_of_uri_restaurant + restaurant.get("href")
    # print(restaurant_url)
    restaurant_html_page = getHTMLdocument(restaurant_url)
    # print(restaurant_html_page)
    restaurant_soup = BeautifulSoup(restaurant_html_page, 'lxml')
    # print(restaurant_soup)

    # for i in restaurant_soup.findAll("a",{"class":"YnKZo Ci Wc _S C AYHFM"}):
    #     print(i)
    #     # rest.website_link = i.get('href')
    #     break

    # get number of reviews
    for i in restaurant_soup.findAll("a", {"class": "BMQDV _F G- wSSLS SwZTJ"}):
        rest.number_of_reviews = i.get_text()
        break
    # print(rest.number_of_reviews)

    # get phone number
    for i in restaurant_soup.findAll("span", {"class": "AYHFM"}):
        a = i.find('a')
        # print(a.get("href"))
        rest.phone_no = a.get_text()
        break
    # print("Phone no" + rest.phone_no)

    # get name
    for i in restaurant_soup.findAll("div",{"class":"acKDw w O"}):
        h1=i.find("h1")
        print(h1.get_text())
        rest.name=h1.get_text()
        break

    # get reviews
    for i in restaurant_soup.findAll("p",{"class":"partial_entry"}):
        rest.reviews.append(i.get_text())
        # print(i.get_text())
    # print(len(rest.reviews))


    # get price range
    for i in restaurant_soup.findAll("div",{"class":"SrqKb"}):
        rest.price_range=i.get_text()
        break

    # get cuisines
    ctr=0
    for i in restaurant_soup.findAll("div",{"class":"SrqKb"}):
        if ctr ==0:
            ctr=ctr+1
            continue
        rest.cuisines=i.get_text()
        break

    # get special diets
    ctr = 0
    for i in restaurant_soup.findAll("div", {"class": "SrqKb"}):
        if ctr == 2:
            rest.special_diets = i.get_text()
            break
        ctr=ctr+1
    print(rest.special_diets)
    break
