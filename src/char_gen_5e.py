# This file is part of D&D Character Generator 5e.

# D&D Character Generator 5e is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# D&D Character Generator 5e is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with D&D Character Generator 5e.  If not, see <https://www.gnu.org/licenses/>.


""" Character Generator for Dungeons & Dragons 5th Edition.

A program to generate randomized characters for D&D 5th Edition.

Usage: python char_gen_5e.py [--version] [--help] [-N]

Optional arguments:
    -h, --help     Show this help message and exit
    --version      Show the program version and exit
    -N             Generate N number of characters, defaults to 1 if not specified
"""

__author__ = "Quinn Luetzow"
__version__ = 1.0


import sys
from random import randint


class Character:
    """Class representing a D&D 5th Edition character"""

    def __init__(self):
        self.gender = None
        self.race = ""
        self.traits = ""
        self.char_class = ""
        self.alignment = ""
        self.constitution = 0
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.speed = 0
        self.size = ""
        self.languages = []


races = {
    0: "Human", 1: "Elf", 2: "Dwarf", 3: "Gnome", 4: "Halfling", 5: "Half-elf", 6: "Half-orc",
    7: "Dragonborn", 8: "Tiefling"
}

langs = {
    0: "Common", 1: "Elvish", 2: "Dwarvish", 3: "Gnomish", 4: "Orc", 5: "Halfling",
    6: "Draconic", 7: "Infernal"
}

alignments = {
    0: "Lawful Good", 1: "Lawful Neutral", 2: "Lawful Evil", 3: "Neutral Good", 4: "True Neutral",
    5: "Neutral Evil", 6: "Chaotic Good", 7: "Chaotic Neutral", 8: "Chaotic Evil"
}

base_classes = {
    0: "Barbarian", 1: "Bard", 2: "Cleric", 3: "Druid", 4: "Fighter", 5: "Monk", 6: "Paladin",
    7: "Ranger", 8: "Rogue", 9: "Sorcerer", 10: "Wizard", 11: "Warlock"
}

