favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for name in coders:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for participatint in this investigation.") 
    else:
        print(f"{name.title()}, please come to participate the investigation.")