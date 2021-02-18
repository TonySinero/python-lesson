def second(first , second ):
    while True:
        ink = input(first)
        if ink == 'q':
            break
        inv = input(second)
        if inv == 'q':
            break
        return second

    cin = second(inv,ink)