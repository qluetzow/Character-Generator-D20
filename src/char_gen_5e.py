# D&D Character Generator 5e Copyright (C) 2019-2020 Quinn Luetzow
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

#!/usr/bin/env python3

""" Character Generator for Dungeons & Dragons 5th Edition.

A program to generate randomized characters for D&D 5th Edition.

Usage: python char_gen_5e.py [--version] [--help] [-N] [-L]

Optional arguments:
    -h, --help     Show this help message and exit
    --version      Show the program version and exit
    -N             Generate N number of characters, defaults to 1 if not specified
    -L             Generate a character of level L, defaults to 1 if not specified
"""

__author__ = "Quinn Luetzow"
__version__ = 2.2


import sys
from random import randint
from string import capwords

from char_gen_components import *


class Character:
    """Class representing a D&D 5th Edition character"""

    def __init__(self):
        self.gender = None
        self.race = None
        self.traits = []
        self.char_class = None
        self.alignment = None
        self.stats = {
            Stat.STRENGTH: 0, Stat.DEXTERITY: 0, Stat.CONSTITUTION: 0,
            Stat.INTELLIGENCE: 0, Stat.WISDOM: 0, Stat.CHARISMA: 0
        }
        self.level = 0
        self.speed = None
        self.size = None
        self.languages = []


def gender(player):
    """Randomly determine the gender of the character being created"""

    gen = randint(0, 99)  # 0-49 results in male, 50-99 results in female

    player.gender = True if gen >= 50 else False


def race(player):
    """Randomly determine the race of the character being created"""

    player.race = Race(randint(0, 8))


def char_class(player):
    """Randomly determine the class of the character being created"""

    player.char_class = BaseClass(randint(0, 11))


def stats(player):
    """Randomly assign initial stat values to the character being created"""

    for key, val in player.stats.items():
        player.stats[key] = randint(3, 18)


def alignment(player):
    """Randomly determine alignment of the character being created"""

    player.alignment = Alignment(randint(0, 8))


def level(player, lvl):
    """Assign a character level to the character being generated"""

    player.level = lvl


def traits(player):
    """Assign appropriate racial traits to the character being created"""

    player.traits = race_traits[player.race]


def languages(player):
    """Assign racial and extra languages to the character being created"""

    player.languages.append(Language(0))  # All characters speak Common

    if player.race is Race.HUMAN:
        player.languages.append(Language(randint(1, 7)))
    elif player.race is Race.ELF:
        player.languages.append(Language.ELVISH)
    elif player.race is Race.DWARF:
        player.languages.append(Language.DWARVISH)
    elif player.race is Race.GNOME:
        player.languages.append(Language.GNOMISH)
    elif player.race is Race.HALFLING:
        player.languages.append(Language.HALFLING)
    elif player.race is Race.HALF_ELF:
        player.languages.append(Language.ELVISH)
        player.languages.append(Language(randint(2, 7)))
    elif player.race is Race.HALF_ORC:
        player.languages.append(Language.ORC)
    elif player.race is Race.DRAGONBORN:
        player.languages.append(Language.DRACONIC)
    elif player.race is Race.TIEFLING:
        player.languages.append(Language.INFERNAL)


