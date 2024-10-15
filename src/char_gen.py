# Standard Fantasy Character Generator Copyright (C) 2019-2024 Quinn Luetzow
# This file is part of Standard Fantasy Character Generator.

# Standard Fantasy Character Generator is free software: you can
# redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.

# Standard Fantasy Character Generator is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Standard Fantasy Character Generator. If not, see
# <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3

""" Character Generator for D20 systems.

A program to generate randomized characters for D20 systems.

Usage: python char_gen.py [--version] [--help] [-N] [-L]

Optional arguments:
    -h, --help     Show this help message and exit
    --version      Show the program version and exit
    -N             Generate N number of characters, defaults to 1 if not specified
    -L             Generate a character of level L, defaults to 1 if not specified
"""

__author__ = "Quinn Luetzow"
__version__ = 3.0

import sys
from random import randint
from string import capwords

from char_gen_components import (
    Alignment, Language, Size, Stat, BaseClass, Race, race_traits, race_proficiencies,
    ToolProficiencies, class_proficiencies, class_proficiency_choices
)


class Character:
    """Class representing a character"""

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
        self.health = 0
        self.hit_dice = None
        self.speed = None
        self.size = None
        self.languages = set()
        self.proficiencies = set()


def gender(player):
    """Randomly determine the gender of the character being created"""

    gen = randint(1, 100)  # 0-49 results in male, 50-99 results in female

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
        # Using the 4d6 drop lowest method
        rolls = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        rolls.remove(min(rolls))
        player.stats[key] = sum(rolls)


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

    player.languages.add(Language(0))  # All characters speak Common

    if player.race is Race.HUMAN:
        player.languages.add(Language(randint(1, 7)))
    elif player.race is Race.ELF:
        player.languages.add(Language.ELVISH)
    elif player.race is Race.DWARF:
        player.languages.add(Language.DWARVISH)
    elif player.race is Race.GNOME:
        player.languages.add(Language.GNOMISH)
    elif player.race is Race.HALFLING:
        player.languages.add(Language.HALFLING)
    elif player.race is Race.HALF_ELF:
        player.languages.add(Language.ELVISH)
        player.languages.add(Language(randint(2, 7)))
    elif player.race is Race.HALF_ORC:
        player.languages.add(Language.ORC)
    elif player.race is Race.DRAGONBORN:
        player.languages.add(Language.DRACONIC)
    elif player.race is Race.TIEFLING:
        player.languages.add(Language.INFERNAL)


def health(player):
    """Assign character's class-based health points and hit dice"""

    d6_hitdice = {BaseClass.SORCERER, BaseClass.WIZARD}
    d8_hitdice = {BaseClass.BARD, BaseClass.CLERIC, BaseClass.DRUID, BaseClass.MONK,
                  BaseClass.ROGUE, BaseClass.WARLOCK}
    d10_hitdice = {BaseClass.FIGHTER, BaseClass.PALADIN, BaseClass.RANGER}

    d12_hitdice = {BaseClass.BARBARIAN}

    if player.char_class in d8_hitdice:
        player.health = 8 + player.stats[Stat.CONSTITUTION]
        player.hit_dice = "1d8"
        if player.level > 1:
            for i in range(2, player.level):
                player.health += randint(1, 8) + player.stats[Stat.CONSTITUTION]

    elif player.char_class in d10_hitdice:
        player.health = 10 + player.stats[Stat.CONSTITUTION]
        player.hit_dice = "1d10"
        if player.level > 1:
            for i in range(2, player.level):
                player.health += randint(1, 10) + player.stats[Stat.CONSTITUTION]

    elif player.char_class in d6_hitdice:
        player.health = 6 + player.stats[Stat.CONSTITUTION]
        player.hit_dice = "1d6"
        if player.level > 1:
            for i in range(2, player.level):
                player.health += randint(1, 6) + player.stats[Stat.CONSTITUTION]

    elif player.char_class in d12_hitdice:
        player.health = 12 + player.stats[Stat.CONSTITUTION]
        player.hit_dice = "1d12"
        if player.level > 1:
            for i in range(2, player.level):
                player.health += randint(1, 12) + player.stats[Stat.CONSTITUTION]


