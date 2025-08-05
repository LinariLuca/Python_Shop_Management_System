from Person import Person

class Customer(Person):

    # Logic: 'origin' is useful for market analysis to understand where customers come from (can later be used for statistics/graphs)
    # Loyalty card could apply a discount when calculating the total (e.g., 10% or 20%) inside the "sum_shopCar" method
    def __init__(self, last_name, first_name, origin):
        super().__init__(last_name, first_name)
        self.__origin = origin
        self.__reviews = []

    # Getters
    def get_origin(self):
        return self.__origin

    def get_reviews(self):
        return self.__reviews

    # Setters
    def set_origin(self, origin):
        self.__origin = origin

    # Customer can leave a review (from 0 to 5 stars)
    def write_review(self):
        try:
            review = int(input("Please leave a review from 0 to 5 ⭐ (where 0 is lowest and 5 is highest): "))
        except ValueError:
            review = 0

        if review < 0 or review > 5:
            review = 0

        self.__reviews.append(review)
