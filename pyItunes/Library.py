from pyItunes.Song import Song
from pyItunes.Playlist import Playlist
import time
class Library:
	def __init__(self,songs,playlists):
		self.songs = self.parseSongs(songs)
		self.playlists = self.parsePlaylists(playlists,songs)

	def parseSongs(self,dictionary):
		songs = []
		format = "%Y-%m-%dT%H:%M:%SZ"
		for song,attributes in dictionary.iteritems():
			s = Song()
			s.name = attributes.get('Name')
			s.artist = attributes.get('Artist')
			s.album_artist = attributes.get('Album Aritst')
			s.composer = attributes.get('Composer')
			s.album = attributes.get('Album')
			s.genre = attributes.get('Genre')
			s.kind = attributes.get('Kind')
			if attributes.get('Size'):
				s.size = int(attributes.get('Size'))
			s.total_time = attributes.get('Total Time')
			s.track_number = attributes.get('Track Number')
			if attributes.get('Year'):
				s.year = int(attributes.get('Year'))
			if attributes.get('Date Modified'):
				s.date_modified = time.strptime(attributes.get('Date Modified'),format)
			if attributes.get('Date Added'):
				s.date_added = time.strptime(attributes.get('Date Added'),format)
			if attributes.get('Bit Rate'):
				s.bit_rate = int(attributes.get('Bit Rate'))
			if attributes.get('Sample Rate'):
				s.sample_rate = int(attributes.get('Sample Rate'))
			s.comments = attributes.get("Comments	")
			if attributes.get('Rating'):
				s.rating = int(attributes.get('Rating'))
			if attributes.get('Play Count'):
				s.play_count = int(attributes.get('Play Count'))
			if attributes.get('Location'):
				s.location = attributes.get('Location')			
			songs.append(s)
		return songs

	def parsePlaylists(self,dictionary,songs):
		playlists = []
		for playlist,attributes in dictionary.iteritems():
			p = Playlist()
			p.name = attributes.get('Name')
			p.visible = attributes.get('Visible')
			p.allItems = attributes.get('All Items')
			p.playlistPersistentId = attributes.get('Playlist Persistent Id')
			p.playlistId = attributes.get('Playlist Id')

			for songId in attributes.get('Playlist Items',[]):
				p.songs.append(songs[songId])

			playlists.append(p)

		return playlists
