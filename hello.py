def main():
    name = int(input("What's your name? "))
    print(hello(name))

    
# printing in this function would be a side effect.
# raising it to the main function keeps side effects in one place.
# limit side effects for better testing
def hello(to = "world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()