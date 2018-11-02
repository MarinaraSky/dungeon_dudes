from random import choice, randint, randrange


class Character:

    def __init__(self, name):
        self.name = name
        self.health = 0
        self.initiative = 0
        self.location = 0

    def __str__(self):
        fmt = "Name: {0} Health: {1} Initiative: {2}"
        return fmt.format(self.name, self.health, self.initiative)

    def roll_dice(self, num_of_dice):
        return [randint(1, 6) for roll in range(num_of_dice)]

    def rumble(self, enemy, print_roll):
        my_roll = self.roll_dice(self.dice)
        enemy_roll = enemy.roll_dice(enemy.dice)
        if print_roll:
            print("Player rolls: ",my_roll)
            print("Enemy rolls: ", enemy_roll)

        my_roll = max(my_roll)
        enemy_roll = max(enemy_roll)

        if my_roll > enemy_roll:
            enemy.health -= 1
        elif my_roll < enemy_roll:
            self.health -= 1
        else:
            if self.initiative < enemy.initiative:
                self.health -= 1
            else:
                enemy.health -= 1


class PlayableCharacter(Character):

    def __init__(self, name):
        super().__init__(name)
        self.health = 10
        self.dice = 3
        self.loot = set()
        self.rooms = set()
        self.defeated = list()


class EnemyCharacter(Character):
    enemy_list = ["Alicorn", "Banshee", "Basilisk", "Bigfoot", "Black Dog",
                  "Bogeyman", "Bogle", "Bray Road Beast", "Brownie", "Centaur",
                  "Cerberus", "Charybdis", "Chimera", "Cockatrice", "Cyclops",
                  "Cynocephalus", "Demon", "Doppelganger", "Dragon", "Dwarf",
                  "Echidna", "Elf", "Fairy", "Ghost", "Gnome", "Goblin",
                  "Golem", "Gorgon", "Griffin", "Grim Reaper", "Hobgoblin",
                  "Hydra", "Imp", "Ladon", "Leprechaun", "Loch Ness Monster",
                  "Manticore", "Medusa", "Mermaid", "Minotaur", "Mothman",
                  "Mutant", "Nemean Lion", "New Jersey Devil", "Nymph", "Ogre",
                  "Orthros", "Pegasus", "Phoenix", "Pixie", "Sasquatch",
                  "Satyr", "Scylla", "Sea-Goat", "Shade", "Shapeshifter",
                  "Siren", "Sphinx", "Sprite", "Sylph", "Thunderbird",
                  "Typhon", "Unicorn", "Valkyrie", "Vampire", "Wendigo",
                  "Will-o'-the-wisp", "Werewolf", "Wraith", "Zombie"]

    loot = ["Finger Nail", "Newt Hair", "Pinky Toe", "3rd Eye",
            "Thumbs"]

    def __init__(self):
        super().__init__(choice(self.enemy_list))
        self.enemy_list.remove(self.name)
        self.dice = randint(1, 3)
        self.health = self.dice

    def drop_loot(self):
        if len(self.loot) > 0 and (self.dice * 2) * 10 > randint(1, 100):
            return choice(self.loot)
