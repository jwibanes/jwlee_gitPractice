#This file is created for practicing basic codes in python


#Picking numbers using sampling without replacement
#A function to pick 3 random integers from 1 to 10
from random import randint

def sample_without_replacement():
    numbers = []
    while len(numbers) < 3:
        picked_number = randint(1,10)
        if picked_number not in numbers:
            numbers.append(picked_number)

    return(numbers)

#Code to execute function
print(sample_without_replacement())