# Tugas:
# 1. Buat kelas bernama Restaurant.
# 2. Metode __init__() untuk Restaurant harus menyimpan dua atribut:
#    - nama restoran (restaurant_name)
#    - jenis masakan (cuisine_type).
# 3. Buat metode bernama describe_restaurant() yang mencetak kedua informasi ini.
# 4. Buat metode bernama open_restaurant() yang mencetak pesan yang menunjukkan
#    bahwa restoran tersebut buka.
# 5. Buat instance bernama restaurant dari kelas Anda.
# 6. Cetak kedua atribut tersebut secara terpisah.
# 7. Lalu panggil kedua metode tersebut.

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





# Soal:
# Dari soal nomor 1, buatlah 3 instance berbeda dari kelas Restaurant,
# dan panggil method describe_restaurant() untuk setiap instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")


# Restaurant 1
restaurant1 = Restaurant('Sugiharti', 'Indonesia')
restaurant1.describe_restaurant()

# Restaurant 2
restaurant2 = Restaurant('Sakura', 'Japanese')
restaurant2.describe_restaurant()

# Restaurant 3
restaurant3 = Restaurant('La Pasta', 'Italian')
restaurant3.describe_restaurant()
