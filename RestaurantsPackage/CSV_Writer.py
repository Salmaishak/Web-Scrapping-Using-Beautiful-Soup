import csv

headers = ["Name", "City", "phone_no", "location", "price_range", "cuisines", "special_diets","meals", "open_time",
           "close_time", "rate", "number of reviews"]

initial_write=True

def add_restaurant(restaurant, initial_write):
    with open('Luxor.csv', mode='a', encoding='utf-8', errors='ignore', newline='') as file:
        writer = csv.writer(file)
        # r.displayData()
        if initial_write is True:
            writer.writerow(headers)
            return
        data = [restaurant.name, restaurant.city, restaurant.phone_no, restaurant.location, restaurant.price_range,
                restaurant.cuisines, restaurant.special_diets,
                restaurant.meal,restaurant.open_time,
                restaurant.close_time, restaurant.rate, restaurant.number_of_reviews]
        writer.writerow(data)



