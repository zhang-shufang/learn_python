def build_car_info(manufacturer, model, **car_info):
    """Build a dictionary containing everything about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_byd = build_car_info('BYD', '秦',
                        price='20_0000',
                        color='white')

print(car_byd)

# 注意函数内最好还是把字典的添加给显性地写出来。

"""reference
def make_car(manufacturer, model, **options):
    # Make a dictionary representing a car.
    *********************************
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value
    *********************************
    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)
"""