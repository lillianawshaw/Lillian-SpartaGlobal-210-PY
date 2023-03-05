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
Special_Moves = ['fillet-away']

Weakness_dict = {
                'grass' : ['fire', 'ice', 'poison', 'flying', 'bug'],
                 'normal' : ['fighting'],
                'fire' : ['water', 'ground', 'rock'],
                'water' : ['electric', 'grass'],
                'electric' : ['ground'],
                'ice' : ['fire', 'fighting', 'rock', 'steel'],
                'fighting' : ['flying', 'psychic', 'fairy'],
                'poison' : ['ground', 'psychic'],
                'ground' : ['water', 'grass', 'ice'],
                'flying' : ['electric', 'ice', 'rock'],
                'psychic' : ['bug', 'ghost', 'dark'],
                'bug' : ['fire', 'flying', 'rock'],
                'rock' : ['water', 'grass', 'fighting', 'ground', 'steel'],
                'ghost' : ['ghost', 'dark'],
                'dragon' : ['ice', 'dragon', 'fairy'],
                'dark' : ['fighting', 'bug', 'fairy'],
                'steel' : ['fire', 'fighting', 'ground'],
                'fairy' : ['poison', 'steel']
                 }

Resists_dict = {
                'grass' : ['water', 'electric', 'grass', 'ground', 'bug'],
                'normal' : [],
                'fire' : ['fire', 'grass', 'ice', 'bug', 'steel', 'fairy'],
                'water' : ['fire', 'water', 'ice', 'steel'],
                'electric' : ['electric', 'flying', 'steel'],
                'ice' : ['ice'],
                'fighting' : ['bug', 'rock', 'dark'],
                'poison' : ['grass', 'fighting', 'poison', 'bug', 'fairy'],
                'ground' : ['poison', 'rock'],
                'flying' : ['grass', 'fighting', 'bug'],
                'psychic' : ['fighting', 'psychic'],
                'bug' : ['grass', 'fighting', 'ground'],
                'rock' : ['normal', 'fire', 'poison', 'flying'],
                'ghost' : ['poison', 'bug'],
                'dragon' : ['fire', 'water', 'electric', 'grass'],
                'dark' : ['dark', 'ghost'],
                'steel' : ['normal', 'grass', 'ice', 'flying', 'psychic', 'bug', 'rock', 'dragon', 'steel', 'fairy'],
                'fairy' : ['fighting', 'bug', 'dark']
                 }

Negate_dict = {
                'grass' : [],
                 'normal' : ['ghost'],
                'fire' : [],
                'water' : [],
                'electric' : [],
                'ice' : [],
                'fighting' : [],
                'poison' : [],
                'ground' : ['electric'],
                'flying' : ['ground'],
                'psychic' : [],
                'bug' : [],
                'rock' : [],
                'ghost' : ['normal', 'fighting'],
                'dragon' : [],
                'dark' : ['psychic'],
                'steel' : ['poison'],
                'fairy' : ['dragon']
                 }



pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1200") # gets a list of pokemon
move_req = requests.get("https://pokeapi.co/api/v2/move/?limit=918")# gets a list of moves

data = pokemon_req.json()
movedata = move_req.json()

