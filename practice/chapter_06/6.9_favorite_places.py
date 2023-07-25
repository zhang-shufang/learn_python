favorite_places = {
    'zhangshufang': ['xinjiang', 'yunnan', 'hainan'],
    'daixinyue': ['neimeng', 'italy', 'chengdu'],
    'huyao': ['mengzi', 'jilin']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite place are:")
    for place in places:
        print(place.title())
