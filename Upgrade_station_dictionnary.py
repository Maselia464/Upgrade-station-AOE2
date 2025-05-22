#Ceci est le dictionnaire de la station d'amélioration,
from email.headerregistry import UniqueUnstructuredHeader

from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.trigger_lists import Attribute, ObjectAttribute, Operation
from AoE2ScenarioParser.datasets.units import UnitInfo
from pandas.core.common import not_none

food = 0
wood = 1
gold = 3
stone = 2
special_case = 2
special_case_2 = 3
special_case_3 = 4
special_case_4 = 5
special_case_5 =6
special_case_6 = 7
special_case_7 = 8
technologie_page_desc_icon = { #Ce dictionnaire est pour les tech qui font office d'ouverture de page, première élément les icônes; deuxièmes les descriptions
    1:[53,"Open the infantry upgrades and allow you to upgrade infantry units"],
    2:[45,"Open the cavalry upgrades and allow you to upgrade cavalry units"],
    3:[54,"Open the archery upgrades and allow you to upgrade ranged units"],
    4:[197,"Open the siege upgrades and allow you to upgrade siege units"],
    5:[210,"Open the economy upgrades and allow you to upgrade villagers and trade"],
    6:[4,"Go back to the technology category"],
}

technology_cost_icon = {
    #ID:[type coûts, quantiter coûts, type coûts 2, quantiter coûts 2, type coûts 3, quantiter resource 3, ICON]
    #--------------------------- Tech infantry
    1: [food, 1900, gold, 2000, Attribute.UNUSED_RESOURCE_010, 2, 44],
    2: [food, 1800, gold, 2500, Attribute.UNUSED_RESOURCE_018, 2, 124],
    3: [stone, 1900, wood, 1200, Attribute.UNUSED_RESOURCE_029, 2, 176],
    4: [gold, 5500, food, 7000, Attribute.UNUSED_RESOURCE_030, 2, 22],
    5: [food, 2000, gold, 1700, Attribute.UNUSED_RESOURCE_031, 2, 114],
    6: [stone, 800, gold, 2500, Attribute.UNUSED_RESOURCE_051, 2, 107],
    7: [wood, 1900, food, 2000, Attribute.UNUSED_RESOURCE_059, 2, 67],
    8: [gold, 2300, food, 1900, Attribute.UNUSED_RESOURCE_060, 2, 91],
    #-------------------------------------------------------------- Tech cavalry
    9:  [gold, 2000, food, 1500, Attribute.UNUSED_RESOURCE_123, 2, 45],
    10: [gold, 2000, food, 1500, Attribute.UNUSED_RESOURCE_061, 2, 23],
    11: [gold, 2300, food, 3000, Attribute.UNUSED_RESOURCE_066, 2, 110],
    12: [gold, 3000, food, 1500, Attribute.UNUSED_RESOURCE_69, 2, 106],
    13: [gold, 4000, food, 2000, Attribute.UNUSED_RESOURCE_70, 2, 114],
    14: [gold, 1800, food, 2300, Attribute.UNUSED_RESOURCE_71, 2, 10],
    15: [gold, 1100, food, 750, Attribute.UNUSED_RESOURCE_72, 2, 19],
    16: [gold, 1800, stone, 600, Attribute.UNUSED_RESOURCE_73, 2, 91],
    #--------------------------------------------------------------- Tech Archery and GUN
    17: [gold, 5000, food, 3500, Attribute.UNUSED_RESOURCE_74, 2, 35],
    18: [wood, 3000, food, 2300, Attribute.UNUSED_RESOURCE_75, 2, 112],
    19: [gold, 5500, food, 3000, Attribute.UNUSED_RESOURCE_76, 2, 124],
    20: [gold, 3000, wood, 3500, Attribute.UNUSED_RESOURCE_102, 2, 37],
    21: [gold, 2000, food, 2000, Attribute.UNUSED_RESOURCE_103, 2, 8],
    22: [gold, 4500, food, 3500, Attribute.UNUSED_RESOURCE_104, 2, 52],
    23: [gold, 2300, food, 2000, Attribute.UNUSED_RESOURCE_105, 2, 91],
    #--------------------------------------------------------------- # Siege
    24: [gold, 5000, food, 3500, Attribute.UNUSED_RESOURCE_106, 2, 18],
    25: [wood, 3000, food, 2300, Attribute.UNUSED_RESOURCE_107, 2, 126],
    26: [gold, 5500, food, 3000, Attribute.UNUSED_RESOURCE_108, 2, 220],
    27: [gold, 3000, wood, 3500, Attribute.UNUSED_RESOURCE_109, 2, 107],
    28: [gold, 2000, food, 2000, Attribute.UNUSED_RESOURCE_110, 2, 25],
    29: [gold, 4500, food, 3500, Attribute.UNUSED_RESOURCE_111, 2, 86],
    30: [gold, 2300, food, 2000, Attribute.UNUSED_RESOURCE_112, 2, 100],
    31: [gold, 4800, food, 3200, Attribute.UNUSED_RESOURCE_113, 2, 60],
    #-------------------------- Eco / villagers
    32: [gold, 2800, food, 1800, Attribute.UNUSED_RESOURCE_114, 2, 58],
    33: [gold, 2000, food, 1650, Attribute.UNUSED_RESOURCE_115, 2, 79],
    34: [gold, 7500, food, 6000, Attribute.UNUSED_RESOURCE_116, 2, 113],
    35: [gold, 6700, food, 5500, Attribute.UNUSED_RESOURCE_117, 2, 3],
    36: [wood, 2200, food, 2200, Attribute.UNUSED_RESOURCE_118, 2, 212],
    37: [gold, 4500, stone, 800, Attribute.UNUSED_RESOURCE_119, 2, 92],
}


