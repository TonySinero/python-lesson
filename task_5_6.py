import random
myList = []
a = 0
count = 0
while a < 20:
    myList.append(random.randint(0,20))
    a += 1
    for i in range(0, len(myList)):
        if myList[i-1] < myList[i]:
            count += 1
print(count)
