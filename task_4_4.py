# lis = [1, 2, 3, 4, 5, 6 ]
# for x in lis:
#     x = lis[1:]+lis[:1]
#
# print(x)
#--------------------------


a = [1, 2, 3, 4, 5, 6]
b = []
i = 0
while i < len(a):
    x = a[1:] + [0]
    b.append(x)
    i += 1
print(b)