from pip._vendor import requests as r

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
                if all_players[i]['team'] == 'self.name':
                    self.roster.append(all_players[i])


av = Club('Aston Villa')

av.form_club

#print(av.name)
#print(av.roster)