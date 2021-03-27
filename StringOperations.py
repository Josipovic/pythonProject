# Creating strings
name1 = "John"
name2 = 'John'
name3 = str("welcome")

print(name1 * 3)  # print name 3 times

# slicing string
print(name3[1:3])
print(name3[:6])
print(name3[4:])

print(ord('Z'))  # ascii

# len() returns length of the string
print(len(name3))

# max() returns character having highest ascii value
print(max(name3))

# min() returns character having lowest ascii value
print(min(name3))

# "in" checks existence of string in another string
print("wel" in name3)

# "not in" checks if given string is not in another string
print("nesto" not in name3)

# string comparision  ==, !=, >, >=, <, <=, >
print("time" == "time")

s = "Python"

# for loop
for i in s:
    print(s)

# testing strings

# isalnum() returns true if string is alpahumeric
print("welcome".isalnum())  # false

# isalpha() returns true if string contains only alphabets
print("welcome".isalpha())  # true

# isdigit() returns true if string contains only digits
print("2012".isdigit())  # true

# isidentifier() returns true if string is a valid identifier
print("first Number".isidentifier())  # false

# islower() returns true if string is in lowercase
print("welcome".islower())  # true

# isupper() returns true if string is in uppercase
print("WELCOME".isupper())  # true

# isspace() returns true if string contains only whitespace
print(" ".isspace())

# searching for substrings
ss = "Welcome to python"
# endswith(s1:str) returns true if string ends with substring s1
print(ss.endswith("thon"))

# startswith(s1:str) returns true if string starts with substring s1
print(ss.startswith("wel"))

# count(substring) returns number of occurences of substring the string
print(ss.count("o"))

# finds(s1) returns lowest index from where s1 starts in the string. If string is not found returns -1
print(ss.find("welcome"))

# rfinds(s1) returns highest index from where s1 starts in the string. If string is not found returns -1
print(ss.rfind("o"))



