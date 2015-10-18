import random
import sys 
import urllib.request

class User:
	sessionId = 0
	userId = 0
	likes = {}
	
	def __init__(self, userId, action, drama, comedy):
		self.sessionId = random.randint(0, 10000)
		self.userId = userId
		self.likes = {'action': action, 'drama': drama, 'comedy': comedy} 

	def getSessionId(self):
		if (random.randint(0,100) > 90): 
			self.sessionId += 1 
		return self.sessionId

	def selectGenre(self):
		return sample(self.likes)
		

def selectFilm(user):
	films = { 'action' : [6,9,10,15,20,21,23,42,44,66,70,71,76,89,95,98,110,112,139,145], \
			  'drama'  : [4,11,14,16,17,18,20,21,22,24,25,26,27,28,29,30,31,34,35,36], \
			  'comedy' : [1,3,4,5,7,11,12,17,18,19,20,21,34,38,39,45,52,54,58,63] }

	genre = user.selectGenre()
	interestedFilms = films[genre]

	filmId = interestedFilms[random.randint(0,19)]
	return filmId
def selectAction(user):
	actions = {'details': 70, 'moredetails': 20, 'buy': 10 }
	
	return sample(actions)

def sample(dictionary):
		randomNumber = random.randint(0,100)
		index = 0
		for key, value in dictionary.items():
			#print("selecting genre, key is "  + key + " random number is" + str(randomNumber) + " likes " + str(self.likes))
			index += value

			if (randomNumber <= index):
				return key

def main():     
	
	print("Generating Data");
	users = [
			User(1, 20, 30, 50),
			User(2, 50, 20, 40),
			User(3, 20, 30, 50),
			User(4, 100, 0, 0),
			User(5, 0, 100, 0),
			User(6, 0, 0, 100),
			]
	print ("Simulating " + str(len(users)) + " visitors")
	
	for x in range(0, 1000):
		randomuserid = random.randint(0, len(users) - 1)
		user = users[randomuserid]
		selectedFilm = selectFilm(user)
		action = selectAction(user)
		print("user id " + str(user.userId) + " selects film " + str(selectedFilm) + " and " + action)
		urllib.request.urlopen('http://moviegeek.com:8000/log/' + str(selectedFilm) \
							 	+ '/' + action \
							 	+ '?sessionid=' + str(user.getSessionId())\
		 						+ '&userid='+ str(user.userId))
	#callMovieGeekLogger();	
main()


