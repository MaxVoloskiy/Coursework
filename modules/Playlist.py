import ctypes

class Playlist:
    """
    Implements the Playlist ADT using array capabilities of the ctypes module.
    """
    def __init__(self, size):
        """
        Creates a playlist with size elements.

        :param size: size of playlist.
        """
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

    def __len__(self):
        """
        Returns the size of the playlist.

        :return: the size of the playlist.
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the song.

        :param index: the index of element.
        :return: value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the playlist element at index position.

        :param index: the index element.
        :param value: the value of element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the playlist by setting each element to the given value.

        :param value: the value of element.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the playlist's iterator for traversing the elements.

        :return: the playlist's iterator for traversing the elements.
        """
        return _PlaylistIterator(self._elements)

    #def sort_by_time(self):
    #def sort_by_alphabet(self):
    #def shuffle_playlist(self):

class _PlaylistIterator:
    """
    An iterator for the Playlist ADT.
    """
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration
