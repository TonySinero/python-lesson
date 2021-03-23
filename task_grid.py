def grid (x,y):
    for i in range(x):  # Rows
        print('+ - - - - + - - - - +')
        for j in range(y):  # Columns
            print('|         |         |')
    print('+ - - - - + - - - - +')
grid(2,4)


def myfunc1():
  x = "+"
  y = "-"
  z = "|"

  def myfunc2():
    nonlocal x,y,z
    print(f'{x} {y * 4} {x} {y * 4} {x}')
    print(f'{z}      {z}      {z}')
    print(f'{z}      {z}      {z}')
    print(f'{z}      {z}      {z}')
    print(f'{z}      {z}      {z}')
    print(f'{x} {y * 4} {x} {y * 4} {x}')
    print(f'{z}      {z}      {z}')
    print(f'{z}      {z}      {z}')
    print(f'{z}      {z}      {z}')
    print(f'{z}      {z}      {z}')
    print(f'{x} {y * 4} {x} {y * 4} {x}')
  myfunc2()
  return x,y,z

myfunc1()

def print_border():
    print("+", "- " * 4, "+","- " * 4,"+")


def print_row():
    print("|", " " * 8, "|"," " * 8, "|")


print_border()
print_row()
print_row()
print_row()
print_row()
print_border()
print_row()
print_row()
print_row()
print_row()
print_border()

def do_Func(funck, value, iter):
    i = 0
    while i < iter:
        funck(value)
        i = i+1

def printer(value):
    print(value)



colCell = '+ - - - - + - - - - +'
rowCell = '|         |         |'

do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)