import re
from decimal import Decimal

import sys, os

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

full_regex = re.compile(r"^([A-Z][a-z]*\s[A-Z][A-Za-z]*)\sbatted\s(\d)\stimes\swith\s(\d)\shits")
def player_name(cur_line):
    match = full_regex.match(cur_line)
    if match is not None:
	    return match.group(1)
    else:
        return None
def player_at_bats(cur_line):
    match = full_regex.match(cur_line)
    if match is not None:
	    return match.group(2)
    else:
        return None
def player_hits(cur_line):
    match = full_regex.match(cur_line)
    if match is not None:
	    return match.group(3)
    else:
        return None


player_list =[]

class Player:
    def __init__(self, name, at_bats, hits):
        self.name = name
        self.at_bats = at_bats
        self.hits = hits
    def batting_average(self):
        return self.hits/self.at_bats



with open(filename) as f:
    for line in f:
        name_player = player_name(line)
        
        if name_player is not None:
            at_bats_player = float (player_at_bats(line))
            hits_player = float (player_hits(line))
            count = 1
            for x in player_list:
                if x.name == name_player:
                    x.at_bats = x.at_bats + at_bats_player
                    x.hits = x.hits + hits_player
                    count=0
                    break
            if count == 1:
                player_list.append( Player(name_player,at_bats_player,hits_player))
player_list.sort(reverse=True, key=Player.batting_average)
for x in player_list:
    a = Decimal(Player.batting_average(x))
    print(f"{x.name}: {round(a,3)}")
                