class Move():
    def __init__(self):
        random_move = random.choice(movedata["results"])
        move_response = requests.get(random_move["url"])
        move = move_response.json()
        self.name = move['name']
        self.target = 'special'
        self.power = move['power']
        if move['accuracy'] != None:
            self.accuracy = move['accuracy']
        else:
            self.accuracy = 0
        self.accuracy = 0
        if self.power == None:
            self.power = 0
        #none target attacks (buffs) do not have accuracy values
        try:
            #print(move['stat_changes'])
            #unmissable move with power
            if move['accuracy'] == 'null' and self.power != 0:
                self.accuracy = 100
                self.target = 'target'
                #print("Succes")

            if not move['accuracy'] is None:
                self.accuracy = int(move['accuracy'])
                self.target = 'target'
                #print("Succes")

            if move['name'] == 'shelter':
                self.accuracy = 0
                self.power = 0
                self.pp = 15
                self.type = 'normal'
                self.damageclass = 'status'
                self.stat_change = 'defense'

            if move['name'] == 'after-you':
                self.accuracy = 0
                self.power = 0
                self.pp = 15
                self.type = 'normal'
                self.damageclass = 'status'
                self.stat_change = 'speed'


            if move['damage_class']['name'] == 'status' and move['accuracy'] is None:
                # print(move['name'])
                # print(move['stat_changes'])
                # print(move['stat_changes'][0])
                if move['stat_changes'] != []:
                    self.accuracy = 0
                    self.stat_change = move['stat_changes'][0]['stat']['name']
                    self.target = 'self'
                else:
                    self.accuracy = 0
                    self.stat_change = 'splash'
                    self.target = 'self'

            elif move['damage_class']['name'] == 'status' and int(move['accuracy']) > 0:
                self.accuracy = int(move['accuracy'])
                self.stat_change = 'evasion'
                self.target = 'self'

        except:
            print("MISTAKE: " + self.name + " : " + str(self.power) + " : " + str(move['accuracy']) + " " + move['target']['name'])
            input(" ")
            self.accuracy = 50
            self.stat_change = 'defense'
            self.target = 'target'
        if move['pp'] is None:
            self.pp = 5
            self.maxpp = 5
        else:
            self.pp = int(move['pp'])
            self.maxpp = int(move['pp'])

        self.damageclass = move['damage_class']['name']
        self.type = move['type']['name']
        if self.power is None:
            self.power = 45

