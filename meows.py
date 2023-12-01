def meow(n: int): # add type annotation to param to give it a type hint
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)