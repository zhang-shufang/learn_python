rivers = {'Yellow River': 'China',
          'Changjiang River': 'China',
          'Amazon': 'Brazil'}

for river, nation in rivers.items():
    print(f"The {river} runs through {nation}.")

for river in rivers.keys():
    print(river)

for nation in rivers.values():
    print(nation)