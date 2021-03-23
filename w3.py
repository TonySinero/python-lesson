import time
func = lambda name: print(f'Hello {name} ')
print(list(map(lambda x:str(x),(1, 2, 3))))

res = filter(lambda x:'k' in x,('kanon','lisa','grink'))
print(list(res))

from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,]
filtered = list(filter(lambda x: x % 3 == 0,nums))
result = reduce(lambda x,y : x * y, filtered)
print(result)

print(reduce(lambda x,y: x * y, filter(lambda x: x % 3 == 0, nums)))




def print_copyright(func):
    def wrap():
        print("It is my code")
        func()

    return wrap


def counter(func):
    count = 0

    def wrap():
        nonlocal count
        count += 1
        func()
        print(f"count is {count}")

    return wrap


@print_copyright
def print_hello():
    print("Hello!")


@print_copyright
@counter
def print_bye():
    print("Bye!")



print_hello()
print_bye()
print_bye()
print_bye()

# Start 9.06
def calc_time(func):
    def wrap(*args, **kwargs):
        start_at = time.time()
        res = func(*args, **kwargs)
        end_at = time.time()
        print(f"{end_at - start_at}")
        return res

    return wrap


@calc_time
def long(n):
    for _ in range(n):
        pass


@calc_time
def short(n, x):
    for _ in range(n, x):
        pass


long(100500 * 1000)
short(1, x=100)

