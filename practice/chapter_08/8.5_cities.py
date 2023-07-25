def describe_city(city_name, city_country='china'):
    """Print which country the city is in."""
    msg = f"{city_name.title()} is in {city_country.title()}."
    print(msg)

describe_city('shanghai')

describe_city('kunming')

describe_city('tokyo', 'Japan')
