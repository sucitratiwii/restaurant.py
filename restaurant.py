class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")


# Restaurant 1
restaurant = Restaurant('Sugiharti', 'Indonesia')

print(f"The restaurant name is {restaurant.restaurant_name}.")
print(f"This restaurant provides {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()


# Restaurant 2
a_restaurant = Restaurant('Pak Nurdin', 'Indonesia')

print(f"The restaurant name is {a_restaurant.restaurant_name}.")
print(f"This restaurant provides {a_restaurant.cuisine_type} food.")
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()
print()
