
class Review:
    # empty list  to store all reviews
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # The customer who wrote the review
        self.customer = customer
        self.restaurant = restaurant
        # The rating given in the review
        self.rating = rating
        # Add this review to the customer's and restaurant's review lists
        self.customer.reviews.append(self)
        self.restaurant.reviews.append(self)
        # Add this review to the list of all reviews
        Review.all_reviews.append(self)