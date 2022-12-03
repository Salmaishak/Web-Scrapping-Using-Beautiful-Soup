class Restaurant:
    id = 0
    city = ""
    name = ""
    location = ""
    phone_no = ""
    website_link = ""
    open_time=""
    close_time=""
    rate = 0.0
    number_of_reviews = ""
    reviews = []
    price_range = ""
    cuisines = ""
    special_diets = ""

    def displayData(self):
        print("Id: " + str(self.id))
        print("Name: " + str(self.name))
        print("City: " + self.city)
        print("location: " + self.location)
        print("phone_no: " + self.phone_no)
        # print("website link: "+self.website_link)
        print("rate: " + str(self.rate))
        print("price range: " + self.price_range)
        print("cuisines: " + self.cuisines)
        print("special diets: " + self.special_diets)
        print("open time: "+self.open_time)
        print("close time: "+self.close_time)
        # print("Reviews: ")
        for review in self.reviews:
            print(review)