Techno_xs = {
100: ("void Script_XS_{s}_{u}_{player}() {{" #TRUE OR FALSE CASE
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
    "}}"
        ),
101: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL_CASE
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
    "}}"
        ),
102: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL CASE 2
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS_3}, {player});"
    "}}"
        ),
103: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL CASE 3
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS_3}, {player});"
      
        "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute_2}, {valeur_XS_2}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute_2}, {valeur_XS_3}, {player});"
    "}}" ),

104: ("void Script_XS_{s}_{u}_{player}() {{" # Special CASE 4
        "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_2}, {attribute_2}, {valeur_XS}, {player});"
      
      "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS}, {player});"
    "}}"
        ),
105: ("void Script_XS_{s}_{u}_{player}() {{" # Special CASE 4
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur_2}, {unit_ID_2}, {attribute_2}, {valeur_XS_2}, {player});"
    "}}"
        ),
106: ("void Script_XS_{s}_{u}_{player}() {{"
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID}, {attribute_3}, {valeur_XS}, {player});"
      
    "}}"
        ),
107: ("void Script_XS_{s}_{u}_{player}() {{"  # SPECIAL CASE 6
          "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS_3}, {player});"
      
          "xsEffectAmount({operateur_2}, {unit_ID_4}, {attribute}, {valeur_XS_4}, {player});"
          "xsEffectAmount({operateur_2}, {unit_ID_5}, {attribute}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_6}, {attribute}, {valeur_XS_4}, {player});"

          "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_2}, {attribute_2}, {valeur_XS_2}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_3}, {attribute_2}, {valeur_XS_3}, {player});"
      
          "xsEffectAmount({operateur_2}, {unit_ID_4}, {attribute_2}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_5}, {attribute_2}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_6}, {attribute_2}, {valeur_XS_4}, {player});"
      
         "xsEffectAmount({operateur}, {unit_ID_4}, {attribute_3}, {valeur_XS_5}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_5}, {attribute_3}, {valeur_XS_5}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_6}, {attribute_3}, {valeur_XS_5}, {player});"
          "}}"),
