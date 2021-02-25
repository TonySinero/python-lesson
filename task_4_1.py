listin = [15, 56, 64, 561, 9, 94, 12, ]
listen2 = []
for x in listin:
    a = x * (-2)
    listen2.append(a)

print(listen2)
#---------------------------------------

list = [15, 56, 64, 561, 9, 94, 12, ]
list2 = []
i = 0
while i < len(list):
    num = list[i]
    x = num * (-2)
    i += 1
    list2.append(x)

print(list2)