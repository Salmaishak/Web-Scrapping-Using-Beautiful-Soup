from bs4 import BeautifulSoup
from RestaurantsPackage import HelperFunctions
from RestaurantsPackage import Restaurant

hotel_id=1
first_part_of_uri_restaurant = "https://www.tripadvisor.com/"



tripadvisor_restaurants_url = "https://www.tripadvisor.com/Restaurants-g294201-zfp19-Cairo_Cairo_Governorate.html"

home_html_document = HelperFunctions.getHTMLdocument(tripadvisor_restaurants_url)

restaurant_list=[]

while home_html_document is not False:
    soup = BeautifulSoup(home_html_document, 'lxml')

    Restaurants = soup.findAll("a", {"class": "Lwqic Cj b"})

    for restaurant_full_html in Restaurants:
        # break
        tmp_restaurant =Restaurant.Restaurant()

        tmp_restaurant.city="Cairo"

        # assign hotel id
        tmp_restaurant.id=hotel_id

        hotel_id=hotel_id+1 # increment hotel id by 1
        restaurant_url = first_part_of_uri_restaurant + restaurant_full_html.get("href")
        restaurant_html_page = HelperFunctions.getHTMLdocument(restaurant_url)
        restaurant_soup = BeautifulSoup(restaurant_html_page, 'lxml')
        # print(restaurant_soup)

        # get website link
        # for i in restaurant_soup.findAll("a",{"class":"YnKZo Ci Wc _S C AYHFM"}):
        #     # HelperFunctions.getHREF(restaurant_url)
        #     print(i)
        #     # tmp_restaurant.website_link = i.get('href')
        #     # print(tmp_restaurant.website_link)
        #     break

        # get number of reviews
        for i in restaurant_soup.findAll("a", {"class": "BMQDV _F G- wSSLS SwZTJ"}):
            tmp_restaurant.number_of_reviews = i.get_text()
            break
        # print(rest.number_of_reviews)

        # get phone number
        for i in restaurant_soup.findAll("span", {"class": "AYHFM"}):
            a = i.find('a')
            # print(a.get("href"))
            tmp_restaurant.phone_no = a.get_text()
            break
        # print("Phone no" + rest.phone_no)

        # get name
        for i in restaurant_soup.findAll("div", {"class": "acKDw w O"}):
            h1 = i.find("h1")
            # print(h1.get_text())
            tmp_restaurant.name = h1.get_text()
            break

        # get reviews
        ctr = 0
        reviews_list = restaurant_soup.findAll("p", {"class": "partial_entry"})
        while len(reviews_list) != 0 and ctr <= 1:
            # print(ctr)
            ctr = ctr + 1
            for review in reviews_list:
                tmp_restaurant.reviews.append(review.get_text())

            next_url_for_reviews = first_part_of_uri_restaurant + HelperFunctions.getNextReviewsLink(restaurant_soup)

            reviews_content = HelperFunctions.getHTMLdocument(next_url_for_reviews)
            reviews_soup = BeautifulSoup(reviews_content, 'lxml')
            reviews_list = reviews_soup.findAll("p", {"class": "partial_entry"})


        # ctr 0 for price range
        # ctr 1 for cuisines
        ctr = 0
        for i in restaurant_soup.findAll("div", {"class": "SrqKb"}):
            if ctr == 0:
                ctr = ctr + 1
                tmp_restaurant.price_range = i.get_text()
                continue
            tmp_restaurant.cuisines = i.get_text()
            break

        # get special diets
        ctr = 0
        for i in restaurant_soup.findAll("div", {"class": "SrqKb"}):
            if ctr == 2:
                tmp_restaurant.special_diets = i.get_text()
                break
            ctr = ctr + 1

        restaurant_list.append(tmp_restaurant)
        break
    # ya rab yekhlas run baaa

    url_next_page=HelperFunctions.getURLForSecondPage(soup)
    if url_next_page is False:
        break
    print(url_next_page)
    print(len(restaurant_list))
    home_html_document=HelperFunctions.getHTMLdocument(url_next_page)
    # testttt
    print(restaurant_list[0].displayData())
    # for rest in restaurant_list:
    #     print(rest.displayData())