108: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL CASE 2
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS}, {player});"
      
        "xsEffectAmount({operateur_2}, {unit_ID_4}, {attribute}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_5}, {attribute}, {valeur_XS_4}, {player});"
       "xsEffectAmount({operateur_2}, {unit_ID_6}, {attribute}, {valeur_XS_4}, {player});"
      
      "xsEffectAmount({operateur}, {unit_ID_4}, {attribute_2}, {valeur_XS_5}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_5}, {attribute_2}, {valeur_XS_5}, {player});"
       "xsEffectAmount({operateur}, {unit_ID_6}, {attribute_2}, {valeur_XS_5}, {player});"
    "}}"
        ),
#["cAddAttribute",904,,,],
    # Amélioration infantrie
    1: ["cAddAttribute", 906, 9, "256*4 + 4", False],  # Infantrie attaque upgrade
    2: ["cAddAttribute", 906, 0, 20, False],           # Amélioration HP
    3: ["cMulAttribute", 906, 10, 0.90, False],        # Vitesse d'attaque
    4: ["cAddAttribute", 906, 8, "256*4 + 2", True, 906, "256*3 + 2"],  # Armure
    5: ["cAddAttribute", 906, 109, 20, False],         # Régénération des PV
    6: ["cAddAttribute", 906, 22, 0.20, False],        # Radius
    7: ["cMulAttribute", 906, 5, 1.15, False],         # Vitesse de déplacement
    8: ["cMulAttribute", 906, 101, 0.85, False],       # Temps d'entrainement
    # Amélioration cavalerie
    9:  ["cAddAttribute", 912, 9, "256*4 + 2", False,],  # Attaque
    10: ["cAddAttribute", 912, 8, "256*4 + 3", True, 912, "256*3 + 3"],  # Armure (duplicata renommé)
    11: ["cMulAttribute", 912, 0, 1.20, False],        # Point de vie
    12: ["cAddAttribute", 912, 12, 0.50, False],       # Portée maximale
    13: ["cAddAttribute", 912, 109, 30, False],        # Régénération PV
    14: ["cMulAttribute", 912, 5, 1.10, False],        # Vitesse de déplacement
    15: ["cAddAttribute", 912, 22, 0.60, False],        # Radius
    16: ["cMulAttribute", 912, 101, 0.90, False],      # Temps d'entrainement

    # Archer tech
    17: ["cAddAttribute", 900, 9, "256 * 3 + 2", special_case, 936, "256 * 3 + 2", 944, "256 * 3 + 2"],
    18: ["cMulAttribute", 900, 10, 0.85, special_case, 936, 0.85, 944, 0.85],
    19: ["cAddAttribute", 900, 0, 10, special_case, 936, 10, 944, 10],
    20: ["cAddAttribute", 900, 12, 2, special_case_2, 936, 2, 944, 2, 1],
    21: ["cAddAttribute", 900, 22, 0.10, special_case, 936, 0.10, 944, 0.10],
    22: ["cAddAttribute", 900, 102, 2, special_case_2, 936, 2, 944, 2, 107],
    23: ["cMulAttribute", 900, 101, 0.90, special_case, 936, 0.90, 944, 0.90],
    # Siege upgrade
    24: ["cAddAttribute", 955, 9, "256 * 3 + 2", special_case, 913, "256 * 4 + 2", 954, "256 * 3 + 2"], #Damage siege
    25: ["cMulAttribute", 913, 10, 0.85, special_case, 954, 0.85, 955, 0.85], # Reload time
    26: ["cMulAttribute", 913, 5, 1.15, special_case, 42, 1.15, 955, 1.15], # Move speed
    27: ["cMulAttribute", 42, 13, 1.15, False], # Temps de déploiement trebs
    28: ["cAddAttribute", 913, 12, 1, special_case_7, 954, 1, 955, 1, 1258, 422, 548, "cSetAttribute", 0, 8, "256*4 + 1"], #Max range et armure pour bélier
    29: ["cMulAttribute", 913, 22, 1.10, special_case, 954, 1.10, 955, 1.10], # AOE
    30: ["cAddAttribute", 913, 102, 1, special_case_6, 954, 1, 955, 1, 107, 1258, 422, 548, 0, 0, 235, "cSetAttribute"], # Nombre de projectile + PV
    31: ["cMulAttribute", 913, 101, 0.90, special_case, 42, 0.10, 955, 0.90], # Temps de construction
    # Eco tech
    32: ["cMulAttribute", 904, 13, 1.15, False],
    33: ["cMulAttribute", 904, 5, 1.10, special_case_4, "cAddAttribute", 904, 0, 10],
    34: ["cMulAttribute", 919, 13, 1.30, False],
    35: ["cModResource", 251, "cAttributeAdd", 15, special_case, 252, 15, 253, 15],
    36: ["cAddAttribute", 904, None, None, None],
    37: ["cAddAttribute", 904, None, None, None],
}

