import re
class XMLLibraryParser:
	def __init__(self,xmlLibrary):
		f = open(xmlLibrary)
		s = f.read()
		lines = s.split("\n")
		self.songs, self.playlists = self.parser(lines)
		
	def getValue(self,restOfLine):
		if restOfLine.strip() == '<true/>': return True
		if restOfLine.strip() == '<false/>': return False

		value = re.sub("<.*?>","",restOfLine)
		u = unicode(value,"utf-8")
		cleanValue = u.encode("ascii","xmlcharrefreplace")
		return cleanValue

	def keyAndRestOfLine(self,line):
		rawkey = re.search('<key>(.*?)</key>',line).group(0)
		key = re.sub("</*key>","",rawkey)
		restOfLine = re.sub("<key>.*?</key>","",line).strip()
		return key,restOfLine

	def parser(self,lines):
		dicts = 0
		songs = {}
		playlists = {}
		inSong = False
		inPlaylists = False
		inPlaylist = False
		inPlaylistTracks = False
		for line in lines:
			if '<key>Playlists</key>' == line.strip():
				inPlaylists = True
				playlist = {}
				continue

			if not inPlaylists:
				if re.search('<dict>',line):
					dicts += 1
				if re.search('</dict>',line):
					dicts -= 1
					inSong = False
					songs[songkey] = temp
				if dicts == 2 and re.search('<key>(.*?)</key>',line):
					rawkey = re.search('<key>(.*?)</key>',line).group(0)
					songkey = re.sub("</*key>","",rawkey)
					inSong = True
					temp = {}
				if dicts == 3  and re.search('<key>(.*?)</key>',line):
					key,restOfLine = self.keyAndRestOfLine(line)
					temp[key] = self.getValue(restOfLine)

			elif inPlaylists:
				if re.search('<key>(.*?)</key>',line):
					key,restOfLine = self.keyAndRestOfLine(line)
					if key == 'Name':
						if playlist: playlists[playlist['Playlist ID']] = playlist
						playlist = {}
					if key == 'Playlist Items':
						playlist[key] = []
					elif key == 'Track ID':
						playlist['Playlist Items'].append(self.getValue(restOfLine))
					else:
						playlist[key] = self.getValue(restOfLine)
						
		playlists[playlist['Playlist ID']] = playlist   # we always miss the last one; add it back here
		return songs, playlists
