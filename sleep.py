def main():
    n = int(input("What's n? " ))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        # generators maintain state allowing
        # yield to return iterator for every calculated result on the following line
        yield "🐑" * i

if __name__ == "__main__":
    main()