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


"""A collection of components used for the main character generator."""


from enum import Enum


class Race(Enum):
    """Character races."""

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
    """Character stats."""

    STRENGTH = 0
    DEXTERITY = 1
    CONSTITUTION = 2
    INTELLIGENCE = 3
    WISDOM = 4
    CHARISMA = 5


class Size(Enum):
    """Character sizes."""

    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    HUGE = 3   # not currently used, but available for future use/expansion


class Language(Enum):
    """Languages characters can speak."""

    COMMON = 0
    ELVISH = 1
    DWARVISH = 2
    GNOMISH = 3
    ORC = 4
    HALFLING = 5
    DRACONIC = 6
    INFERNAL = 7


class Alignment(Enum):
    """Alignments for characters."""

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
    """Base classes for characters."""

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
    """Racial trait names."""

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
    DRACONIC_ANCESTRY = "Draconic Ancestry"
    DAMAGE_RESISTANCE = "Damage Resistance"
    BREATH_WEAPON = "Breath Weapon"
    HELLISH_RESISTANCE = "Hellish Resistance"
    INFERNAL_LEGACY = "Infernal Legacy"


class StatProficiencies(Enum):
    """Saves that characters can be proficient in."""

    STRENGTH = 0
    DEXTERITY = 1
    CONSTITUTION = 2
    INTELLIGENCE = 3
    WISDOM = 4
    CHARISMA = 5


class TestProficiencies(Enum):
    """Skills that characters can be proficient in."""

    ATHLETICS = 0
    ACROBATICS = 1
    SLEIGHT_OF_HAND = 8
    STEALTH = 9
    ARCANA = 10
    HISTORY = 11
    INVESTIGATION = 12
    NATURE = 13
    RELIGION = 14
    ANIMAL_HANDLING = 15
    INSIGHT = 16
    MEDICINE = 17
    PERCEPTION = 18
    SURVIVAL = 19
    DECEPTION = 20
    INTIMIDATION = 21
    PERFORMANCE = 22
    PERSUASION = 23


class BaseEquipProficiencies(Enum):
    """General equipment classes that characters can be proficient in."""
    SIMPLE_WEAPONS = 0
    MARTIAL_WEAPONS = 1
    LIGHT_ARMOR = 2
    MEDIUM_ARMOR = 3
    HEAVY_ARMOR = 4
    SHIELD = 5


class EquipProficiencies(Enum):
    """Specific weapons that characters can be proficient in."""
    CLUB = 0
    DAGGER = 1
    GREATCLUB = 2
    HANDAXE = 3
    JAVELIN = 4
    LIGHT_HAMMER = 5
    MACE = 6
    QUARTERSTAFF = 7
    SICKLE = 8
    SPEAR = 9
    UNARMED = 10
    LIGHT_CROSSBOW = 11
    DART = 12
    SHORTBOW = 13
    SLING = 14
    BATTLEAXE = 15
    FLAIL = 16
    GLAIVE = 17
    GREATAXE = 18
    GREATSWORD = 19
    HALBERD = 20
    LANCE = 21
    LONGSWORD = 22
    MAUL = 23
    MORNINGSTAR = 24
    PIKE = 25
    RAPIER = 26
    SCIMITAR = 27
    SHORTSWORD = 28
    TRIDENT = 29
    WAR_PICK = 30
    WARHAMMER = 31
    WHIP = 32
    BLOWGUN = 33
    HAND_CROSSBOW = 34
    HEAVY_CROSSBOW = 35
    LONGBOW = 36
    NET = 37


class ToolProficiencies(Enum):
    """Tools that characters can be proficient in."""
    ALCHEMIST_SUPPLIES = 0
    BREWER_SUPPLIES = 1
    CALLIGRAPHER_TOOLS = 2
    CARPENTER_TOOLS = 3
    CARTOGRAPHER_TOOLS = 4
    COBBLER_TOOLS = 5
    COOK_UTENSILS = 6
    GLASSBLOWER_TOOLS = 7
    JEWELER_TOOLS = 8
    MASON_TOOLS = 9
    PAINTER_SUPPLIES = 10
    POTTER_TOOLS = 11
    SMITH_TOOLS = 12
    TINKER_TOOLS = 13
    WEAVER_TOOLS = 14
    WOODCARVER_TOOLS = 15
    DISGUISE_KIT = 16
    FORGERY_KIT = 17
    HERBALISM_KIT = 18
    BAGPIPES = 19
    DRUM = 20
    DULCIMER = 21
    FLUTE = 22
    LUTE = 23
    LYRE = 24
    HORN = 25
    PAN_FLUTE = 26
    SHAWM = 27
    VIOL = 28
    NAVIGATOR_TOOLS = 29
    POISONER_KIT = 30
    THIEF_TOOLS = 31
    DICE_SET = 32
    DRAGONCHESS_SET = 33
    PLAYING_CARD_SET = 34
    THREE_DRAGON_ANTE_SET = 35


