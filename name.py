import sys

# sys.argv[0] is the name of the program running
# print(sys.argv[0])

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