char_traits = {
    "Elf": ("Darkvision", "Keen Senses", "Fey Ancestry", "Trance"),
    "Dwarf": ("Darkvision", "Dwarven Resistance", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning"),
    "Gnome": ("Darkvision", "Gnome Cunning"),
    "Halfling": ("Lucky", "Brave", "Halfling Nimbleness"),
    "Half-elf": ("Darkvision", "Fey Ancestry", "Skill Versatility"),
    "Half-orc": ("Darkvision", "Menacing", "Relentless Endurance", "Savage Attacks"),
    "Dragonborn": ("Damage Resistance",),
    "Tiefling": ("Darkvision", "Hellish Resistance", "Infernal Legacy")

}


def gender(player):
    """Randomly determine the gender of the character being created"""

    gen = randint(0, 100)  # 0-49 results in male, 50-99 results in female

    player.gender = True if gen >= 50 else False


def race(player):
    """Randomly determine the race of the character being created"""
    player.race = races[randint(0, 8)]


def char_class(player):
    """Randomly determine the class of the character being created"""

    player.char_class = base_classes[randint(0, 11)]


def stats(player):
    """Randomly assign initial stat values to the character being created"""

    player.constitution = randint(3, 18)
    player.strength = randint(3, 18)
    player.dexterity = randint(3, 18)
    player.intelligence = randint(3, 18)
    player.wisdom = randint(3, 18)
    player.charisma = randint(3, 18)


def alignment(player):
    """Randomly determine alignment of the character being created"""

    player.alignment = alignments[randint(0, 8)]


def languages(player):
    """Assign racial and extra languages to the character being created"""

    player.languages.append(langs[0])  # All characters speak Common

    if player.race == "Human":
        player.languages.append(langs[randint(1, 7)])
    elif player.race == "Elf":
        player.languages.append(langs[1])
    elif player.race == "Dwarf":
        player.languages.append(langs[2])
    elif player.race == "Gnome":
        player.languages.append(langs[3])
    elif player.race == "Halfling":
        player.languages.append(langs[5])
    elif player.race == "Half-elf":
        player.languages.append(langs[1])
        player.languages.append((langs[randint(2, 7)]))
    elif player.race == "Half-orc":
        player.languages.append(langs[4])
    elif player.race == "Dragonborn":
        player.languages.append(langs[6])
    elif player.race == "Tiefling":
        player.languages.append(langs[7])


def race_stat_effects(player):
    """Apply racial stat bonuses to the character being created"""

    player.speed = 30       # "Default" or most common speed and size, here to avoid repetition
    player.size = "Medium"

    if player.race == "Human":
        player.constitution += 1
        player.strength += 1
        player.dexterity += 1
        player.intelligence += 1
        player.wisdom += 1
        player.charisma += 1
    elif player.race == "Elf":
        player.dexterity += 2
    elif player.race == "Dwarf":
        player.constitution += 2
        player.speed = 25
    elif player.race == "Gnome":
        player.intelligence += 2
        player.size = "Small"
        player.speed = 25
    elif player.race == "Halfling":
        player.dexterity += 2
        player.size = "Small"
        player.speed = 25
    elif player.race == "Half-elf":
        player.charisma += 2

        rand_stat1 = randint(0, 5)  # Pick two random stats to give bonus to
        rand_stat2 = randint(0, 5)

        if rand_stat1 == 0:
            player.constitution += 1
        elif rand_stat1 == 1:
            player.strength += 1
        elif rand_stat1 == 2:
            player.dexterity += 1
        elif rand_stat1 == 3:
            player.intelligence += 1
        elif rand_stat1 == 4:
            player.wisdom += 1
        elif rand_stat1 == 5:
            player.charisma += 1

        if rand_stat2 == 0:
            player.constitution += 1
        elif rand_stat2 == 1:
            player.strength += 1
        elif rand_stat2 == 2:
            player.dexterity += 1
        elif rand_stat2 == 3:
            player.intelligence += 1
        elif rand_stat2 == 4:
            player.wisdom += 1
        elif rand_stat2 == 5:
            player.charisma += 1

    elif player.race == "Half-orc":
        player.strength += 2
        player.constitution += 1
    elif player.race == "Dragonborn":
        player.strength += 2
        player.charisma += 1
    elif player.race == "Tiefling":
        player.intelligence += 1
        player.charisma += 2

    # Make sure no stats are over 18 (max value) from racial bonuses
    if player.constitution > 18:
        player.constitution = 18
    if player.strength > 18:
        player.strength = 18
    if player.dexterity > 18:
        player.dexterity = 18
    if player.intelligence > 18:
        player.intelligence = 18
    if player.wisdom > 18:
        player.wisdom = 18
    if player.charisma > 18:
        player.charisma = 18


def traits(player):
    """Assign appropriate racial traits to the character being created"""
    player.traits = char_traits.get(player.race, ())


def print_char(character):
    """Output each attribute of the created character to the console."""

    print("Gender: {0}".format("Female" if character.gender else "Male"))
    print("Race: {0}".format(character.race))
    print("Racial Traits: {0}".format(", ".join(character.traits)))
    print("Class: {0}".format(character.char_class))
    print("Alignment: {0}".format(character.alignment))

    print("Constitution: {0}".format(character.constitution))
    print("Strength: {0}".format(character.strength))
    print("Dexterity: {0}".format(character.dexterity))
    print("Intelligence: {0}".format(character.intelligence))
    print("Wisdom: {0}".format(character.wisdom))
    print("Charisma: {0}".format(character.charisma))

    print("Languages Spoken: {0}".format(", ".join(character.languages)))

    print("Walk speed: {0} feet".format(character.speed))
    print("Size: {0}".format(character.size))

    print()  # Print empty line between characters


def generate():
    """Workhorse function to keep main() uncluttered."""

    player = Character()

    gender(player)
    race(player)
    char_class(player)
    alignment(player)
    stats(player)
    race_stat_effects(player)
    languages(player)
    traits(player)

    return player


def main():
    """Main() function for program."""

    chars_to_generate = 1

    if len(sys.argv) == 2:
            if sys.argv[1] == "--version":
                print("D&D Character Generator 5th Edition version {0}".format(__version__))
                exit(0)
            elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
                print(__doc__)
                exit(0)
            elif (sys.argv[1])[1:]:
                chars_to_generate = int((sys.argv[1])[1:])
            else:
                print("Invalid argument passed: {0}".format(sys.argv[1]))
                print(__doc__)
                exit(1)

    for i in range(chars_to_generate):
        character = generate()
        print_char(character)


if __name__ == "__main__":
    main()
