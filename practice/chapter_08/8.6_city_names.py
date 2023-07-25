def city_country(name, country):
    """Return city and its country."""
    return f"{name.title()}, {country.title()}"

msg = city_country('shanghai', 'china')
print(msg)

msg = city_country('yunnan', 'china')
print(msg)

msg = city_country('tokyo', 'japan')
print(msg)