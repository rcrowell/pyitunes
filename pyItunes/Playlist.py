class Playlist:
    itunes_id = None
    name = None
    visible = None
    playlistPersistentId = None
    playlistId = None
    songs = None
    allItems = None   # not sure what this one means?

    def __init__(self):
        self.songs = []

    def __repr__(self):
        return '<Playlist("%s", %d songs)>' % (self.name, len(self.songs))
