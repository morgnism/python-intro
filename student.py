def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[2]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] # <--- change tuple to list to convert between immutable to mutable

if __name__ == "__main__":
    main()