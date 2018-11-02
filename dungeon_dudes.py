#! /usr/bin/env python3

from dd_Classes import *
from random import choice, randint
import sys


def main():
    '''Main of dungeon_dudes'''
    if "-d" in sys.argv:
        print_roll = True
    else:
        print_roll = False
    adventure(print_roll)


def adventure(print_roll):
    '''Main adventure function. Will loop until all enemies have been
    defeated or until the player dies.'''
    menu = "\n0) Fight\n1) My Health\n2) Enemy Health\n" \
            "3) Next Room\n4) View Loot Bag\n9) Quit"
    bye = "\nGood Bye"
    clear_screen = "\033c"

    print(clear_screen)
    try:
        name = input("Enter a player name: ")
    except (EOFError, KeyboardInterrupt):
        print(bye)
        return
    player = PlayableCharacter(name)
    print(clear_screen)
    while player.health != 0 and EnemyCharacter.enemy_list:
        cur_room = get_room(player)
        room_prompt = "You've entered a {}".format(cur_room)
        print(room_prompt)
        room_enemies = generate_enemies()
        player.initiative = player.roll_dice(1)[0]
        for enemy in room_enemies:
            enemy_prompt = "A {} {} is standing before you."
            print(enemy_prompt.format(enemy.enemy_size[enemy.dice - 1], enemy.name))
            while enemy.health != 0 and player.health != 0:
                print(menu)
                if "Potion" in player.loot:
                    print("\nD) Drink Potion")
                try:
                    selection = input("Selection: ")
                    print(clear_screen)
                except (EOFError, KeyboardInterrupt):
                    print(bye)
                    return
                if selection == "0":
                    player.rumble(enemy, print_roll)
                    if player.dice == 4:
                        player.dice -= 1
                    print(player)
                    print(enemy)
                elif selection.upper() == "D":
                    player.dice += 1
                    player.loot.remove("Potion")
                elif selection == "1":
                    print(player)
                elif selection == "2":
                    print(enemy)
                elif selection == "3":
                    print("Cannot continue until all enemies defeated.")
                elif selection == "4":
                    if len(player.loot) == 0:
                        print("No loot.")
                    else:
                        for loot in player.loot:
                            print(loot)
                elif selection == "9":
                    print(bye)
                    return
            if enemy.health == 0:
                victory = "You have defeated {}."
                print(victory.format(enemy.name))
                player.defeated.append(enemy)
                loot = enemy.drop_loot()
                if loot is not None:
                    loot_fmt = "Do you want to pick up {} (ENTER for NO)\n"
                    try:
                        if input(loot_fmt.format(loot)):
                            EnemyCharacter.loot.remove(loot)
                            player.loot.add(loot)
                    except (EOFError, KeyboardInterrupt):
                        print(bye)
                else:
                    print("No loot dropped.")
        input("Anything to continue")
        print(clear_screen)

    print("\033[4mEnemies who lost their lives\033[0m")
    player.defeated.sort(key=lambda defeated: defeated.name)
    for enemy in player.defeated:
        print(enemy.name)
    print("\n\033[4mLoot Carried\033[0m")
    for piece in player.loot:
        print(piece)
    print("\n\033[4mYour Encountered Environments\033[0m")
    for room in player.rooms:
        print(room)


def get_room(player):
    '''Generates the room for the player and enemies to be in'''
    colors = ["Blue", "Red", "Yellow", "Green", "White", "Black",
              "Grey", "Purple"]
    locations = ["Room", "Beach", "Desert", "Forest", "Swamp", "Cave", "Jungle"]
    adjectives = ["Damp", "Dry", "Wet", "Arid", "Cold", "Hot"]
    room_fmt = "{} {} {}"
    cur_room = room_fmt.format(
            choice(adjectives), choice(colors), choice(locations))
    if cur_room not in player.rooms:
        player.rooms.add(cur_room)
        return cur_room
    else:
        get_room(player)


def generate_enemies():
    '''Generates 1-3 enemies for player to fight'''
    enemy_list = list()
    enemy_count = randint(1, 3)
    for count in range(0, enemy_count):
        new_challenger = EnemyCharacter()
        new_challenger.initiative = new_challenger.roll_dice(1)[0]
        enemy_list.append(new_challenger)
    return enemy_list


if __name__ == "__main__":
    main()
