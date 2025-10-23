def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

album1 = make_album('Lil Baby', 'My Turn')
album2 = make_album('Lil Baby', 'The Bigger Picture')
album3 = make_album('Lil Baby', 'It\'s Only Me', songs=16)

print(album1)
print(album2)
print(album3)