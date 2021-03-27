# Creating lists
list1 = list()  # create an empty list

list2 = list([22, 31, 51])
print(list2)

list3 = list(["tom", "jerry", "spike"])
print(list3)

list4 = list("python")
print(list4)

# Accessing elements in the list
l = [1, 2, 3, 4, 5]
print(l[1])

list5 = [2, 3, 4, 5, 6]
# x in s true if element x is in sequence s
print(2 in list5)

# x not in s if element x is not in sequence s
print(2 not in list5)

# s[i] ith element in sequence s
print(list5[1])

# len(s)  length of sequence s, i.e number of elements in s
print(len(list5))

# min(s) smallest element in sequence s
print(min(list5))

# max(s) largest element in sequence s
print(max(list5))

# sum(s) sum of all numbers in sequence s
print(sum(list5))

# list slicing
list6 = [1, 5, 6, 7, 8, 3, 10]

print(list6[0:5])  # gets 5 elements starting from beginning

print(list1 + list2)
print(list6 * 3)

# for loop

lista = [1, 2, 3, 4, 5]

for i in lista:
    print(i)  # to prin in one line print(i,end=" ")

# list methods with return type
listz = [2, 3, 4, 5, 6, 8]
# append(x:object)  adds an element x to the end of the list and returns none
print(listz.append(19))

# count(x:object) returns the number of times element x appears in the list
print(listz.count(4))

# extend(I:list) appends all the elements in I to the list and returns none
listk = [8, 2]
print(listz.extend(listk))

# index(x:object) returns the index of the first occurrence of element x in the lit
print(listz.index(4))

# insert(index: int, x:object) inserts and element x at a given index
print(listz.insert(1, 25))

# remove(x:object) removes the first occurrence of element x from the list and returns none
listz.remove(8)

# reverse() reverse the list and returns none
listz.reverse()

# sort() sorts the elements in the list in ascending order and returns none
listz.sort()

# pop(i)   removes the element at the given position and returns it
listz.pop(2)

# list comprehension
# example in for loop ---> for x in range(10)

listv = [x for x in range(10)]
print(listv)

# store 1 to 10
listv = [x + 1 for x in range(10)]
print(listv)

# store only even numbers from 1 to 10
listv = [x for  x in range(10) if x % 2 == 0]
print(listv)
