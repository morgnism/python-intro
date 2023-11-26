import sys

# sys.argv[0] is the name of the program running
# print(sys.argv[0])

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
