import random
import requests
import json

# Pokemon roulette:
# Each player gets 6 random pokemon with their base stats
#Eavh pokemon gets 4 random moves with a limted amount of pp
#players battle with their team till exhaustion. End states: KO all emeny PK or 1 player exhausts all their pp
#the players will input using numbers to select options. (Attck, Switch. 1-6 pk)
#the program will track active pokemon for inputs and methods between 2 players. activepokemon.battle()
#
#the ai will attack randomly
#the moves will be objects used by pokemon

#TEAMS
Pokemon_Team = []
Enemy_Pokemon_Team = []

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10000") # gets a list of pokemon
move_req = requests.get("https://pokeapi.co/api/v2/move/") # gets a list of moves

data = pokemon_req.json()
movedata = move_req.json()

class Move():
    def __init__(self):
        random_move = random.choice(movedata["results"])
        move_response = requests.get(random_move["url"])
        move = move_response.json()
        self.name = move['name']

        self.power = move['power']
        #none target attacks (buffs) do not have accuracy values
        if not move['accuracy'] is None and move['power'] > 0:
            self.accuracy = int(move['accuracy'])
            self.target = 'target'
        else:
            self.accuracy = 0
            self.stat_change = move['stat_changes'][0]['stat']['name']
            self.target = 'self'

        self.pp = int(move['pp'])
        self.maxpp = int(move['pp'])
        self.damageclass = move['damage_class']['name']
        self.type = move['type']['name']

class Pokemon():

    move_list = []
    def __init__(self, pk):
        # initlaises pokemone obj
        self.name = pk['name']
        self.hp = pk['stats'][0]['base_stat']
        self.attack = pk['stats'][1]['base_stat']
        self.defense = pk['stats'][2]['base_stat']
        self.special_attack = pk['stats'][3]['base_stat']
        self.special_defense = pk['stats'][4]['base_stat']
        self.speed = pk['stats'][5]['base_stat']
        self.type = pk['types'][0]['type']['name']
        self.active = False
        self.move_list = self.GetMoves()

    def SelectMoves(self):
        while True:
            choice = input("Select a number [1,2,3,4]")
            if int(choice) in [1, 2, 3, 4]:
                return int(choice)

    def Attack(self, Enemy):
        self.DisplayMoves()
        move = self.move_list[self.SelectMoves()]
        if move.target == "target":
            if move.accuracy >= random.randint(1, 100):
                if move.damageclass == 'physical':
                    dmg = (move.power + (self.attack * random.randint(0,1)))
                    protection = (Enemy.defense * random.randint(0,1))
                    Enemy.hp = Enemy.hp -(dmg - protection)
                if move.damageclass == 'special':
                    dmg = (move.power + (self.special_attack * random.randint(0,1)))
                    protection = (Enemy.special_defense * random.randint(0,1))
                    Enemy.hp = Enemy.hp -(dmg - protection)
        #moves that are buffs
        else:
            if move.stat_change == 'defense':
                self.defense = self.defense + 20


    def DisplayMoves(self):
        counter = 0
        for i in self.move_list:
            print(str(counter) + ". " + i.name + "  ({}/{})".format(i.pp, i.maxpp))
    def TurnInput(self, Enemy):
        while True:
            choice = input("1. Attack \n2. Switch")
            if choice == 1:
                self.Attack(Enemy)

                # or choice == 2:
                # return choice
                #

    def GetMoves(self):
        temp_move_list = []
        for i in range(4):
            temp_move_list.append(Move())

        return temp_move_list



while len(Pokemon_Team) < 6:

    random_pokemon = random.choice(data['results'])
    response = requests.get(random_pokemon["url"])
    Enemy_random_pokemon = random.choice(data['results'])
    Enemy_response = requests.get(Enemy_random_pokemon["url"])

    pk = response.json()

    New_Pokemon = Pokemon(pk)
    Pokemon_Team.append(New_Pokemon)

    epk = Enemy_response.json()
    New_Pokemon = Pokemon(epk)
    Enemy_Pokemon_Team.append(New_Pokemon)

#checks for the active pokemon in the squad and returns it in the game loop at the start of each round
def CheckActive(pkt):
    for i in pkt:
        if i.active == True:
            return i
    else:
        return "Error"
## pokemon has been created, teams decked out
## game play loop:

Pokemon_Team[0].active = True
Enemy_Pokemon_Team[0].active = True



while True:
    round_counter = 0
    Player = CheckActive(Pokemon_Team)
    Enemy = CheckActive(Enemy_Pokemon_Team)
    print("It is round: " + str(round_counter) + "\n")
    print("Players 1 Pokemon " + Player.name + " on " + Player.hp + " and is fighting: " + Enemy.name + " on " + Enemy.hp + "\n")
    Player.TurnInput()

print(Pokemon_Team[0].name)
print(Enemy_Pokemon_Team[0].name)



    # hp = stat['name']
    # print(hp)
#print(list(data.keys())
# name = data['name']
# stat = data['stats']
# print(name)
# for stats in stat:
#     print(stats['stat']['name'], ':', stats['base_stat'])

