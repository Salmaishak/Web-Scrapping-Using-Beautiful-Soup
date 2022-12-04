import pandas as pd
from bs4 import BeautifulSoup
from RestaurantsPackage import HelperFunctions
from RestaurantsPackage import RestaurantClass
import CSV_Writer

# constant variables
first_part_of_uri_restaurant = "https://www.tripadvisor.com/"
MAX_REVIEWS_PAGE = 75

tripadvisor_restaurants_url = "https://www.tripadvisor.com/Restaurants-g297555-Sharm_El_Sheikh_South_Sinai_Red_Sea_and_Sinai.html"
home_html_document = HelperFunctions.getHTMLdocument(tripadvisor_restaurants_url)

# make a list carry restaurant objects
restaurant_list = []

while home_html_document is not False:

    soup = BeautifulSoup(home_html_document, 'lxml')

    Restaurants = soup.findAll("a", {"class": "Lwqic Cj b"})

    for restaurant_full_html in Restaurants:

        tmp_restaurant = RestaurantClass.Restaurant()
        # assign city
        tmp_restaurant.city = "Cairo"

        restaurant_url = first_part_of_uri_restaurant + restaurant_full_html.get("href")
        restaurant_html_page = HelperFunctions.getHTMLdocument(restaurant_url)
        restaurant_soup = BeautifulSoup(restaurant_html_page, 'lxml')

        # todo
        # get website link
        # for i in restaurant_soup.findAll("a", {"class": "YnKZo Ci Wc _S C FPPgD"}):
        #     # HelperFunctions.getHREF(restaurant_url)
        #     print(i)
        # tmp_restaurant.website_link = i.get('href')
        # print(tmp_restaurant.website_link)
        # break

        # get number of reviews
        for i in restaurant_soup.findAll("a", {"class": "BMQDV _F G- wSSLS SwZTJ"}):
            tmp_restaurant.number_of_reviews = i.get_text()
            break
        tmp_restaurant.number_of_reviews=HelperFunctions.get_text_of_html_tag(restaurant_soup,"a","BMQDV _F G- wSSLS SwZTJ",0,False)

        # get phone number
        tmp_restaurant.phone_no=HelperFunctions.get_text_of_html_tag(restaurant_soup,"span", "AYHFM",0,"a")

        # get name
        tmp_restaurant.name = HelperFunctions.get_text_of_html_tag(restaurant_soup, "div", "acKDw w O", 0, "h1")

        # # get reviews
        ctr = 0
        reviews_list = restaurant_soup.findAll("p", {"class": "partial_entry"})
        while len(reviews_list) != 0 and ctr <= MAX_REVIEWS_PAGE:
            ctr = ctr + 1
            for review in reviews_list:
                tmp_restaurant.reviews.append(review.get_text())

            next_url_for_reviews = first_part_of_uri_restaurant + HelperFunctions.getNextReviewsLink(restaurant_soup)

            reviews_content = HelperFunctions.getHTMLdocument(next_url_for_reviews)
            reviews_soup = BeautifulSoup(reviews_content, 'lxml')
            reviews_list = reviews_soup.findAll("p", {"class": "partial_entry"})

        # ctr 0 for price range
        # ctr 1 for cuisines
        # ctr 2 for special_diets

        # get price range
        try:
            tmp_restaurant.price_range=HelperFunctions.get_text_of_html_tag(restaurant_soup,"div","AGRBq",0,False)
            tmp_restaurant.price_range=tmp_restaurant.price_range.replace('Â', '').strip()
        except:
            tmp_restaurant.price_range=HelperFunctions.get_text_of_html_tag(restaurant_soup,"div","AGRBq",0,False)
            
        # get cuisines
        tmp_restaurant.cuisines=HelperFunctions.get_text_of_html_tag(restaurant_soup,"div","AGRBq",1,False)
        # get special diets
        tmp_restaurant.special_diets=HelperFunctions.get_text_of_html_tag(restaurant_soup,"div","AGRBq",2,False)

        # get rate
        tmp_restaurant.rate = HelperFunctions.get_text_of_html_tag(restaurant_soup, "span", "ZDEqb", 0, False)
        try:
            tmp_restaurant.rate = tmp_restaurant.rate.rstrip(tmp_restaurant.rate[-1])  # remove last index which is A
        except:
            tmp_restaurant.rate = HelperFunctions.get_text_of_html_tag(restaurant_soup, "span", "ZDEqb", 0, False)
            print("Error in getting rate")

        # # get open times
        for i in restaurant_soup.findAll("span", {"class": "mMkhr"}):
            try:
                spans = i.findAll("span")
                # print(spans)
                tmp_restaurant.open_time = spans[4].get_text()
                tmp_restaurant.open_time += spans[5].get_text()
                tmp_restaurant.close_time = spans[8].get_text()
                tmp_restaurant.close_time += spans[9].get_text()
            except:
                print("Error in get open times the restaurant is closed or doesn't set the times ")
                tmp_restaurant.open_time="None"
                tmp_restaurant.close_time="None"
            break

        # get location
        tmp_restaurant.location = HelperFunctions.get_text_of_html_tag(restaurant_soup, "a", "YnKZo Ci Wc _S C FPPgD", 0, "span")
        restaurant_list.append(tmp_restaurant)
        # tmp_restaurant.displayData()
        # CSV_Writer.add_restaurant(restaurant_list)
        # break
        print("len: "+str(len(restaurant_list)))

    # CSV_Writer.add_restaurant(restaurant_list)
    url_next_page = HelperFunctions.getURLForSecondPage(soup)
    # break
    if url_next_page is False:
        break
    home_html_document = HelperFunctions.getHTMLdocument(url_next_page)
    # testttt
    # print(restaurant_list[0].displayData())

print("Finally, Writing now")
CSV_Writer.add_restaurant(restaurant_list)
print("Done ")
