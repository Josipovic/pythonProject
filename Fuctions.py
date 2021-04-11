def myfun():
    pass


myfun()


def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result = result + i
        return result


s = sum(10, 20)
print(s)


def sums(starts, ends):
    if (starts > ends):
        print("start should be less than end")
        return
    results = 0
    for i in range(starts, ends + 1):
        results = results + i
        return results


# default value

def someFunc(i, j=100):
    print(i, j)


someFunc(20)


def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a
    