import requests

first_part_of_uri_restaurant = "https://www.tripadvisor.com/"


def getHTMLdocument(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers={'Accept': 'application/xml; charset=utf-8', 'User-Agent': 'foo'})
    if response.status_code != 200:
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


def getHREF(url):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time

    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    # This next line does not show the expected html.
    # print (driver.page_source)

    # But this finds it.
    body = driver.find_element_by_tag_name("a").get_attribute('innerHTML')
    driver.quit()
    soup = BeautifulSoup(body, "html.parser")
    ps = soup.find_all("a", {"class": "YnKZo Ci Wc _S C AYHFM"})
    for p in ps:
        print(p)


def get_text_of_html_tag(soup, html_tag, class_name, no_of_find,inside_html_tag):
    try:
        ctr = 0
        for i in soup.findAll(html_tag, {"class": class_name}):
            if ctr == no_of_find:
                if inside_html_tag is not False:
                    x = i.find(inside_html_tag)
                    # print("x : "+str(x))
                    # if inside_html_tag =="a":
                    #     return x.get
                    return x.get_text()
                return i.get_text()
            ctr = ctr + 1
        return "None"
    except:
        return "None"
