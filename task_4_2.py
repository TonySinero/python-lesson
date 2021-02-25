ls = [1, 2, 3, 54, 55, 74, 45, 10]
count2 = 0
for i in ls:
    if i % 2 == 0:
        count2 += 1

print(count2)

#-----------------------------------


ls2 = [1, 2, 3, 54, 55, 74, 45, 10]
i = 0
count = 0
while i < len(ls2):
    num = ls2[i]
    i += 1
    if num % 2 == 0:
        count += 1

print(count)