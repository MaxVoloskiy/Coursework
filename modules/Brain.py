import random
from modules.Playlist import Playlist

class Brain():
    '''
    Class that generate the playlist of songs against
    mental and internal illnesses.
    '''

    classical_list = ['mozart', 'beathoven', 'chopin', 'einaudi', 'bach', 'vivaldi', 'handel',
                      'chaikovskiy', 'paganini']
    sweet_songs = Playlist(50)

    def __init__(self, logged_api):
        """
        :param logged_api: logged api
        """
        self.api = logged_api

    def generate_songs(self):
        """
        Return playlist of songs

        :return: playlist of songs
        """
        for item in range(50):
            search = random.choice(self.classical_list)
            self.sweet_songs[item] = (random.choice(self.api.search(search)['song_hits'])['track']['storeId'])

        return self.sweet_songs
