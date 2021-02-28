family = input()
age = 0
if family.isdigit():
    age = int(family)
    if age > 50:
        print('to order restaurant')
    elif age in range(20,50):
        print('to order caffe')
    elif age < 20:
        print('home, sweet home')