def race_stat_effects(player):
    """Apply racial stat bonuses to the character being created"""

    player.speed = 30  # "Default" or most common speed and size, here to avoid repetition
    player.size = Size.MEDIUM

    match player.race:
        case Race.HUMAN:
            for key, val in player.stats.items():
                player.stats[key] += 1
        case Race.ELF:
            player.stats[Stat.DEXTERITY] += 2
        case Race.DWARF:
            player.stats[Stat.CONSTITUTION] += 2
            player.speed = 25
        case Race.GNOME:
            player.stats[Stat.INTELLIGENCE] += 2
            player.size = Size.SMALL
            player.speed = 25
        case Race.HALFLING:
            player.stats[Stat.DEXTERITY] += 2
            player.size = Size.SMALL
            player.speed = 25
        case Race.HALF_ELF:
            player.stats[Stat.CHARISMA] += 2

            rand_stat1 = randint(0, 5)  # Pick two random stats to give bonus to
            rand_stat2 = randint(0, 5)

            match rand_stat1:
                case 0:
                    player.stats[Stat.STRENGTH] += 1
                case 1:
                    player.stats[Stat.DEXTERITY] += 1
                case 2:
                    player.stats[Stat.CONSTITUTION] += 1
                case 3:
                    player.stats[Stat.INTELLIGENCE] += 1
                case 4:
                    player.stats[Stat.WISDOM] += 1
                case 5:
                    player.stats[Stat.CHARISMA] += 1

            match rand_stat2:
                case 0:
                    player.stats[Stat.STRENGTH] += 1
                case 1:
                    player.stats[Stat.DEXTERITY] += 1
                case 2:
                    player.stats[Stat.CONSTITUTION] += 1
                case 3:
                    player.stats[Stat.INTELLIGENCE] += 1
                case 4:
                    player.stats[Stat.WISDOM] += 1
                case 5:
                    player.stats[Stat.CHARISMA] += 1

        case Race.HALF_ORC:
            player.stats[Stat.CONSTITUTION] += 2
            player.stats[Stat.STRENGTH] += 1
        case Race.DRAGONBORN:
            player.stats[Stat.STRENGTH] += 2
            player.stats[Stat.CONSTITUTION] += 1
        case Race.TIEFLING:
            player.stats[Stat.CHARISMA] += 2
            player.stats[Stat.INTELLIGENCE] += 1

    # Make sure no stats are over 20 (max value) from racial bonuses
    for key, val in player.stats.items():
        if player.stats[key] > 20:
            player.stats[key] = 20


def level_stat_effects(player):
    """Assign ASI stat bumps to the character being created."""

    disallowed_stats = set()  # Stats that are maxed out at 20 already

    for stat in player.stats:
        if stat.value == 20:
            disallowed_stats.add(stat)

    # Milestone levels each class gets ASI at. Fighters get extra,
    # so will be processed separately.
    basic_asi_milestones = {4, 8, 12, 16, 19}
    fighter_asi_milestones = {4, 6, 8, 12, 14, 16, 19}

    def select_stat(disallowed):
        stat_1 = None
        stat_2 = None

        # Loop until valid stats are chosen
        while (stat_1 in disallowed or not stat_1 and
               stat_2 in disallowed or not stat_2):
            stat_1 = Stat(randint(0, 5))
            stat_2 = Stat(randint(0, 5))

        return stat_1, stat_2

    # Fighters get extra ASI bonuses, so run separately.
    if player.char_class == BaseClass.FIGHTER:
        for milestone_level in fighter_asi_milestones:  # Loop for each ASI
            if player.level >= milestone_level:
                # Select stat and increment by 1
                stat1, stat2 = select_stat(disallowed_stats)
                player.stats[stat1] += 1
                player.stats[stat2] += 1

                # To avoid going above 20 in any stat, if at 20 after this
                # round of bumps, add to disallowed stats.
                if player.stats[stat1] == 20:
                    disallowed_stats.add(stat1)
                if player.stats[stat2] == 20:
                    disallowed_stats.add(stat2)

    # All other class get the same number of ASI bonuses, so share logic.
    else:
        for milestone_level in basic_asi_milestones:  # Loop for each ASI.
            if player.level >= milestone_level:
                # Select stat and increment by 1.
                stat1, stat2 = select_stat(disallowed_stats)
                player.stats[stat1] += 1
                player.stats[stat2] += 1

                # To avoid going above 20 in any stat, if at 20 after this
                # round of bumps, add to disallowed stats.
                if player.stats[stat1] == 20:
                    disallowed_stats.add(stat1)
                if player.stats[stat2] == 20:
                    disallowed_stats.add(stat2)