class Pokemon():

    move_list = []
    def __init__(self, pk):
        # initlaises pokemone obj
        self.name = pk['name']
        self.hp = pk['stats'][0]['base_stat']
        self.maxhp = self.hp
        self.attack = pk['stats'][1]['base_stat']
        self.defense = pk['stats'][2]['base_stat']
        self.special_attack = pk['stats'][3]['base_stat']
        self.special_defense = pk['stats'][4]['base_stat']
        self.speed = pk['stats'][5]['base_stat']
        self.type = pk['types'][0]['type']['name']
        self.active = False
        self.KO = False
        self.move_list = self.GetMoves()
        self.Dangerous_Terrain = False



    def CompareTypes(self, Movetype, EnemyType):

        if Weakness_dict[EnemyType].count(Movetype) > 0:
            print("Super Effective move against " + EnemyType + "\n")
            print("2")
            return 2
        if Resists_dict[EnemyType].count(Movetype) > 0:
            print("Not Effective move against " + EnemyType + "\n")
            return 0.5
        if Negate_dict[EnemyType].count(Movetype) > 0:
            print("This move is negated by " + EnemyType + "\n")
            return 0
        print("Normal dmg")
        return 1

    def SelectMoves(self):
        while True:
            choice = input("Select a number [0,1,2,3] \n ")
            if int(choice) in [0, 1, 2, 3]:
                return int(choice)



    def Attack(self, Enemy):
        self.DisplayMoves()
        move = self.move_list[self.SelectMoves()]
        
        #Special move that deletes 50% of your enemy health
        if move.target == 'special':

            if move.name == 'lock-on':
                buff = self.move_list[random.randint(0, 3)]
                print(buff.name + " can't miss!")
                buff.accuracy = 100

            if move.name == 'stealth-rock' or move.name == 'spikes':
                Enemy.Dangerous_Terrain = True
            ##"Spreads sharp rocks around the opposing field, "
            ##"damaging any Pokémon that enters the field for 1/8 its max HP. "
            ##"This damage is affected by the entering Pokémon's susceptibility to rock moves. rapid "
            ##"spin removes this effect from its user's side of the field."

                print("Sharp rocks spread around the opposing field, damaging any Pokémon that enters the field for 1/8 its max HP. \n" )

            if move.name == 'fillet-away':
                print("Fillet Away carves 50% off " + Enemy.name + " hp\n")
                if Enemy.hp % 2 == 0:
                    Enemy.hp = Enemy.hp / 2
                else:
                    Enemy.ho = (Enemy.hp + 1) / 2


        
        if move.target == "target":
            print(self.name + " attacks with: " + move.name + "\n")
            if move.accuracy >= random.randint(1, 100):
                if move.damageclass == 'physical':
                    dmg = (move.power + (self.attack * random.randint(0, 1)))
                    protection = (Enemy.defense * random.randint(0, 1))
                    total = dmg - protection
                    total = total * self.CompareTypes(move.type, Enemy.type)
                    if total < 0:
                        #stops accidental healing if dmg is lower than protect
                        total = 0
                    Enemy.hp = Enemy.hp - (dmg - protection)
                    print(self.name + " did " + str(total) + " points of dmg\n")
                    move.pp = move.pp - 1
                if move.damageclass == 'special':
                    dmg = (move.power + (self.special_attack * random.randint(0, 1)))
                    protection = (Enemy.special_defense * random.randint(0, 1))
                    total = dmg - protection
                    total = total * self.CompareTypes(move.type, Enemy.type)
                    if total < 0:
                        #stops accidental healing if dmg is lower than protect
                        total = 0
                    print(self.name + " did " + str(total) + " points of dmg\n")
                    Enemy.hp = Enemy.hp - (dmg - protection)
                    move.pp = move.pp - 1
            else:
                print("The move misses...\n")

        #moves that are buffs
        if move.target == 'self':
            move.pp = move.pp - 1
            if move.stat_change == 'attack':
                self.attack = self.attack + 20

                print("Attack has been raised to: " + str(self.attack))
            if move.stat_change == 'defense' or move.stat_change == 'evasion':
                self.defense = self.defense + 20
                print("Defense has been raised to: " + str(self.defense))
            if move.stat_change == 'speed':
                self.speed = self.speed + 20
                print("Speed has been raised to: " + str(self.speed) )

            if move.stat_change == 'special_defense':
                self.special_defense = self.special_defense + 20
                print("Special Defense has been raised to: " + str(self.special_defense))

            if move.stat_change == 'special_attack':
                self.special_attack = self.special_attack + 20
                print("Special Attack has been raised to: " + str(self.special_attack))


    def Switch(self, pkt):
        counter = 0
        for i in pkt:
            print(str(counter) + ". " + i.name + "  ({}/{})".format(i.hp, i.maxhp))
            counter = counter + 1
        while True:
            self.active = False
            choice = self.SelectPK()
            if pkt[int(choice)].KO == False:
                pkt[int(choice)].active = True

                print(pkt[int(choice)].name + " is now active")
                for i in pkt:
                    if i.Dangerous_Terrain == True:
                        print("Dangerous Terrian: You take an 1/8th of mxh hp in damage")
                        pkt[int(choice)].hp = round((pkt[int(choice)].hp / 8))
                break


    def SelectPK(self):
        while True:
            choice = input("Select your pokemon [0,1,2,3,4,5] \n")
            return choice


    def DisplayMoves(self):
        counter = 0
        for i in self.move_list:
            print(str(counter) + ". " + i.name + "  ({}/{})".format(i.pp, i.maxpp))
            counter = counter + 1

    def TurnInput(self, Enemy, pkt):

        while True:
            choice = input("1. Attack \n2. Switch \n ")
            if int(choice) == 1:
                self.Attack(Enemy)
                break
            if int(choice) == 2:
                self.Switch(pkt)
                break
                # or choice == 2:
                # return choice
                #

    def GetMoves(self):
        temp_move_list = []
        for i in range(4):
            temp_move_list.append(Move())

        return temp_move_list

    def CheckAlive(self):
        if self.hp >= 0:
            return True
        else:
            return False

    def AllDeadDave(self, pkt):
        #checks to see if team is KO
        for i in pkt:
            if i.KO == False:
                return False
        else:
            return True



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
        if i.active is True:
            return i
    else:
        return "Error"



