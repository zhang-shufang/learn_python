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

album = make_album('mayday', '2012', 12)
print(album)

album = make_album('jay chou', 'niuzaihenmang')
print(album)

album = make_album('mayday', 'No.9')
print(album)

# 注意对有无歌曲数的判断写法
"""reference    
def make_album(artist, title, num_songs=0):
    # Build a dictionary containing information about an album.
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', num_songs=8)
print(album)
"""