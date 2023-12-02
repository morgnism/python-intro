# spread args into the function closer to ...args like in JavaScript
# in python:
#   args = positional arguments.
#          maintains the same order passed in.
#          converts to a tuple if only one list element
#   kwargs = named arguments.
#           maintains the same order passed in.
#           converts automatically to a dictionary
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)