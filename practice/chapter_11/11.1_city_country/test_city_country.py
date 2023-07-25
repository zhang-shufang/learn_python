from city_functions import format_city

def test_city_country():
    """Test if function can handle city info like 'shanghai, china'."""
    format_city_info = format_city('shanghai', 'china')
    assert format_city_info == 'Shanghai, China'