## pokemon has been created, teams decked out
## game play loop:

round_counter = 0
print("Welcome to Pokemon")
Pokemon_Team[0].active = True
Enemy_Pokemon_Team[0].active = True
while True:
    turn_counter = 0

    Player = CheckActive(Pokemon_Team)

    Enemy = CheckActive(Enemy_Pokemon_Team)


    if Player.AllDeadDave(Pokemon_Team) or round_counter > 50:
        #should be unreachable code but nice catch to prevent loops
        print("Player 1 team is KO \n You white out...")
        break
    if Enemy.AllDeadDave(Enemy_Pokemon_Team):
        print("Player 2 team is KO \n You white out...")
        break

    print("It is round: " + str(round_counter) + "\n")
    print("Players 1 Pokemon " + Player.name + " on " + str(Player.hp) + "hp and is fighting: " + Enemy.name + " on " + str(Enemy.hp) + "hp \n")

    if Player.speed >= Enemy.speed:
        print(Player.name + " is faster so goes first")
        Player.TurnInput(Enemy, Pokemon_Team)

        if Enemy.CheckAlive() == False:
            print(Enemy.name + " Is KO")
            Enemy.KO = True
            Enemy.hp = 0
            if Enemy.AllDeadDave(Enemy_Pokemon_Team) is False:
                Enemy.Switch(Enemy_Pokemon_Team)
                Enemy = CheckActive(Enemy_Pokemon_Team)
                print()
            else:
                print("Enemy team is deafted, you win")
                break
        print("Next players turn \n")
        print("Players 2 Pokemon " + Enemy.name + " on " + str(
            Enemy.hp) + "hp and is fighting: " + Player.name + " on " + str(Player.hp) + "hp \n")

        Enemy.TurnInput(Player, Enemy_Pokemon_Team)
        if Player.CheckAlive() == False:
            print(Player.name + " Is KO")
            Player.KO = True
            Player.hp = 0
            if Player.AllDeadDave(Pokemon_Team) is False:
                Player.Switch(Pokemon_Team)
                Player = CheckActive(Pokemon_Team)
            else:
                print("Enemy team is deafted, you win")
                break
    else:
        print(Enemy.name + " is faster so goes first")
        print("Players 2 Pokemon " + Enemy.name + " on " + str(
            Enemy.hp) + "hp and is fighting: " + Player.name + " on " + str(Player.hp) + "hp \n")

        Enemy.TurnInput(Player, Enemy_Pokemon_Team)
        if Player.CheckAlive() == False:
            print(Player.name + " Is KO")
            Player.KO = True
            Player.hp = 0
            if Player.AllDeadDave(Pokemon_Team) is False:
                Player.Switch(Pokemon_Team)
                Player = CheckActive(Pokemon_Team)
            else:
                print("Enemy team is deafted, you win")
                break
        print("Next players turn \n")
        print("Players 1 Pokemon " + Player.name + " on " + str(
            Player.hp) + "hp and is fighting: " + Enemy.name + " on " + str(Enemy.hp) + "hp \n")

        Player.TurnInput(Enemy, Pokemon_Team)
        if Enemy.CheckAlive() == False:
            print(Enemy.name + " Is KO")
            Enemy.KO = True
            Enemy.hp = 0
            if Enemy.AllDeadDave(Enemy_Pokemon_Team) is False:
                Enemy.Switch(Enemy_Pokemon_Team)
                Enemy = CheckActive(Enemy_Pokemon_Team)
            else:
                print("Enemy team is deafted, you win")
                break
    round_counter = round_counter + 1

input("Game over!")



    # hp = stat['name']
    # print(hp)
#print(list(data.keys())
# name = data['name']
# stat = data['stats']
# print(name)
# for stats in stat:
#     print(stats['stat']['name'], ':', stats['base_stat'])