def race_stat_effects(player):
    """Apply racial stat bonuses to the character being created"""

    player.speed = 30       # "Default" or most common speed and size, here to avoid repetition
    player.size = Size.MEDIUM

    if player.race is Race.HUMAN:
        for key, val in player.stats.items():
            player.stats[key] += 1
    elif player.race is Race.ELF:
        player.stats[Stat.DEXTERITY] += 2
    elif player.race is Race.DWARF:
        player.stats[Stat.CONSTITUTION] += 2
        player.speed = 25
    elif player.race is Race.GNOME:
        player.stats[Stat.INTELLIGENCE] += 2
        player.size = Size.SMALL
        player.speed = 25
    elif player.race is Race.HALFLING:
        player.stats[Stat.DEXTERITY] += 2
        player.size = Size.SMALL
        player.speed = 25
    elif player.race is Race.HALF_ELF:
        player.stats[Stat.CHARISMA] += 2


        rand_stat1 = randint(0, 5)  # Pick two random stats to give bonus to
        rand_stat2 = randint(0, 5)

        if rand_stat1 == 0:
            player.stats[Stat.STRENGTH] += 1
        elif rand_stat1 == 1:
            player.stats[Stat.DEXTERITY] += 1
        elif rand_stat1 == 2:
            player.stats[Stat.CONSTITUTION] += 1
        elif rand_stat1 == 3:
            player.stats[Stat.INTELLIGENCE] += 1
        elif rand_stat1 == 4:
            player.stats[Stat.WISDOM] += 1
        elif rand_stat1 == 5:
            player.stats[Stat.CHARISMA] += 1

        if rand_stat2 == 0:
            player.stats[Stat.STRENGTH] += 1
        elif rand_stat2 == 1:
            player.stats[Stat.DEXTERITY] += 1
        elif rand_stat2 == 2:
            player.stats[Stat.CONSTITUTION] += 1
        elif rand_stat2 == 3:
            player.stats[Stat.INTELLIGENCE] += 1
        elif rand_stat2 == 4:
            player.stats[Stat.WISDOM] += 1
        elif rand_stat2 == 5:
            player.stats[Stat.CHARISMA] += 1

    elif player.race is Race.HALF_ORC:
        player.stats[Stat.STRENGTH] += 2
        player.stats[Stat.CONSTITUTION] += 1
    elif player.race is Race.DRAGONBORN:
        player.stats[Stat.STRENGTH] += 2
        player.stats[Stat.CONSTITUTION] += 1
    elif player.race is Race.TIEFLING:
        player.stats[Stat.INTELLIGENCE] += 1
        player.stats[Stat.CHARISMA] += 2

    # Make sure no stats are over 18 (max value) from racial bonuses
    for key, val in player.stats.items():
        if player.stats[key] > 18:
            player.stats[key] = 18


def print_char(character):
    """Output each attribute of the created character to the console."""

    print("Gender: {0}".format("Female" if character.gender else "Male"))
    print("Race: {0}".format(character.race.name.capitalize()))
    print("Racial Traits: {0}".format(capwords(", ".join(x.name for x in character.traits).replace("_", " "))))
    print("Class: {0}".format(character.char_class.name.capitalize()))
    print("Level: {0}".format(character.level))
    print("Alignment: {0}".format(capwords(character.alignment.name.replace("_", " "))))

    for key, val in character.stats.items():
        print("{0}: {1}".format(key.name.lower().capitalize(), character.stats[key]))

    print("Languages Spoken: {0}".format(capwords(", ".join(x.name for x in character.languages).replace("_", " "))))

    print("Walk speed: {0} feet".format(character.speed))
    print("Size: {0}".format(character.size.name.capitalize()))

    print()  # Print empty line between characters


def generate(lvl):
    """Workhorse function to keep main() uncluttered."""

    player = Character()

    gender(player)
    race(player)
    char_class(player)
    alignment(player)
    stats(player)
    race_stat_effects(player)
    level(player, lvl)
    languages(player)
    traits(player)

    return player


def main():
    """Main() function for program."""

    chars_to_generate = 1
    lvl = 1

    if len(sys.argv) >= 2:
            if sys.argv[1] == "--version":
                print("D&D Character Generator 5th Edition version {0}".format(__version__))
                exit(0)
            elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
                print(__doc__)
                exit(0)
            elif sys.argv[1]:
                chars_to_generate = int((sys.argv[1])[1:])  # Exclude the - on the argument

                try:
                    lvl = (sys.argv[2])[1:]  # Exclude the - on the argument
                except IndexError:
                    pass  # Do nothing, use default value set above

            else:
                print("Invalid argument passed: {0}".format(sys.argv[1]))
                print(__doc__)
                exit(1)

    for ch in range(chars_to_generate):
        character = generate(lvl)
        print_char(character)


if __name__ == "__main__":
    main()
