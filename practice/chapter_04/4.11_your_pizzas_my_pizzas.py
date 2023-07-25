pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = pizzas[:]

# Add a pizza to the pizzas.
pizzas.append('boluo')

# Add another pizza to the friend_pizzas
friend_pizzas.append('haixian')

# Check out the two lists of pizzas.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)
