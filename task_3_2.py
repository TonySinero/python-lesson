family = int(input())
if family > 50:
    print('to order restaurant')
elif family > 20 and family < 50:
    print('to order caffe')
elif family < 20:
    print('home, sweet home')