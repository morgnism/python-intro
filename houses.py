students = [
    {"name": "Hermoine", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set() # only stores one of each element in a list

for student in students:
    houses.add(student["house"]) # set automatically filters dupes

for house in sorted(houses):
    print(house)