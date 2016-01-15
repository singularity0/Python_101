import os
from random import randint
from tabulate import tabulate
import json
from mutagen.mp3 import MP3
import mutagen

class Song:
	def __init__(self, title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44"):
		self.title = title
		self.artist = artist
		self.album = album
		self.length = length

		self.legth_in_secs = self.legth_in_secs()

	def legth_in_secs(self):
		total = 0
		total += 100 #int(self.length[:2])*60*60 #add secs
		total += 10  #int(self.length[-5:-3])*60 #add mins
		total += 1   #int(self.length[:2]) #add hours
		return total

	def __str__(self):
		return "{0} - {1} from {2} - {3}".format(self.artist, self.title, self.album, self.length)

	def __eq__(self, other):
		if self.title == other.title and self.artist == other.artists:
			return True
		else:
			return False

	def __hash__(self):
		return 123

	def lengths(self, minutes=False, seconds=False, hours=False):
		total_length = 0
		if hours:
			return self.length[:2]
		elif minutes:
			return self.length[-5:-3]
		elif seconds:
			return self.length[-2:]


class Playlist:
	def __init__(self, name="Code", repeat=False, shuffle=False):
		self.name = name
		self.repeat = repeat
		self.shuffle = shuffle

		self.content = 	[]
		self.current_song = None

	def add_song(self, song):
		self.content.append(song)
		# self.content[song.title] = [song.artist, song.album, song.length]

	def remove_song(self, song):
		self.content.remove(song)

	def add_songs(self, songs):
		for item in songs:
			self.add_song(item)

	def total_length(self):
		total_l = 0
		for item in self.content:
			total_l += item.legth_in_secs
		return total_l

	def artists(self):
		artist = {}
		for item in self.content:
			if item in artist:
				artist[item] += 1
			else: 
				artist[item] = 1
		for item in artist:
			print(item.artist),
			print(artist[item])

	def curren_song(self):
		if self.current_song == None:
			current_song = input("select a number in our playlist - >  ")
			self.current_song = int(current_song)
			
		return self.current_song

	def next_song(self):
		current_song  = self.curren_song()
		# self.current_song = self.curren_song()

		# print(self.current_song)
		remaining_songs = self.content[self.current_song+1:]

		if current_song == len(self.content)-1 and self.repeat == False:
			return "no next song"

		if self.repeat is False and self.shuffle is False:
			self.current_song = current_song + 1
			return self.content[current_song + 1]

		if current_song == len(self.content)-1 and self.repeat == True and self.shuffle == False:
			self.current_song = 0
			return self.content[0]

		if self.repeat is True and self.shuffle is True:
			self.current_song = randint(0, len(self.content))
			return self.content[self.current_song]

		if self.repeat is True and self.shuffle is False:
			# if self.current_song < len(self.content)-1:
			pass	

		if self.repeat is False and self.shuffle is True:
			rand_selection = randint(0, len(remaining_songs)-1)
			self.current_song = rand_selection
			return self.content[rand_selection]



	def print_content(self):
		for i in range(0, len(self.content)):
			print (self.content[i])

	def pprint_playlist(self):
		table = []
		for i in range(0, (len(self.content))):
			table.append([self.content[i].artist, self.content[i].title, self.content[i].length])
		headers = ['Artist', 'Title', 'Length of song']
		print(tabulate(table, headers, tablefmt='orgtbl'))

	def save(self):
		d = {}
		if ' ' in self.name:
			self.name = self.name.replace(" ", "-")
		d[self.name] = []
		for i in range(0, len(self.content)):
			d[self.name].append(str(self.content[i]))
		f = open("playlist_output.json", "w")
		json.dump(d, f)
		print(d)

	@staticmethod
	def load():
		f = open("playlist_input.json", "r")
		data = json.load(f)
		for k, v in data.items():
			playlist_name = k
			playlist_songs = v
		playlist = Playlist(name=playlist_name)
		# print(playlist_songs)


class MusicCrawler:
	def __init__(self, path):
		self.path = path

	def get_info(self, data):
		song_data = {}
		try:
			song_data["artist"] = data["TPE1"].text[0]
		except:
			song_data["artist"] = "Unknown Artist"
		try:
			song_data["album"] = data["TALB"].text[0]
		except:
			song_data["album"] = "Unknown Album"
		try:
			song_data["title"] = data["TIT2"].text[0]
		except:
			song_data["title"] = "Unknown Title"
		try:
			song_data["length"] = str(datetime.timedelta(seconds=data.info.length//1))[2:]
		except:
			song_data["length"] = "Unknown"
		return song_data

	def generate_playlist(self):
		play_list = Playlist()
		tracks = [mp3 for mp3 in os.listdir(self.path) if mp3.endswith(".mp3")]

		for track in tracks:
			data = mutagen.File(self.path + "/" + track)
			info = self.get_info(data)
			new_song = Song(artist=info["artist"], title=info["title"], album=info["album"], length=info["length"])
			play_list.add_song(new_song)
			
		return play_list
		

some_song = Song(length="22:32:44")
other_song = Song(title='tttttitle', album='allBUM', artist='Man', length="01:32:32")
print(other_song.legth_in_secs)
li = [some_song, other_song]
some_playlist = Playlist(name='s wmw t')
print(some_song.legth_in_secs)
# some_playlist.add_song(some_song)
print(some_playlist.content)
# some_playlist.remove_song(some_song)
some_playlist.add_songs(li)
# print(some_playlist.content)
print(some_playlist.total_length())
# print(some_playlist.current_song())

# print(some_playlist.next_song())
print(some_playlist.pprint_playlist())

Playlist.load()

crawler = MusicCrawler("/home/mihail/Music/CD1")
print(crawler.generate_playlist().name)
