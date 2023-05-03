import random
import copy

TOP = 0
JG = 1
MID = 2
BOT = 3
SUP = 4


class Player:
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes
        self.lane = -1
    
    def get_note(self, lane):
        return self.notes[lane]

    def get_actual_note(self):
        return self.notes[self.lane]
    
    def reset(self):
        self.lane = -1


def modulo(num):
    if num < 0:
        num = -num
    return num

def get_possible_pairs(_players, lane, diff, restriction):
    possibilities = []

    if diff == 0:
        for p1 in _players:
            for p2 in _players:
                if p1 != p2 and p2.get_note(lane) + lane_tolerance >= p1.get_note(lane) >= p2.get_note(lane) - lane_tolerance :
                    possibilities.append([p1, p2])
    
    elif diff < 0:
        for p1 in _players:
            for p2 in _players:
                if p1 != p2 and p2.get_note(lane) + lane_tolerance >= p1.get_note(lane) >= p2.get_note(lane) - lane_tolerance and p1.get_note(lane) > p2.get_note(lane):
                    possibilities.append([p1, p2])

    elif diff > 0:
        for p1 in _players:
            for p2 in _players:
                if p1 != p2 and p2.get_note(lane) + lane_tolerance >= p1.get_note(lane) >= p2.get_note(lane) - lane_tolerance and p1.get_note(lane) < p2.get_note(lane):
                    possibilities.append([p1, p2])
    return possibilities

def create_teams(possible_pairs, _players, lane, diff, team, restriction):
    for pair in possible_pairs:
        actual_list = copy.copy(_players)

        for p in pair:
            actual_list.remove(p)
        team.append(pair)
        diff += pair[0].get_note(lane) - pair[1].get_note(lane)
        if lane == 4 and modulo(diff) <= tolerance:
            all_matches.append(copy.copy(team))
            diff -= pair[0].get_note(lane) - pair[1].get_note(lane)
            team.remove(pair)
        
        elif recursive_balance(lane+1, actual_list, diff, tolerance, lane_tolerance, team, restriction) == -1:
            diff -= pair[0].get_note(lane) - pair[1].get_note(lane)
            team.remove(pair)
        else:
            diff -= pair[0].get_note(lane) - pair[1].get_note(lane)
            team.remove(pair)


def recursive_balance(lane, _players, diff, tolerance, lane_tolerance, team = [], restriction = None):
    if restriction != None and lane == restriction[1]:
        actual_list = copy.copy(_players)
        pair = restriction[0]
        team.append(pair)
        diff += pair[0].get_note(lane) - pair[1].get_note(lane)
        if recursive_balance(lane+1, actual_list, diff, tolerance, lane_tolerance, team, restriction) == -1:
            diff -= pair[0].get_note(lane) - pair[1].get_note(lane)
            team.remove(pair)
        else:
            diff -= pair[0].get_note(lane) - pair[1].get_note(lane)
            team.remove(pair)
        return
    
    possible_pairs = get_possible_pairs(_players, lane, diff, restriction)
    
    create_teams(possible_pairs, _players, lane, diff, team, restriction)
        
    if len(possible_pairs) <= 0:
        return -1
    
    return 0

def get_matches(num):
    matches = []
    if num < len(all_matches):
        for x in range(0, num):
            match = random.choice(all_matches)
            all_matches.remove(match)
            matches.append(match)
    
        return matches
    elif len(all_matches) > 0:
        for x in range(0, len(all_matches)):
            match = random.choice(all_matches)
            all_matches.remove(match)
            matches.append(match)
        return matches
    else:
        print("Nenhuma partida encontrada!")

def show_matches(matches):
    if matches == None:
        return
    match_level = 0
    team1_level = 0
    team2_level = 0
    for x, match in enumerate(matches):
        
        print(f"Match {x+1}:")

        for y, pair in enumerate(match):

            if y == 0:
                print("TOP :", end=" ")
            if y == 1:
                print("JG :", end=" ")
            if y == 2:
                print("MID :", end=" ")
            if y == 3:
                print("BOT :", end=" ")
            if y == 4:
                print("SUP :", end=" ")

            team1_level += pair[0].get_note(y)
            team2_level += pair[1].get_note(y)
            for z, player in enumerate(pair):
                
                print(player.name, player.get_note(y), end=" ") 
                if z % 2 == 0 : 
                    print("x", end=" ")
            print()
        match_level = team1_level + team2_level
        print(f"Team1: {team1_level}")
        print(f"Team2: {team2_level}")
        print(f"Match: {match_level}")
        team1_level = 0
        team2_level = 0
        match_level = 0
        print()
    print(f"Total de partidas encontradas: {len(all_matches) + len(matches)}")
    
def show_players():
    for p in players:
        print(f"{p.name}")
        for y in range(0, 5):
            if y == 0:
                print("TOP:", p.get_note(y), end=" | ")
            if y == 1:
                print("JG:", p.get_note(y), end=" | ")
            if y == 2:
                print("MID:", p.get_note(y), end=" | ")
            if y == 3:
                print("BOT:", p.get_note(y), end=" | ")
            if y == 4:
                print("SUP:", p.get_note(y), end="  ")
        print()
        print()

ari = Player("Ari", [2, 6, 2, 2, 4])
bigode = Player("Bigode", [8, 7, 9, 7, 8])
cain = Player("Cain", [9, 10, 10, 10, 8])
carioca = Player("Carioca", [5, 6, 5, 6, 7])
caua = Player("Caua", [4, 6, 6, 4, 4])
coffler = Player("Coffler", [2, 2, 2, 3, 2])
dudu = Player("Dudu", [7, 10, 8, 10, 6])
danilo = Player("Danilo", [5, 6, 5, 3, 9])
grilha = Player("Grilha", [10, 8, 8, 6, 7])
luca = Player("Luca", [7, 2, 6, 8, 4])
lucas = Player("Lucas", [4, 4, 4, 8, 6])
lyra = Player("Lyra", [9, 8, 8, 4, 8])
zan = Player("Zan", [8, 7, 6, 10, 8])
nascido = Player("Nascido", [4, 4, 1, 2, 3])
reinaldo = Player("Reinaldo", [4, 6, 6, 6, 9])
reyner = Player("Reyner", [8, 9, 9, 8, 8])
talita = Player("Talita", [2, 2, 5, 4, 7])
valbin = Player("Valbin", [7, 9, 6, 8, 10])
vinicim = Player("Vinicim", [8, 7, 6, 10, 6])
xibiu = Player("Xibiu", [6, 4, 3, 2, 5])
isaque = Player("Isaque", [7, 10, 7, 7, 7])
limazin = Player("Limazin", [4, 6, 9, 7, 9])

all_matches = []

players = [

    ari,
    bigode,
    cain,
    carioca,
    caua,
    coffler,
    dudu,
    grilha,
    luca,
    lyra,
    zan,
    nascido,
    reinaldo,
    reyner,
    talita,
    valbin,
    vinicim,
    xibiu,
    isaque

]

game = [
    ari,
    limazin,
    xibiu,
    lyra,
    vinicim,
    nascido,
    grilha,
    cain,
    danilo,
    reinaldo
]

lane_tolerance = 1
tolerance = 0

restriction1 = [[cain, valbin], JG]
restriction2 = [[xibiu, nascido], BOT]

actual_restriction = None

if actual_restriction != None:
    for p in actual_restriction[0]:
        game.remove(p)

recursive_balance(0, game, 0, tolerance, lane_tolerance, restriction = actual_restriction)

selected_matches = get_matches(10)

show_matches(selected_matches)