race_traits = {
    Race.HUMAN: [],

    Race.ELF: [RaceTraits.DARKVISION, RaceTraits.KEEN_SENSES, RaceTraits.FEY_ANCESTRY,
               RaceTraits.TRANCE],

    Race.DWARF: [RaceTraits.DARKVISION, RaceTraits.DWARVEN_RESISTANCE,
                 RaceTraits.DWARVERN_COMBAT_TRAINING,
                 RaceTraits.TOOL_PROFICIENCY, RaceTraits.STONECUNNING],

    Race.GNOME: [RaceTraits.DARKVISION, RaceTraits.GNOME_CUNNING],

    Race.HALFLING: [RaceTraits.LUCKY, RaceTraits.BRAVE,
                    RaceTraits.HALFLING_NIMBLENESS],

    Race.HALF_ELF: [RaceTraits.DARKVISION, RaceTraits.FEY_ANCESTRY,
                    RaceTraits.SKILL_VERSATILITY],

    Race.HALF_ORC: [RaceTraits.DARKVISION, RaceTraits.MENACING,
                    RaceTraits.RELENTLESS_ENDURANCE, RaceTraits.SAVAGE_ATTACKS],

    Race.DRAGONBORN: [RaceTraits.DRACONIC_ANCESTRY, RaceTraits.DAMAGE_RESISTANCE,
                      RaceTraits.BREATH_WEAPON],

    Race.TIEFLING: [RaceTraits.DARKVISION, RaceTraits.HELLISH_RESISTANCE,
                    RaceTraits.INFERNAL_LEGACY]
}


race_proficiencies = {
    Race.HUMAN: set(),

    Race.ELF: set(),

    Race.DWARF: set(),

    Race.GNOME: set(),

    Race.HALFLING: set(),

    Race.HALF_ELF: set(),

    Race.HALF_ORC: {
        TestProficiencies.INTIMIDATION
    },

    Race.DRAGONBORN: set(),

    Race.TIEFLING: set()
}

""" Starting point for class-based proficiencies. This does NOT
    list all of the proficiencies to be assigned, as some are
    randomized. Due to the fact that if they were picked here,they
    would be identical for all characters generated in a single
    session, they will be generated separately later.
"""
class_proficiencies = {
    BaseClass.BARBARIAN: {
        StatProficiencies.STRENGTH,
        StatProficiencies.CONSTITUTION,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.MEDIUM_ARMOR, BaseEquipProficiencies.SHIELD,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        BaseEquipProficiencies.MARTIAL_WEAPONS
    },

    BaseClass.BARD: {
        StatProficiencies.DEXTERITY,
        StatProficiencies.CHARISMA,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        EquipProficiencies.HAND_CROSSBOW, EquipProficiencies.LONGSWORD,
        EquipProficiencies.RAPIER, EquipProficiencies.SHORTSWORD
    },

    BaseClass.CLERIC: {
        StatProficiencies.WISDOM,
        StatProficiencies.CHARISMA,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.MEDIUM_ARMOR, BaseEquipProficiencies.SHIELD,
        BaseEquipProficiencies.SIMPLE_WEAPONS
    },

    BaseClass.DRUID: {
        StatProficiencies.INTELLIGENCE,
        StatProficiencies.WISDOM,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.MEDIUM_ARMOR, BaseEquipProficiencies.SHIELD,
        EquipProficiencies.CLUB, EquipProficiencies.DAGGER,
        EquipProficiencies.DART, EquipProficiencies.JAVELIN,
        EquipProficiencies.QUARTERSTAFF,
        EquipProficiencies.SCIMITAR, EquipProficiencies.SICKLE,
        EquipProficiencies.SLING, EquipProficiencies.SPEAR,
        ToolProficiencies.HERBALISM_KIT
    },

    BaseClass.FIGHTER: {
        StatProficiencies.STRENGTH,
        StatProficiencies.CONSTITUTION,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.MEDIUM_ARMOR,
        BaseEquipProficiencies.HEAVY_ARMOR,
        BaseEquipProficiencies.SHIELD,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        BaseEquipProficiencies.MARTIAL_WEAPONS
    },

    BaseClass.MONK: {
        StatProficiencies.STRENGTH,
        StatProficiencies.DEXTERITY,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        EquipProficiencies.SHORTSWORD
    },

    BaseClass.PALADIN: {
        StatProficiencies.WISDOM,
        StatProficiencies.CHARISMA,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.MEDIUM_ARMOR,
        BaseEquipProficiencies.HEAVY_ARMOR,
        BaseEquipProficiencies.SHIELD,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        BaseEquipProficiencies.MARTIAL_WEAPONS
    },

    BaseClass.RANGER: {
        StatProficiencies.STRENGTH,
        StatProficiencies.DEXTERITY,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.MEDIUM_ARMOR, BaseEquipProficiencies.SHIELD,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        BaseEquipProficiencies.MARTIAL_WEAPONS
    },

    BaseClass.ROGUE: {
        StatProficiencies.DEXTERITY, StatProficiencies.INTELLIGENCE,
        BaseEquipProficiencies.LIGHT_ARMOR,
        BaseEquipProficiencies.SIMPLE_WEAPONS,
        EquipProficiencies.HAND_CROSSBOW, EquipProficiencies.LONGSWORD,
        EquipProficiencies.RAPIER, EquipProficiencies.SHORTSWORD,
        ToolProficiencies.THIEF_TOOLS
    },

    BaseClass.SORCERER: {
        StatProficiencies.CONSTITUTION,
        StatProficiencies.CHARISMA,
        EquipProficiencies.DAGGER, EquipProficiencies.DART,
        EquipProficiencies.SLING, EquipProficiencies.QUARTERSTAFF,
        EquipProficiencies.LIGHT_CROSSBOW
    },

    BaseClass.WIZARD: {
        StatProficiencies.INTELLIGENCE,
        StatProficiencies.WISDOM,
        EquipProficiencies.DAGGER, EquipProficiencies.DART,
        EquipProficiencies.SLING, EquipProficiencies.QUARTERSTAFF,
        EquipProficiencies.LIGHT_CROSSBOW
    },

    BaseClass.WARLOCK: {
        StatProficiencies.WISDOM,
        StatProficiencies.CHARISMA,
        BaseEquipProficiencies.LIGHT_ARMOR, BaseEquipProficiencies.SIMPLE_WEAPONS
    }
}

