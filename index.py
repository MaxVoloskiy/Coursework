from gmusicapi import Mobileclient
from modules.Cardiovascular import Cardiovascular
from modules.Brain import Brain
from modules.Breath import Breath
from modules.HeartRate import HeartRate
from modules.Mental import Mental
from modules.Playlist import Playlist

def check_the_account(check):
    """
    Return boolean despite of the entered answer
    :param check: inputed checker
    :return: bool
    """

    if check.lower() == "n" or check.lower() == 'no':
        print("Please, firstly get the account on Google music")
        return None
    elif check.lower() == 'y' or check.lower() == 'yes':
        return False
    else:
        print("Incorrect symbol")
        return True


def login(email, password, api):
    '''
    Login to the Google Music
    :param email: inputed e-mail adress
    :param password: inputed password
    :param api: api interface
    :return bool: True if is authenticated, else False.
    '''
    api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
    return api.is_authenticated()



def choose_playlist(num, api):
    """
    Return the playlist of songs deapite of
    choosen illnesses
    :param num: Choosen number of illness
    :param api: API interface
    :return: playlist of songs
    """

    if num == 1:
        sweet_songs = Cardiovascular(api).generate_songs()
    elif num == 2:
        sweet_songs = Mental(api).generate_songs()
    elif num == 3:
        sweet_songs = HeartRate(api).generate_songs()
    elif num == 4:
        sweet_songs = Breath(api).generate_songs()
    elif num == 5:
        sweet_songs = Brain(api).generate_songs()
    else:
        sweet_songs = Playlist(50)
    return sweet_songs


def create_playlist(sweet_songs, api):
    """
    Create a playlist on Google Music
    :param sweet_songs: playlist of songs
    :param api: API interface
    """

    playlist_title = str(input('Enter the name of your illness: '))

    playlist_id = api.create_playlist(playlist_title)
    for song in sweet_songs:
        api.add_songs_to_playlist(playlist_id, song)


def main():
    """
    This function does the main action.
    Includes functions:
    - create_playlist
    - choose_playlist
    - login
    - check_the_account
    """

    api = Mobileclient()
    ch = True
    while ch:
        check = str(input("Do you have an account on Google music? (Y/N): "))
        ch = check_the_account(check)

    if ch == None:
        return False

    ch = False
    while ch == False:
        email = str(input("Enter your e-mail adress: "))
        password = str(input("Enter your password: "))
        if not login(email, password, api):
            print("Incorrect login or password")
        else:
            ch = True

    print("Choose your problem:")
    print("\t 1. Cardiovascular;\n\t 2. Mental;\n\t 3. Heart Rate;\n" +
          "\t 4. Breath;\n\t 5. Stimulation of the brain;\n")
    num = int(input('Choose the number: '))
    print("Waiting. Your playlist is generating...")
    sweet_songs = choose_playlist(num, api)

    create_playlist(sweet_songs, api)
    print("Waiting, your playlist is creating on Google Music...")
    print("Have a nice day! We will try to make your ears happy:)")

class Exeption_Google_account(Exception):
    pass

class Exeption_Incorrect_Symbol(Exception):
    pass

main()
