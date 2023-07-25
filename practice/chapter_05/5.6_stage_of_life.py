age = int(input("Please type the age:"))
stage = ""
if age < 2:
    stage = "infant"
elif age >= 2 and age < 4:
    stage = "toddler"
elif age >= 4 and age < 13:
    stage = "child"
elif age >= 13 and age < 18:
    stage = "adolescent"
elif age >= 18 and age < 65:
    stage = "young adult"
else:
    stage = "old person"
print(f"This person is a {stage}")

"""答案如下
age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 18:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")
"""