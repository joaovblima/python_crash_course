def make_album(name_artist, album_title, launched_year=None):
    artis_info = {'name': name_artist, 'album': album_title}
    if launched_year:
        artis_info['launched_year'] = launched_year
    return artis_info


while True:
    print("\nDigte o nome do artista, nome do album e se lembrar o ano em que foi lançado.")
    print("Pressione 'q' para sair quando quiser. ")

    artista = input('Nome do artista: ')
    if artista == 'q':
        break
    album = input('Nome do album: ')
    if album =='q':
        break

    info_album = make_album(artista, album)
    print(info_album)