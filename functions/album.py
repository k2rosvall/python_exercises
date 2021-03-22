def make_album(artist_name, album_title):
    album = {'artist':artist_name, 'name':album_title}
    return album


album1 = make_album('BTS', '2 cool 4 Skool')
print(album1)
album2 = make_album('MAMAMOO', 'Travel')
print(album2)
album3 = make_album('HAIM', 'Days Are Gone')
print(album3)