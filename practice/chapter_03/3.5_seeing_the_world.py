locations = ['xinjiang', 'xizang', 'neimenggu', 'hainan', 'taiwan']
print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("Original order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("Original order:")
print(locations)

print("\nReverse:")
locations.reverse()
print(locations)
#print(locations.reverse())
#注意！！！！！！！！！！！！这里不返回值，所以打印出来为None

print("Original order:")
locations.reverse()
print(locations)

print("\nAlphabetical:")
locations.sort()
print(locations)

print("\nReverse alphabetical:")
locations.reverse()
print(locations)