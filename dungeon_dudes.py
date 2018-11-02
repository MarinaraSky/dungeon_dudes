from dd_Classes import *
from itertools import product
from random import choice

def main():

    name = input("Enter a player name: ")
    player = PlayableCharacter(name)
    print(player)


def get_room(player):
    colors = [ "Blue", "Red", "Yellow", "Green", "White", "Black",
            "Grey", "Purple"]
    locations = ["Room", "Beach", "Desert", "Forest", "Swamp", "Cave"]
    adjectives = ["Damp", "Dry", "Wet", "Arid", "Cold", "Hot"]
    room_fmt = "{} {} {}"
    cur_room = room_fmt.format(
            choice(adjectives), choice(colors), choice(locations))
    if cur_room not in player.rooms:
        player.rooms.add(cur_room)
        return cur_room


if __name__ == "__main__":
    main()
