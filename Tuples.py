# tuples are similar to lists but once a tuple is created, you cannot add, delete, replace or reorder elements

t1 = ()

t2 = (11, 25, 46)

t3 = ([1, 2, 3, 4, 5])

t4 = tuple("abc")

print(t1)
print(t2)
print(t3)
print(t4)

print(min(t2))
print(max(t2))
print(len(t3))
print(sum(t3))

# iterating through tuples

t = (1, 5, 6, 7, 3)

for i in t:
    print(i, end=" ")

# slicing tuples
print(t[0:2])
print(t[2:4])

# in and not in operator
print(5 in t)
print(5 not in t)
