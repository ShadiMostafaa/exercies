import random

randomNum = random.randint(1, 20)
print(randomNum)
user = 0
while True:
    user = int(input("Please neter a number between 1 and 20"))
    print(user)
    print(randomNum)
    if user == randomNum:
        break
    print("Not Correct")
print("Correct")
