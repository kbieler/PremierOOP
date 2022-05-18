#class for teams/club
#class for players
#another class for filling lineup?/running eligibility, position & possible formations

#sort by team/club
#filter out injured and/or suspended
#sort by position
#check possible formations

from pip._vendor import requests as r

#data = r.get(f'https://foxes90-prempundit.herokuapp.com/players')
#if data.status_code == 200:
    #data = data.json()
    #for i in range(len(data['Players'])):
        #print(data['Players'][i]['team'])


data = r.get(f'https://foxes90-prempundit.herokuapp.com/players')
if data.status_code == 200:
    data = data.json()
    liverbirds = []
    for i in range(len(data['Players'])):
        if data['Players'][i]['team'] == 'Liverpool':
            liverbirds.append(data['Players'][i])
    print(liverbirds)
            


class Player:
    def __init__(self, d):
        self.first = d['first_name']
        self.last = d['last_name']
        self.position = d['position']
        self.team = d['team']
        
        if d['injured'] or d['suspended'] == 'True':
            self.eligible = False
        else:
            self.eligible = True


virgil = Player(liverbirds[0])
print (virgil.position)
print(virgil.eligible)


class Club:
    def __init__(self, name):
        self.name = name
        self.roster = []

    def form_club(self):
        all_players = r.get(f'https://foxes90-prempundit.herokuapp.com/players')
        if all_players.status_code == 200:
            all_players = all_players.json() 
            all_players = all_players['Players']
            for i in range(len(all_players)):
                if all_players[i]['team'] == self.name:
                    self.roster.append(all_players[i])
            
    #dict of eligible players by position 



class Starters:
    def __init__(self, team):
        self.team = team

    #function to fill formation with eligible players by position
    #Keeper == 1
    #Defender >= 3, <= 5
    #Midfielder >= 3, <= 5
    #Striker >= 1, <=3
    #All_Starters == 11
    #(else: None)


#Example output (NOT THE CORRECT ANSWER):
#{Teams: {
     #'Manchester City' :  '1-4-5-1',
     #'Swansea Swans': None,
    # 'Nottingham Forest Tricky Trees': '1-4-3-3',
    # 'Stoke City Potters': '1-3-5-2'
#}}
