x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is less than y")
# elseif s more performant because the code stops when conditions are met
elif x > y:
    print("x is greater than y")
# else acts as a default
else:
    print("x is equal to y")