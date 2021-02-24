a = 1
b = 1
ldd = [a, b,]
while len(ldd) < 15:
    c = ldd[-1] + ldd[-2]
    ldd.append(c)
print(ldd)