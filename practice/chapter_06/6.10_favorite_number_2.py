persons_numbers = {'tony': ['1', '3', '5'],
                  'jerry': ['2', '4', '6'],
                  'tom': ['3', '6', '9'],
                  'eric': ['4', '7', '3'],
                  'larry': ['5']
                 }

for person, numbers in persons_numbers.items():
    print(f'{person.title()}:')
    for number in numbers:
        print(number)