import pandas as pd
from bs4 import BeautifulSoup
from RestaurantsPackage import HelperFunctions
from RestaurantsPackage import RestaurantClass
import CSV_Writer

first_part_of_uri_restaurant = "https://www.tripadvisor.com/"

#### NOTE HERE ##################################################
# inspect any of those price range, cuisines, special diets and get its class name
master_class_name = ""
# write the city you which to scrape
city = ""
# put here the url
tripadvisor_restaurants_url = ""


home_html_document = HelperFunctions.getHTMLdocument(tripadvisor_restaurants_url)


# initialize the csv file with headers
CSV_Writer.add_restaurant(None, True)

while home_html_document is not False:

    soup = BeautifulSoup(home_html_document, 'lxml')

    Restaurants = soup.findAll("a", {"class": "Lwqic Cj b"})

    for restaurant_full_html in Restaurants:

        tmp_restaurant = RestaurantClass.Restaurant()
        # assign city
        tmp_restaurant.city = city

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
        tmp_restaurant.number_of_reviews = HelperFunctions.get_text_of_html_tag(restaurant_soup, "a",
                                                                                "BMQDV _F G- wSSLS SwZTJ", 0, False)

        # get phone number
        tmp_restaurant.phone_no = HelperFunctions.get_text_of_html_tag(restaurant_soup, "span", "AYHFM", 0, "a")

        # get name
        tmp_restaurant.name = HelperFunctions.get_text_of_html_tag(restaurant_soup, "div", "acKDw w O", 0, "h1")

        # get rate
        tmp_restaurant.rate = HelperFunctions.get_text_of_html_tag(restaurant_soup, "span", "ZDEqb", 0, False)
        try:
            tmp_restaurant.rate = tmp_restaurant.rate.rstrip(tmp_restaurant.rate[-1])  # remove last index which is A
        except:
            tmp_restaurant.rate = HelperFunctions.get_text_of_html_tag(restaurant_soup, "span", "ZDEqb", 0, False)
            print("Error in getting rate")

        # get meals,price_range, cuisines, special_diets
        try:
            all_divs = restaurant_soup.findAll("div", {"class": "tbUiL b"})
            tmp_restaurant.price_range = "None"
            tmp_restaurant.meal = "None"
            tmp_restaurant.cuisines = "None"
            tmp_restaurant.special_diets = "None"
            ctr = 0
            for d in all_divs:
                # print(d.get_text())
                if d.get_text() == "PRICE RANGE":
                    tmp_restaurant.price_range = HelperFunctions.get_text_of_html_tag(restaurant_soup, "div",
                                                                                      master_class_name, ctr, False)
                elif d.get_text() == "CUISINES":
                    tmp_restaurant.cuisines = HelperFunctions.get_text_of_html_tag(restaurant_soup, "div",
                                                                                   master_class_name, ctr, False)
                elif d.get_text() == "Meals":
                    tmp_restaurant.meal = HelperFunctions.get_text_of_html_tag(restaurant_soup, "div",
                                                                               master_class_name, ctr, False)
                elif d.get_text() == "SPECIAL DIETS":
                    tmp_restaurant.special_diets = HelperFunctions.get_text_of_html_tag(restaurant_soup, "div",
                                                                                        master_class_name, ctr, False)
                ctr = ctr + 1
        except:
            print("Error ")

        # get open times & close times
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
                # get_time(restaurant_soup)
                tmp_restaurant.open_time = "None"
                tmp_restaurant.close_time = "None"
            break

        # get location
        tmp_restaurant.location = HelperFunctions.get_text_of_html_tag(restaurant_soup, "a", "YnKZo Ci Wc _S C FPPgD",
                                                                       0, "span")
        # print("Add a restaurant is Done")
        CSV_Writer.add_restaurant(tmp_restaurant, False)
        # break

        # End of for loop

    url_next_page = HelperFunctions.getURLForSecondPage(soup)
    # break
    if url_next_page is False:
        break
    home_html_document = HelperFunctions.getHTMLdocument(url_next_page)

print("Done ::)")