Techno_message = {
    #----------------- Tech infantry
    1: "Upgrade infantry damage <cost>.\n Give +4 damages to your infantries units.\nYou can make this upgrade 3 times.",
    2: "Upgrade infantry hitpoint <cost>.\n Give +20 hitpoints to your infantries units.\nYou can make this upgrade 3 times.",
    3: "Upgrade infantry attack speed <cost>\n Infantries attack 10% faster.\nYou can make this upgrade 3 times.",
    4: "Upgrade infantry armor <cost>\n Give +2 armor and piercing armor to your infantries units.\nYou can make this upgrade 3 times.",
    5: "Upgrade infantry health regeneration <cost>.\n Infantry heal +20 hp per minutes.\nYou can make this upgrade 3 times.",
    6: "Upgrade infantry radius attack <cost>.\n Infantry gain 0.20 radius attack.\nYou can make this upgrade 3 times.",
    7: "Upgrade infantry movement speed <cost>.\nInfantry move 15% faster\nYou can make this upgrade 3 times.",
    8: "Reduce the training time of infantry units <cost>.\n Infantry units (Unique units included) are produced 10% faster.\nYou can make this upgrade 3 times.",
    #-----------------------------------------------------------
    9:  "Upgrade cavalry attack <cost>.\n Give +2 attacks to your cavalry units (elephant included)\nYou can make this upgrade 3 times.",
    10: "Upgrade cavalry armor <cost>.\n Give +3 armors and piercing armor to cavalry units (elephant included)\nYou can make this upgrade 3 times.",
    11: "Upgrade cavalry hitpoints <cost>.\n Cavalry units gain 20% hitpoints (elephant included).\nYou can make this upgrade 3 times.",
    12: "Upgrade cavalry attack range <cost>.\n Give 0.50 range to cavalry attack (elephant included)\nYou can make this upgrade 3 times.",
    13: "Upgrade cavalry regeneration <cost>.\n Cavalry Heal 30 HP per minutes(elephant included).\nYou can make this upgrade 3 times.",
    14: "Upgrade cavalry movement speed <cost>.\n Cavalry move 10% faster(elephant included)\nYou can make this upgrade 3 times.",
    15: "Upgrade cavalry line of sight <cost>.\n Cavalry gain 0.60 attack radius (elephant included)\nYou can make this upgrade 3 times.",
    16: "Reduce the training time of cavalry units\nCavalry units are trained 10% faster (elephant and unique units included).\nYou can make this upgrade 3 times.",
    #---------------------------------------------------------------------------------------------------------------------------------------------
    17: "Upgrade ranged units damage <cost>.\nGive +2 attacks to every range units\nYou can make this upgrade 3 times.",
    18: "Upgrade ranged units attack speed <cost>.\nRanged units attack 15% faster.\nYou can make this upgrade 3 times.",
    19: "Upgrade ranged units hitpoints <cost>\nRanged units gain +10 HP.\nYou can make this upgrade 3 times.",
    20: "Upgrade ranged units range <cost>\nRanged units gain +2 range and line of sight\nYou can make this upgrade 3 times.",
    21: "Upgrade ranged units attack radius <cost>\nRanged units gain 0.10 radius attack.\nYou can make this upgrade 3 times.",
    22: "Give +2 projectile to ranged units <cost>.\nRanged units gain +2 projectile.\nYou can make this upgrade 3 times.",
    23: "Reduce ranged units training time <cost>\nRanged units (unique units included) are train 10% faster.\nYou can make this upgrade 3 times.",
    #---------------------------------------------------------------------------------------------------------------------------------------------
    24: "Upgrade siege attack <cost>\n Give +2 attacks to every siege units.\nYou can make this upgrade 3 times.",
    25: "Upgrade siege attack speed <cost>\n Siege weapon attack 15% faster.\nYou can make this upgrade 3 times.",
    26: "Upgrade siege movement speed <cost>\n Siege weapon move 15% faster.\nYou can make this upgrade 3 times.",
    27: "Upgrade trebuchet unpack speed <cost>\n Trebuchet unpack 15% faster.\nYou can make this upgrade 3 times.",
    28: "Upgrade siege ranged and ram HP <cost>\n Sieges weapons gain +1 range except rams who gain +1 melee armor instead .\nYou can make this upgrade 3 times.",
    29: "Upgrade siege blast <cost>\nSiege weapons gain +10% blastwidth.\nYou can make this upgrade 3 times.",
    30: "Give +1 projectile to siege weapons <cost>\nSiege weapons gain +1 projectile except rams who gain 235 HP instead.\nYou can make this upgrade 3 times.",
    31: "Reduce siege construction time <cost>\nSiege weapon are builded 10% faster(Unique units included).\nYou can make this upgrade 3 times.",
    #---------------------------------------------------------------------------------------------------------------------------------------------
    32: "Upgrade villager workrate <cost>.\nVillager gather and build 15% faster.\nYou can make this upgrade 3 times.",
    33: "Ugrade villager speed and Hitpoints <cost>\nVillager move 10% faster and gain +10 hitpoints.\nYou can make this upgrade 3 times.",
    34: "Upgrade trade cart workrate <cost>\nTrade cart carry +30% gold.\nYou can make this upgrade 3 times.",
    35: "Upgrade trade cart resource carrying <cost>.\nTrade cart bring back 15%(calculated on the total gold) food, stone and wood after each trip.\nYou can make this upgrade 3 times.",
    36: "Upgrade population headroom <cost>\n You gain +50 population headroom.\nYou can make this upgrade 3 times.",
    37: "Upgrade relic gold generation <cost>\nYour relics gold production is doubled, also the first time you reserach this, you unlock the possibility to create relics inside monastery.\nYou can make this upgrade 3 times."
}

