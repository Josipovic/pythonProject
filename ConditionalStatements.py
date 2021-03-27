a = 10
# Example 1
if a > 20:
    print("True condition")
else:
    print("False condition")


# Example 2
b = 10

if b % 2 == 0:
    print("Number is even number")
else:
    print("Number is odd")

print("This is not part of if or else blocks")


# Example 3 Single statement
print("welcome") if True else print("Python")

# Example 4 Multiple statements
print("welcome"), print("welcome again") if True else print("Python")

{print("welcome"), print("welcome again") if True else print("Python"), print("python 2")}


# elif
m = 10
if m == 10:
    print("Ten")
elif m == 20:
    print("Twenty")
elif m == 30:
    print("Thirty")
else:
    print("Not listed")
