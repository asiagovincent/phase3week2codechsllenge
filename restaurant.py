# restaurant.py

class Restaurant:
    # Class variable to store all restaurants
    all_restaurants = []

    # Constructor to initialize the restaurant object with a name
    def __init__(self, name):
        # Name of the restaurant
        self.name = name
        # List to store reviews for this restaurant
        self.reviews = []
        # Adding the restaurant to the list of all restaurants
        Restaurant.all_restaurants.append(self)

    # Method to calculate and return the average star rating for the restaurant
    def average_star_rating(self):
        # Calculate the total rating 
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews) if len(self.reviews) > 0 else "No ratings yet"

