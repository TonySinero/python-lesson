m = int(input())
n = int(input())
x = range(m,n)
for i in x:
    for e in range(2,i-1):
        if i % e == 0:
            print ("Chislo",i, "Delitel",e)