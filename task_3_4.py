enter = input("enter a word: ")

fsrt = len(enter)
mid = fsrt / 2
if fsrt % 2 == 0:
    print(enter[int(mid) - 1:int(mid)])
elif enter[int(mid)] == enter[0]:
    print(enter[1:-1])
elif fsrt % 2 != 0:
    print(enter[int(mid)])
