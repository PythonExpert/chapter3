import random
import sys 
import urllib.request

SEED = 0
class User:
    sessionId = 0
    userId = 0
    likes = {}
    events = {}
    
    def __init__(self, userId, action, drama, comedy):
        self.sessionId = random.randint(0, 1000000)
        self.userId = userId
        self.likes = {'action': action, 'drama': drama, 'comedy': comedy} 
        self.events = { self.sessionId: []}

    def getSessionId(self):
         if (random.randint(0,100) > 90): 
             self.sessionId += 1 
             self.events[self.sessionId] = []
             
         return self.sessionId

    def selectGenre(self):
        return sample(self.likes)
        

def selectFilm(user):
    films = { 'action' : [145,2373,8241,23,459,1240,7787,63113,6534,57528,57640,63181,57951,61024,64508,58293,61350,61132,62999,64231], \
#6,9,10,15,20,21,23,42,44,66,70,71,76,89,95,98,110,112,139,145
              'drama'  : [25940,864,1805,5340,7456,48567,3621,297,5907,459,1508,5527,8397,4260,5471,5178,2227,8016,60758,60943], \
# 4,11,14,16,17,18,20,21,22,24,25,26,27,28,29,30,31,34,35,36], \
              'comedy' : [8241,32013,3884,864,61255,62718,62788,59258,60161,60126,60939,61250,62113,62586,58047,58490,57532,58315,58972,59118,] }
     #1,3,4,5,7,11,12,17,18,19,20,21,34,38,39,45,52,54,58,63] }
    genre = user.selectGenre()
    interestedFilms = films[genre]

    filmId = interestedFilms[random.randint(0,len(interestedFilms) - 1)]
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
    random.seed(SEED)
    number_of_events = 10000
        
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
    
    for x in range(0, number_of_events):
        randomuserid = random.randint(0, len(users) - 1)
        user = users[randomuserid]
        selectedFilm = selectFilm(user)
        action = selectAction(user)
        if (action == 'buy'):
            user.events[user.sessionId].append(selectedFilm)
    #       print("user id " + str(user.userId) + " selects film " + str(selectedFilm) + " and " + action)
        urllib.request.urlopen('http://moviegeek.com:8000/log/' + str(selectedFilm) \
                                 + '/' + action \
                                 + '?sessionid=' + str(user.getSessionId())\
                                 + '&userid='+ str(user.userId))
    print ("users\n")                             
    for u in users:
        print("user with id {} \n".format(u.userId))
        for key, value in u.events.items():
            if (len(value) > 0):
                print (" {}: {}".format(key, value))                                
main()


