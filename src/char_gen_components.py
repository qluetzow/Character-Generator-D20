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


from enum import Enum


class Race(Enum):
    HUMAN = 0
    ELF = 1
    DWARF = 2
    GNOME = 3
    HALFLING = 4
    HALF_ELF = 5
    HALF_ORC = 6
    DRAGONBORN = 7
    TIEFLING = 8


class Stat(Enum):
    STRENGTH = 0
    DEXTERITY = 1
    CONSTITUTION = 2
    INTELLIGENCE = 3
    WISDOM = 4
    CHARISMA = 5


class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    HUGE = 3   # not currently used, but available for future use/expansion


class Language(Enum):
    COMMON = 0
    ELVISH = 1
    DWARVISH = 2
    GNOMISH = 3
    ORC = 4
    HALFLING = 5
    DRACONIC = 6
    INFERNAL = 7


class Alignment(Enum):
    LAWFUL_GOOD = 0
    LAWFUL_NEUTRAL = 1
    LAWFUL_EVIL = 2
    NEUTRAL_GOOD = 3
    TRUE_NEUTRAL = 4
    NEUTRAL_EVIL = 5
    CHAOTIC_GOOD = 6
    CHAOTIC_NEUTRAL = 7
    CHAOTIC_EVIL = 8


class BaseClass(Enum):
    BARBARIAN = 0
    BARD = 1
    CLERIC = 2
    DRUID = 3
    FIGHTER = 4
    MONK = 5
    PALADIN = 6
    RANGER = 7
    ROGUE = 8
    SORCERER = 9
    WIZARD = 10
    WARLOCK = 11


class RaceTraits(Enum):
    DARKVISION = "Darkvision"
    KEEN_SENSES = "Keen Senses"
    FEY_ANCESTRY = "Fey Ancestry"
    TRANCE = "Trance"
    DWARVEN_RESISTANCE = "Dwarven Resistance"
    DWARVERN_COMBAT_TRAINING = "Dwarven Combat Training"
    TOOL_PROFICIENCY = "Tool Proficiency"
    STONECUNNING = "Stonecunning"
    GNOME_CUNNING = "Gnome Cunning"
    LUCKY = "Lucky"
    BRAVE = "Brave"
    HALFLING_NIMBLENESS = "Halfling Nimbleness"
    SKILL_VERSATILITY = "Skill Versatility"
    MENACING = "Menacing"
    RELENTLESS_ENDURANCE = "Relentless Endurance"
    SAVAGE_ATTACKS = "Savage Attacks"
    DRACONIC_ANCESTRY= "Draconic Ancestry"
    DAMAGE_RESISTANCE = "Damage Resistance"
    BREATH_WEAPON = "Breath Weapon"
    HELLISH_RESISTANCE = "Hellish Resistance"
    INFERNAL_LEGACY = "Infernal Legacy"


race_traits = {
    Race.HUMAN: {},

    Race.ELF: (RaceTraits.DARKVISION, RaceTraits.KEEN_SENSES, RaceTraits.FEY_ANCESTRY, RaceTraits.TRANCE),

    Race.DWARF: (RaceTraits.DARKVISION, RaceTraits.DWARVEN_RESISTANCE, RaceTraits.DWARVERN_COMBAT_TRAINING,
                 RaceTraits.TOOL_PROFICIENCY, RaceTraits.STONECUNNING),

    Race.GNOME: (RaceTraits.DARKVISION, RaceTraits.GNOME_CUNNING),

    Race.HALFLING: (RaceTraits.LUCKY, RaceTraits.BRAVE, RaceTraits.HALFLING_NIMBLENESS),

    Race.HALF_ELF: (RaceTraits.DARKVISION, RaceTraits.FEY_ANCESTRY, RaceTraits.SKILL_VERSATILITY),

    Race.HALF_ORC: (RaceTraits.DARKVISION, RaceTraits.MENACING, RaceTraits.RELENTLESS_ENDURANCE,
                    RaceTraits.SAVAGE_ATTACKS),

    Race.DRAGONBORN: (RaceTraits.DRACONIC_ANCESTRY, RaceTraits.DAMAGE_RESISTANCE, RaceTraits.BREATH_WEAPON),

    Race.TIEFLING: (RaceTraits.DARKVISION, RaceTraits.HELLISH_RESISTANCE, RaceTraits.INFERNAL_LEGACY)
}
