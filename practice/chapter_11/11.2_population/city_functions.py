def format_city(city_name, city_country, polulation=None):
    """This function return a message of format city information."""
    format_city_msg = f"{city_name.title()}, {city_country.title()}"
    if polulation != None:
        format_city_msg +=  f" - population {polulation}"
    return format_city_msg