import csv

headers = ["Name", "City", "phone_no", "location", "price_range", "cuisines", "special_diets", "open_time",
           "close_time", "rate", "number of reviews"]

initial_write=True

def add_restaurant(restaurant, initial_write):
    with open('restaurants_data_alex.csv', mode='a', encoding='utf-8', errors='ignore', newline='') as file:
        writer = csv.writer(file)
        # r.displayData()
        if initial_write is True:
            writer.writerow(headers)
            write_reviews(restaurant, initial_write)
            return
        data = [restaurant.name, restaurant.city, restaurant.phone_no, restaurant.location, restaurant.price_range, restaurant.cuisines, restaurant.special_diets, restaurant.open_time,
                restaurant.close_time, restaurant.rate, restaurant.number_of_reviews]
        writer.writerow(data)

    write_reviews(restaurant,initial_write)


def write_reviews(restaurant,initial_write):
    with open('alex_reviews.csv', mode='a', encoding='utf-8', errors='ignore', newline='') as file:
        writer = csv.writer(file)
        if initial_write is True:
            headers = ["restaurant_name", "review"]
            writer.writerow(headers)
            return
        for review in restaurant.reviews:
            data = [restaurant.name, review]
            writer.writerow(data)

