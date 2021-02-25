a,b = 1,1
ldd = [a, b,]
while len(ldd) < 15:
    c = ldd[-1] + ldd[-2]
    ldd.append(c)
print(ldd)

#------------------------------

a,b = 1,1
ldd = [a, b,]
for x in ldd:
    x = ldd[-1] + ldd[-2]
    ldd.append(x)
    if len(ldd) > 14:
        break

print(ldd)


