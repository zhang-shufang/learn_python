# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'type': 'dog',
    'owner': 'daixinyue'
    }
pets.append(pet)

pet = {
    'type': 'cat',
    'owner': 'zhangshufang'
    }
pets.append(pet)

pet = {
    'type': 'fish',
    'owner': 'huyao'
    }
pets.append(pet)

for pet in pets:
    for key, value in pet.items():
        if type(value) != int:
            print(f"{key}: {value.title()}")
        else:
            print(f"{key}: {value}")
    print()