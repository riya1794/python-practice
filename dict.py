class Song(object):

	def __init__(myself,lyrics):
		myself.lyrics = lyrics

	def sing_to_me(myself):
		for line in myself.lyrics:
			print line

str = ["happy bday", "is it so", "u r lucky"]
hbd = Song(str)
hbd.sing_to_me()
