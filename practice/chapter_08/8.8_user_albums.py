def make_album(singer_name, album_name, songs_number=None):
    """Return a dictionary with singer and album."""
    if songs_number:
        album = {
            'singer': singer_name,
            'album': album_name,
            'songs_number': songs_number}
    else:
        album = {
            'singer': singer_name,
            'album': album_name}
    return album

# Prepare the prompts.
prompt_singer = "\nPlease enter the singer and album: "
prompt_album = "\nPlease enter the singer's album: "
prompt_quit = "\nDo you want to input another singer? yes/no: "

while True:
    singer_input = input(prompt_singer)
    album_input = input(prompt_album)
    album = make_album(singer_input, album_input)
    print(album)

    quit_input = input(prompt_quit)
    if quit_input != 'yes':
        break

# 注意在任何时候都可以退出的机制设计。
"""reference    
# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")
"""