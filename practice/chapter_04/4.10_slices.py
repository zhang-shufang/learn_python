# Generate the list.
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
print(cubes)

# Print the first three elements.
print("The first three items in the list are:")
for item in cubes[0:3]:
    print(item)

# Print the middle three elements.
print("Three items from the middle of the list are:")
middle_index = int(len(cubes)/2)
#print(middle_index)
for item in cubes[middle_index - 1 : middle_index + 2]:
    print(item)

# Print the last three elements.
print("The last three items in the list are:")
for item in cubes[-3:]:
    print(item)