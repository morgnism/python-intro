def meow(n: int) -> None: # annotate the return of a function with a `void` type
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)