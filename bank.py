balance = 0 # can read but can't write to global variables

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    balance +=n

def withdraw(n):
    balance -=n

if __name__ == "__main__":
    main()