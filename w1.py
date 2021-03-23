import random
def create_matrix(x,y):
    rows = []
    for _ in range(x):
        stolb = []
        for _ in range(y):
            stolb.append(random.randint(0,10))
        rows.append(stolb)
    return rows


def square_matrix(lengh):
    return create_matrix(lengh,lengh)

def devide_matrix(matrix, devide):
    sum = 0
    for parentlist in matrix:
        for itemlist in parentlist:
            if itemlist % devide == 0:
                sum += itemlist
    return sum

def count_of_matrix(matrix,number):
    count = 0
    for parentlist in matrix:
        for itemlist in parentlist:
            if number == itemlist:
                count += 1
    return count

def sum_matrix(matrix):
    count = 0
    sum = 0
    for parentlist in matrix:
        for itemlist in parentlist:
            count += 1
            sum += itemlist
        av = sum/count
    return av


def calc_elements(matrix, average):
    count = 0
    for parentIndex, parentList in enumerate(matrix):
        print(f"parentInx: {parentIndex}, parentlist: {parentList}")
        for childIndex, childlist in enumerate(parentList):
            print(f"childInx: {childIndex}, childlist: {childlist}")
            if childIndex > average and (parentIndex + childIndex) % 2 == 0:
                count += 1
    return count

# vrvrt = square_matrix(5)
# chfk = sum_matrix(vrvrt)
# print(vrvrt)
# print(calc_elements(vrvrt,sum_matrix(vrvrt)))

lst = ['Петрова', 'Сидоров']
def print_lastnames(names):
    for name in names:
        if name[0] == 'П' and name[-1] == 'а':
            print(name)
# print_lastnames(lst)

pupils = [{"name":"User1","physics":5,"history":7}, {"name":"User2","physics":3,"history":2}, {"name":"User2","physics":6,"history":4}]
def calc_av_score(users):
    for user in users:
        av = (user["physics"] + user["history"]) / 2
        user["score"] = av

calc_av_score(pupils)

def print_good_students(students, needScore):
    for student in students:
        if student["score"] >= float(needScore):
            print(f'Good student is: {student["name"]}')

print_good_students(pupils, 4)