###########################################################################################################################################################################################################################################
#
#
#
#
#
#                                                                   Séparation, la suite c'est le TRADE WORKSHOP
#                                                                   Separation, next part is the TRADE WORKSHOP
#
#
#
#
#
###########################################################################################################################################################################################################################################

Trade_workshop_placeholder_tech = {
    1:[TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID,"Exchange a point for 500 food.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab",124],
    2:[TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID,"Exchange a point for 500 wood.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab",70],
    3:[TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID,"Exchange a point for 500 gold.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab",3],
    4:[TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID,"Exchange a point for 500 stone.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab",88],
    5:[TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,"Upgrade the trade workshop to tier 2 <cost>.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab",105],
}

Trigger_Trade_workshop = {
    1:["Exchange 1 ticket for 500 food {player}",0,1,Attribute.UNUSED_RESOURCE_121,food,500,TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID],
    2:["Exchange 1 tickets for 500 wood {player}",0,1,Attribute.UNUSED_RESOURCE_121,wood,500,TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID],
    3:["Exchange 1 tickets for 500 gold {player}",0,1,Attribute.UNUSED_RESOURCE_121,gold,500,TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID],
    4:["Exchange 1 tickets for 500 stone {player}",0,1,Attribute.UNUSED_RESOURCE_121,stone,500,TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID],
    5: ["Exchange 1 ticket for 1000 food {player}", 1,2, Attribute.UNUSED_RESOURCE_121, food, 1000,TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID],
    6: ["Exchange 1 tickets for 1000 wood {player}", 1,2, Attribute.UNUSED_RESOURCE_121, wood, 1000,TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID],
    7: ["Exchange 1 tickets for 1000 gold {player}", 1,2, Attribute.UNUSED_RESOURCE_121, gold, 1000,TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID],
    8: ["Exchange 1 tickets for 1000 stone {player}", 1, 2, Attribute.UNUSED_RESOURCE_121, stone, 1000,TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID],
    9: ["Exchange 1 ticket for 1500 food {player}", 2, 3, Attribute.UNUSED_RESOURCE_121, food, 1500,TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID],
    10: ["Exchange 1 tickets for 1500 wood {player}", 2, 3, Attribute.UNUSED_RESOURCE_121, wood, 1500,TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID],
    11: ["Exchange 1 tickets for 1500 gold {player}", 2, 3, Attribute.UNUSED_RESOURCE_121, gold, 1500,TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID],
    12: ["Exchange 1 tickets for 1500 stone {player}", 2, 3, Attribute.UNUSED_RESOURCE_121, stone, 1500,TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID],
    13: ["Exchange 1 ticket for 2500 food {player}", 3, 4, Attribute.UNUSED_RESOURCE_121, food, 2500,TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID],
    14: ["Exchange 1 tickets for 2500 wood {player}", 3, 4, Attribute.UNUSED_RESOURCE_121, wood, 2500,TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID],
    15: ["Exchange 1 tickets for 2500 gold {player}", 3, 4, Attribute.UNUSED_RESOURCE_121, gold, 2500,TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID],
    16: ["Exchange 1 tickets for 2500 stone {player}", 3, 4, Attribute.UNUSED_RESOURCE_121, stone, 2500,TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID],
    17: ["Exchange 1 ticket for 4000 food {player}", 4, 5, Attribute.UNUSED_RESOURCE_121, food, 4000,TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID],
    18: ["Exchange 1 tickets for 4000 wood {player}", 4, 5, Attribute.UNUSED_RESOURCE_121, wood, 4000,TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID],
    19: ["Exchange 1 tickets for 4000 gold {player}", 4, 5, Attribute.UNUSED_RESOURCE_121, gold, 4000,TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID],
    20: ["Exchange 1 tickets for 4000 stone {player}", 4, 5, Attribute.UNUSED_RESOURCE_121, stone, 4000,TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID],
    21: ["Exchange 1 ticket for 6000 food {player}", 5, 6, Attribute.UNUSED_RESOURCE_121, food, 6000,TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID],
    22: ["Exchange 1 tickets for 6000 wood {player}", 5, 6, Attribute.UNUSED_RESOURCE_121, wood, 6000,TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID],
    23: ["Exchange 1 tickets for 6000 gold {player}", 5, 6, Attribute.UNUSED_RESOURCE_121, gold, 6000,TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID],
    24: ["Exchange 1 tickets for 6000 stone {player}", 5, 6, Attribute.UNUSED_RESOURCE_121, stone, 6000,TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID],
}
Trigger_Trade_workshop_upgrade = {
    1:["Upgrade trade workshop {player}",Attribute.UNUSED_RESOURCE_121,0,1],
    2:["Upgrade trade workshop {player}",Attribute.UNUSED_RESOURCE_121,1,2],
    3:["Upgrade trade workshop {player}",Attribute.UNUSED_RESOURCE_121,2,3],
    4:["Upgrade trade workshop {player}",Attribute.UNUSED_RESOURCE_121,3,4],
    5:["Upgrade trade workshop {player}",Attribute.UNUSED_RESOURCE_121,4,5],
}