""" Choices for the class-based proficiencies that are 'pick x from
    {y, z, ...}
"""
class_proficiency_choices = {
    BaseClass.BARBARIAN: {
        TestProficiencies.ANIMAL_HANDLING,
        TestProficiencies.ATHLETICS,
        TestProficiencies.INTIMIDATION,
        TestProficiencies.NATURE,
        TestProficiencies.PERCEPTION,
        TestProficiencies.SURVIVAL
    },

    BaseClass.BARD: {x for x in TestProficiencies},

    BaseClass.CLERIC: {
        TestProficiencies.HISTORY,
        TestProficiencies.INSIGHT,
        TestProficiencies.MEDICINE,
        TestProficiencies.PERSUASION,
        TestProficiencies.RELIGION
    },

    BaseClass.DRUID: {
        TestProficiencies.ARCANA,
        TestProficiencies.ANIMAL_HANDLING,
        TestProficiencies.INSIGHT,
        TestProficiencies.MEDICINE,
        TestProficiencies.NATURE,
        TestProficiencies.PERCEPTION,
        TestProficiencies.RELIGION,
        TestProficiencies.SURVIVAL
    },

    BaseClass.FIGHTER: {
        TestProficiencies.ACROBATICS,
        TestProficiencies.ANIMAL_HANDLING,
        TestProficiencies.ATHLETICS,
        TestProficiencies.HISTORY,
        TestProficiencies.INSIGHT,
        TestProficiencies.INTIMIDATION,
        TestProficiencies.PERCEPTION,
        TestProficiencies.SURVIVAL
    },

    BaseClass.MONK: {
        TestProficiencies.ACROBATICS,
        TestProficiencies.ATHLETICS,
        TestProficiencies.HISTORY,
        TestProficiencies.INSIGHT,
        TestProficiencies.RELIGION,
        TestProficiencies.STEALTH
    },

    BaseClass.PALADIN: {
        TestProficiencies.ATHLETICS,
        TestProficiencies.INSIGHT,
        TestProficiencies.INTIMIDATION,
        TestProficiencies.MEDICINE,
        TestProficiencies.PERSUASION,
        TestProficiencies.RELIGION
    },

    BaseClass.RANGER: {
        TestProficiencies.ANIMAL_HANDLING,
        TestProficiencies.ATHLETICS,
        TestProficiencies.INSIGHT,
        TestProficiencies.INVESTIGATION,
        TestProficiencies.NATURE,
        TestProficiencies.PERCEPTION,
        TestProficiencies.STEALTH,
        TestProficiencies.SURVIVAL
    },

    BaseClass.ROGUE: {
        TestProficiencies.ACROBATICS,
        TestProficiencies.ATHLETICS,
        TestProficiencies.DECEPTION,
        TestProficiencies.INSIGHT,
        TestProficiencies.INTIMIDATION,
        TestProficiencies.INVESTIGATION,
        TestProficiencies.PERCEPTION,
        TestProficiencies.PERFORMANCE,
        TestProficiencies.PERSUASION,
        TestProficiencies.SLEIGHT_OF_HAND,
        TestProficiencies.STEALTH,
    },

    BaseClass.SORCERER: {
        TestProficiencies.ARCANA,
        TestProficiencies.DECEPTION,
        TestProficiencies.INSIGHT,
        TestProficiencies.INTIMIDATION,
        TestProficiencies.PERSUASION,
        TestProficiencies.RELIGION
    },

    BaseClass.WIZARD: {
        TestProficiencies.ARCANA,
        TestProficiencies.ARCANA,
        TestProficiencies.INSIGHT,
        TestProficiencies.INVESTIGATION,
        TestProficiencies.MEDICINE,
        TestProficiencies.RELIGION
    },

    BaseClass.WARLOCK: {
        TestProficiencies.ARCANA,
        TestProficiencies.DECEPTION,
        TestProficiencies.ARCANA,
        TestProficiencies.INTIMIDATION,
        TestProficiencies.INVESTIGATION,
        TestProficiencies.NATURE,
        TestProficiencies.RELIGION
    }
}
