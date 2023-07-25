cities = {
    'beijing': {
        'country': 'china',
        'population': 1200e4,
        'fact': 'It is the capital of China.'
    },
    'newyork':{
        'country': 'USA',
        'population': 300e4,
        'fact': 'Times Square is in there.'
    },
    'paris':{
        'country': 'france',
        'population': 200e4,
        'fact': 'It is famous for its food.'
    }   
}

for city, information in cities.items():
    print(f"{city.title()}'s information is:")
    
    for key, value in information.items():
        if key == 'country':
            print(f"{key}: {value.title()}")
        else:
            print(f"{key}: {value}")
    
    print()

"""参考答案
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")
"""