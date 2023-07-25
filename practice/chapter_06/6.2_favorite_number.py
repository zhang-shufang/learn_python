persons_numbers = {'tony': '1',
                  'jerry': '2',
                  'tom': '3',
                  'eric': '4',
                  'larry': '5'
                 }

for person in persons_numbers:
    print(f'{person.title()}: {persons_numbers[person]}')