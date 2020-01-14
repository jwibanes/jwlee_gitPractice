#This file is created for practicing basic codes in python


# #Picking numbers using sampling without replacement
# #A function to pick 3 random integers from 1 to 10
# from random import randint
#
# def sample_without_replacement():
#     numbers = []
#     while len(numbers) < 3:
#         picked_number = randint(1,10)
#         if picked_number not in numbers:
#             numbers.append(picked_number)
#
#     return(numbers)
#
# #Code to execute function
# print(sample_without_replacement())


# #Practicing __init__ method
# class User:
#     count = 0 #class variable
#
#     def __init__(self, name, email, password): #__init__ automatically called when each user instance is created
#         self.name = name
#         self.email = email
#         self.password = password
#
#         User.count += 1
#
#     def __str__(self): #double underscore method (dunder method), __str__ is automatically called when function print() is called
#         return "Username: {}, Email: {}, Password: *****".format(self.name, self.email)
#
#
# user1 = User("Paul Lee", "lee18@naver.com", "12945")
# user2 = User("Tanaka Akihiro", "Aki4637@yahoo.jp", "48314")
# user3 = User("Shaun Martin", "ShaunGuitar@gmail.com", "38462")
#
# user1.count = 5 #this is not a class variable. this is adding a new instance variable with the same name "count"
# #User.count = 5 redesignates class variable "count"
#
# print(User.count) #prints number of instances
# print(user1.count) #instance variable
# print(user2.count) #class variable
# print(user3.count) #class variable
#
# #Example of decorator function
# #Decorator is useful for indicating starts and ends of multiple functions
#
# def add_print_to(original):
#     def wrapper():
#         print("Start of function")
#         original()
#         print("End of function")
#     return wrapper
#
# @add_print_to
# def print_hello():
#     print("Hello Japan")
# #cf) add_print_to(print_hello) == wrapper
#
# print_hello()


# Understanding instance, class, static
class User:
    count = 0 #class variable

    def __init__(self, name, email, password):
        self.name = name #instance variable
        self.email = email
        self.password = password

        User.count += 1

    def __str__(self):
        return "Username: {}, Email: {}, Password: *****".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("Total number of users is {}".format(cls.count))

    @staticmethod #static method does not include variables
    def is_valid_email(email_address):
        return "@" in email_address


user1 = User("Paul Lee", "lee18@naver.com", "12945") #__init__ method is automatically called when instnace variable is created
user2 = User("Tanaka Akihiro", "Aki4637@yahoo.jp", "48314")
user3 = User("Shaun Martin", "ShaunGuitar@gmail.com", "38462")

#calling instance method
print(user1) # __str__ method is automatically called when print function is used
print(user3.password)

#calling class method
User.number_of_users()
user1.number_of_users()

#calling static method
print(User.is_valid_email(user1.name))
print(User.is_valid_email(user1.email))
