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


#Practicing __init__ method

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User("Jungwoo Lee", "jwlee2020@gmail.com", "205527")
user2 = User("Sanggil Jeong", "dopa1993@gmail.com", "350000")
print(user1.name, user1.email, user1.password)
print(user2.name)


