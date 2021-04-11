file = open('file path', 'w')  # open file for writing

file.write('Hello')
file.write('World')

file.close()

# reading all the data at once
file1 = open('', 'r')
file1.read()  # read entire content of file at once
file1.read((10))  # read number of characters from a file

file1.readlines()  # read entire content of a file in array format
file1.readline()  # read the first line

file2 = open('', 'a')  # append data

file.write("dfsss")
