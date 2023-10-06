def show_music(file_name):
    with open("file_to_choose_songs.txt") as file:
        song_list = []
        data = file.readlines()
        for song in file:
            song = song.strip().split(";")
            dictionary = {
                "titel":song[0],
                "artiest":song[1],
                "aantal_keer_geluisterd":song[2],
                "aantal_keer_overgeslagen":song[3],
                "liked":song[4],
                "duur":song[5]
            }
            song_list.append(dictionary)
    return song_list


def compare_songs(chosen_song,dictionary_songs):
    chosen_song_score = chosen_song["duur"] * chosen_song["aantal_keer_geluisterd"] / chosen_song["aantal_keer_overgeslagen"]
    dictionary_songs =
    for song in dictionary_songs:
        if song["liked"]  == "ja" and chosen_song["liked"] == "ja":
            # Smells Like Teen Spirit;Nirvana;102;5;ja;251
        # Applejuice is nice;Draven;122;7;nee;250
        # Comcomer;Manea;105;5;ja;201
            print("both are liked")
        elif song["liked"] == "ja":
            print("joepie")
        #both are liked
        elif chosen_song_score