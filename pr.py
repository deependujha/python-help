from functools import reduce

def add(x, y):
    print(f"{x=}, {y=}")
    return x + y

numbers = [1, 2, 3, 4, 5]
sum = reduce(add, numbers,100)
print(sum)  # 15