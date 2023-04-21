# a: int = 5
# b: float = 1.2
# c: str = 't'
# d: list = [5, 6]
# e: bool = True
#
# def task_1(a: int, b: float, c: str, d: list, e: bool):
#     return task_1
# print(type (task_1))

def task_1():
    a: int = 5
    b: float = 1.2
    c: str = 't'
    d: list = [5, 6]
    e: bool = True

    return a, b


t = task_1()

print(t)

def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])

task_2()


def task_3(a: int) -> int:
    return a ** 2


print(task_3(12))
