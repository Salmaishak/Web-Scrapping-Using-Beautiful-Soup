import requests

first_part_of_uri_restaurant = "https://www.tripadvisor.com/"


def getHTMLdocument(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': 'foo'})
    if response.status_code !=200:
        print("failed to response")
        return False
    return response.text


def getNextReviewsLink(soup):
    next = ""
    for i in soup.findAll("a", {"class": "nav next ui_button primary"}):
        next = i.get("href")
        break
    return next

def getURLForSecondPage(soup):
    try:
        next = soup.find("a", {"class": "nav next rndBtn ui_button primary taLnk"})
        url_next_page = next.get("href")
        return first_part_of_uri_restaurant + url_next_page
    except:
        print("All pages is Done")
        return False