def proficiencies(player):
    """Assign proficiencies to the character being created."""

    # Cutoff point for gaming set proficiencies, needed for monk.
    game_set_cutoff = 32

    # Cutoff points for instrument proficiencies, needed for bard.
    instrument_start_cutoff = 19
    instrument_end_cutoff = 28

    # How many random proficiencies.
    choose2 = {
        BaseClass.BARBARIAN, BaseClass.CLERIC, BaseClass.DRUID,
        BaseClass.FIGHTER, BaseClass.PALADIN, BaseClass.SORCERER,
        BaseClass.WARLOCK, BaseClass.WIZARD, BaseClass.MONK
    }
    choose3 = {BaseClass.BARD, BaseClass.RANGER}
    choose4 = {BaseClass.ROGUE}

    # Monk can also choose from anything except game sets.
    monk_opt = [ToolProficiencies(x) for x in range(game_set_cutoff)]

    # Bard can choose from random instruments.
    bard_opt = [
        ToolProficiencies(x) for x in range(instrument_start_cutoff,
                                            instrument_end_cutoff)
    ]

    def select_proficiency(amount):
        """Select the random proficiencies for the character"""

        options_list = list(class_proficiency_choices[player.char_class])

        # range() starts at 0, so subtract 1 to get the right number of selections.
        for i in range(amount - 1):
            while True:
                selection = options_list[randint(0, len(options_list) - 1)]
                if selection not in player.proficiencies:
                    player.proficiencies.add(selection)
                    break

        # Add random extra proficiencies for Monk and Bard.
        if player.char_class is BaseClass.MONK:
            player.proficiencies.add(monk_opt[randint(0, len(monk_opt) - 1)])
        elif player.char_class is BaseClass.BARD:
            instruments = 3
            while instruments > 0:
                selection = bard_opt[randint(0, len(bard_opt) - 1)]
                if selection not in player.proficiencies:
                    player.proficiencies.add(selection)
                    instruments -= 1
                else:
                    continue

    # Combine racial and class proficiencies together.
    player.proficiencies = race_proficiencies[player.race]
    player.proficiencies = player.proficiencies.union(class_proficiencies[player.char_class])

    # Select random proficiencies for class that get them.
    if player.char_class in choose2:
        select_proficiency(2)
    elif player.char_class in choose3:
        select_proficiency(3)
    elif player.char_class in choose4:
        select_proficiency(4)


def print_char(character):
    """Output each attribute of the created character to the console."""

    print("Gender: {0}".format("Female" if character.gender else "Male"))
    print("Race: {0}".format(character.race.name.capitalize()))
    print("Size: {0}".format(character.size.name.capitalize()))
    print("Walk speed: {0} feet".format(character.speed))

    print("Racial Traits: {0}".format(
        capwords(", ".join(x.name for x in character.traits).replace("_", " ")))
    )

    print("Class: {0}".format(character.char_class.name.capitalize()))
    print("Level: {0}".format(character.level))
    print("HP: {0}".format(character.health))
    print("Hit Dice: {0}".format(character.hit_dice))

    print("Alignment: {0}".format(
        capwords(
            character.alignment.name.replace("_", " "))
    )
    )

    for key, val in character.stats.items():
        print("{0}: {1}".format(key.name.lower().capitalize(), character.stats[key]))

    print("Languages Spoken: {0}".format(
        capwords(", ".join(x.name for x in character.languages).replace("_", " ")))
    )

    print("Proficiencies: {0}".format(
        capwords(", ".join(x.name for x in character.proficiencies).replace("_", " ")))
    )

    print()  # Print empty line between characters


def generate(lvl):
    """Workhorse function to keep main() uncluttered."""

    player = Character()

    gender(player)
    race(player)
    char_class(player)
    alignment(player)
    stats(player)
    level(player, lvl)
    race_stat_effects(player)
    level_stat_effects(player)
    health(player)
    languages(player)
    traits(player)
    proficiencies(player)

    return player


def main():
    """Main() function for program."""

    chars_to_generate = 1
    lvl = 1

    if len(sys.argv) >= 2:
        if sys.argv[1] == "--version":
            print("D20 Character Generator version {0}".format(__version__))
            sys.exit(0)
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(__doc__)
            sys.exit(0)
        elif sys.argv[1]:
            chars_to_generate = int((sys.argv[1])[1:])  # Exclude the - on the argument

            try:
                lvl = int((sys.argv[2])[1:])  # Exclude the - on the argument
            except IndexError:
                pass  # Do nothing, use default value set above

        else:
            print("Invalid argument passed: {0}".format(sys.argv[1]))
            print(__doc__)
            sys.exit(1)

    for i in range(chars_to_generate):
        character = generate(lvl)
        print_char(character)


if __name__ == "__main__":
    main()
