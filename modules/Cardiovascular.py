import random
from modules.Playlist import Playlist

class Cardiovascular():
    '''
    Class that generate the playlist of songs against
    cardiovascular illnesses.
    '''
    acoustic_list = ['acoustic guitar', 'violin', 'cello', 'banjo', 'harp', 'kobza', 'ukulele']
    sweet_songs = Playlist(50)

    def __init__(self, logged_api):
        """
        :param logged_api: loogged api
        """
        self.api = logged_api

    def generate_songs(self):
        """
        Return playlist of songs

        :return: playlist of songs
        """
        for item in range(50):
            search = random.choice(self.acoustic_list)
            self.sweet_songs[item] = random.choice(self.api.search(search)['song_hits'])['track']['storeId']

        return self.sweet_songs
