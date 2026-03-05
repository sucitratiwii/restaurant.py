class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email

    def describe_user(self):
        print(f"Full name : {self.first_name} {self.last_name}")
        print(f"Age       : {self.age}")
        print(f"Gender    : {self.gender}")
        print(f"Email     : {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")


# User 1
user1 = User('Rina', 'Putri', 21, 'Female', 'rina@email.com')

print(f"First name is {user1.first_name}.")
print(f"Last name is {user1.last_name}.")
user1.describe_user()
user1.greet_user()
print()


# User 2
user2 = User('Dimas', 'Prakoso', 22, 'Male', 'dimas@email.com')

print(f"First name is {user2.first_name}.")
print(f"Last name is {user2.last_name}.")
user2.describe_user()
user2.greet_user()
print()


# User 3
user3 = User('Alya', 'Rahma', 20, 'Female', 'alya@email.com')

print(f"First name is {user3.first_name}.")
print(f"Last name is {user3.last_name}.")
user3.describe_user()
user3.greet_user()
print()