Trade_workshop_upgrade_msg = {
    1:[TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID,"Exchange a point for 1000 food.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    2:[TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID,"Exchange a point for 1000 wood.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    3:[TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID,"Exchange a point for 1000 gold.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    4:[TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID,"Exchange a point for 1000 stone.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    5:[TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,"Upgrade the trade workshop to tier 3 <cost>.\nExchanging a point will now give you 1500 resource...",food,2200,gold,1500,None,None],
    6: [TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID,"Exchange a point for 1500 food.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    7: [TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID,"Exchange a point for 1500 wood.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    8: [TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID,"Exchange a point for 1500 gold.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    9: [TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID,"Exchange a point for 1500 stone.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    10: [TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,"Upgrade the trade workshop to tier 4 <cost>.\nExchanging a point will now give you 2500 resource...\nAlso you will gain points every 3 minutes instead of 3:30 minutes",food,5000,gold,2700,None,None],
    11: [TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID,"Exchange a point for 2500 food.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    12: [TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID,"Exchange a point for 2500 wood.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    13: [TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID,"Exchange a point for 2500 gold.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    14: [TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID,"Exchange a point for 2500 stone.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    15: [TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,"Upgrade the trade workshop to tier 5 <cost>.\nExchanging a point will now give you 4000 resource...",food,7500,wood,7500,stone,2000],
    16: [TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID,"Exchange a point for 4000 food.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    17: [TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID,"Exchange a point for 4000 wood.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    18: [TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID,"Exchange a point for 4000 gold.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    19: [TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID,"Exchange a point for 4000 stone.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    20: [TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,"Upgrade the trade workshop to tier 6 <cost>.\nExchanging a point will now give you 6000 resource...\nAlso you will receive a ticket every 2:30 minutes instead of 3 minutes",food,10000,gold,10000,stone,1000],
    21: [TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID,"Exchange a point for 6000 food.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    22: [TechInfo.TECHNOLOGY_PLACEHOLDER_02.ID,"Exchange a point for 6000 wood.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    23: [TechInfo.TECHNOLOGY_PLACEHOLDER_03.ID,"Exchange a point for 6000 gold.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    24: [TechInfo.TECHNOLOGY_PLACEHOLDER_04.ID,"Exchange a point for 6000 stone.\nYou gain points by killing enemy units or waiting...\nPoints are displayed in the objective tab"],
    25: [TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,None,None,None,None,None,None,None],
}

Kill_reward = {
    1: [200,350,  500,  600,  750,1000,1150,1350, 1500, 1750,2000,2250,2500, 2800,3000, 3500, 4000, 4500, 5000],# Nombre de kill
    2: [300,500,False,False,650,700,False,1000,False,False,1000,1200,False,1500,1700,False,False,False,False], # food
    3: [False,False,400,500,False,False,500,False,False,800,1100,False,1100,False,False,2000,2000,False,False], # wood
    4: [300,300,  400,  550,  False, 900, 1000, False, False, False, False, 1200, False,1400, 1400, False, False, 1600, 1600], # stone
    5: [150,150,200,250,500,False,800,900,False,1000, 1100, False, False, 1600, 1700, False, False, 1900, 2100], # gold
    6: [False,False,False,False,1,False,1,1,5,False,False,2,2,False,3,False,5,False,10] # tickets
}

Demon_tech = {
    1:["Fight me {player}",TechInfo.DARK_AGE.ID,TechInfo.FEUDAL_AGE.ID,HeroInfo.ZAWISZA_THE_BLACK.ID,food,450,wood,300,Attribute.UNUSED_RESOURCE_130,1,
       "Town-center challenge <cost>\n You win another packed town-center and special upgrades for tower at your blackmist, but you must fight 10 enemies unit...",
       "Town-center challenge <cost>. You gain a packed town-center, you fight 10 enemies units..."],
    2:["Malay + Khmer {player}",TechInfo.FEUDAL_AGE.ID,TechInfo.CASTLE_AGE.ID,HeroInfo.ZAKARE.ID,None,None,None,None,Attribute.UNUSED_RESOURCE_131,1,
       "Challenge of the car <cost>\n You win the farm bonus of the Khmers and the fast and upgrade of the Malay but you must fight the mighty cobra car",
       "Challenge of the car <cost>. You win Khmer farming bonus and malay age upgrade, you fight a cobra car..."],
    3:["You are FIRED {player}",TechInfo.CASTLE_AGE.ID,TechInfo.IMPERIAL_AGE.ID,HeroInfo.YURY.ID,food,1500,gold,800,Attribute.UNUSED_RESOURCE_132,1,
       "You are FIRED <cost>\n All your villager will gain triple collection and construction speed but they will all die...",
       "You are FIRED <cost>.All villager triple gathering and building speed, they will all die too"],
    4:["Woman vs CRYPTO {player}",TechInfo.IMPERIAL_AGE.ID,None,HeroInfo.YODIT.ID,None,None,None,None,Attribute.UNUSED_RESOURCE_133,1,
       "Woman vs CRYPTO <cost>\n Your trade cart bring back 3 times more gold...\nHowever you have to fight Jagwiga and Tamar which are able to summon units",
       "Woman vs CRYPTO <cost>. Trade cart bring back more gold... You must fight Jagwiga and Tamar"]
}

Boss_unit_spawn = {
    1:[UnitInfo.HUSSAR.ID,UnitInfo.HEAVY_PIKEMAN.ID],
    2:[UnitInfo.HUSSAR.ID,UnitInfo.HEAVY_PIKEMAN.ID],
    3:[UnitInfo.HEAVY_CAVALRY_ARCHER.ID,UnitInfo.CAVALIER.ID],
    4:[UnitInfo.HEAVY_CAVALRY_ARCHER.ID,UnitInfo.HEAVY_CAMEL_RIDER.ID],
    5:[UnitInfo.ELITE_SKIRMISHER.ID,UnitInfo.ARAMBAI.ID],
    6:[UnitInfo.ELITE_SKIRMISHER.ID,UnitInfo.ARAMBAI.ID],
    7:[UnitInfo.HAND_CANNONEER.ID,UnitInfo.JANISSARY.ID],
    8:[UnitInfo.CHAMPION.ID,UnitInfo.ELITE_EAGLE_WARRIOR.ID],
    9:[UnitInfo.ELITE_WOAD_RAIDER.ID,UnitInfo.CHAMPION.ID],
    10:[UnitInfo.ELITE_BERSERK.ID,UnitInfo.KONNIK_DISMOUNTED.ID],
}

Tower_upgrade_stat = {
    1:[ObjectAttribute.HIT_POINTS,2,Operation.MULTIPLY],
    2:[ObjectAttribute.ATTACK,6,Operation.ADD],
    3:[ObjectAttribute.TOTAL_MISSILES,4,Operation.ADD,ObjectAttribute.MAX_TOTAL_MISSILES,4,Operation.ADD],
    4:[ObjectAttribute.TRAIN_TIME,2,Operation.DIVIDE],
    5:[ObjectAttribute.STONE_COSTS,95,Operation.SET],
}

Tower_upgrade_cost_desc = {
    1:[food,800,gold,800,"Research Construction improvement <cost>\n Watch towers lines and donjon double their hitpoint",103],
    2:[stone,1000,wood,950,"Research tower re-design <cost>\n Watch towers lines and donjon gain +6 attacks",119],
    3:[stone,1250,gold,950,"Research firing improvement <cost>\n Watch tower lines and donjon shoot 4 additional arrows",204],
    4:[food,800, gold,400,"Research defence engineering <cost>\n Watch towers are build 2 times faster",60],
    5:[food,7000,wood,6500,"Research new resource study <cost>\n Watch towers lines and donjon have a stone cost set at 95",172]
}

Potion = {

}
