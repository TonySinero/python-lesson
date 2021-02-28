import random
myList = []
a = 0
while a < 19:
    myList.append(random.randint(0,19))
    a += 1
    m = max(myList)
for i in range(0, len(myList), 2):
    myList[i] = m
print(myList)