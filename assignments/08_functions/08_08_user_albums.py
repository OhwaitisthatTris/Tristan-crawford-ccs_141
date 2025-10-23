def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    artist = input("Enter the artist's name (or type 'quit' to finish): ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album title: ")

    # Prompt the user for the number of songs (optional)
    songs = input("Enter the number of songs on the album (or press Enter to skip): ")
    if songs:
        try:
            songs = int(songs)
        except ValueError:
            print("Invalid number entered for songs; skipping song count.")
            songs = None
    else:
        songs = None

    # Create the album dictionary
    album = make_album(artist, title, songs)

    # Print the dictionary
    print(f"\nAlbum information: {album}\n")