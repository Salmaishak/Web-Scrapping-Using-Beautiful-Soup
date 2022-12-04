import csv
headers=["Name","City","phone_no","location","price_range","cuisines","special_diets","open_time","close_time","rate","number of reviews"]

def add_restaurant(resturants_list):
    with open('restaurants_data.csv', 'w',encoding='utf-8',errors='ignore',newline='') as file:
        writer = csv.writer(file)
        # r.displayData()
        writer.writerow(headers)
        for r in resturants_list:
            data = [r.name, r.city, r.phone_no, r.location, r.price_range, r.cuisines, r.special_diets, r.open_time,
                    r.close_time, r.rate,r.number_of_reviews]
            writer.writerow(data)
    write_reviews(resturants_list)

def write_reviews(resturants_list):
    with open('restaurant_review.csv', 'w', encoding='utf-8', errors='ignore',newline='') as file:
        writer = csv.writer(file)
        headers=["restaurant_name","review"]
        writer.writerow(headers)
        for restaurant in resturants_list:
            for review in restaurant.reviews:
                data= [restaurant.name, review]
                writer.writerow(data)

