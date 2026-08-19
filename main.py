import random
random_numbers =[]
for i in range(0,10):
    random_numbers.append(random.randint(1,100))
print(random_numbers)
maxNum = max(random_numbers)
print(maxNum)
minNum = min(random_numbers)
print(minNum)
sumNum = sum(random_numbers)
print(sumNum)
avg = sum(random_numbers)/len(random_numbers)
print(avg)
print("SHADI")
gg