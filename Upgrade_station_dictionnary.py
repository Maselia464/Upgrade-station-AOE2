#Ceci est le dictionnaire de la station d'amélioration,
from email.headerregistry import UniqueUnstructuredHeader

from AoE2ScenarioParser.datasets.trigger_lists import Attribute

food = 0
wood = 1
gold = 3
stone = 2
special_case = 2
special_case_2 = 3
special_case_3 = 4
special_case_4 = 5
special_case_5 =6
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
    1:[food,1900,gold,2000,Attribute.UNUSED_RESOURCE_010,1,44],
    2:[food,1800,gold,2500,Attribute.UNUSED_RESOURCE_018,1,124],
    3:[stone,1900,wood,1200,Attribute.UNUSED_RESOURCE_029,1,176],
    4:[gold,5500,food,7000,Attribute.UNUSED_RESOURCE_030,1,22],
    5:[food,2000,gold,1700,Attribute.UNUSED_RESOURCE_031,1,114],
    6:[stone,800,gold,2500,Attribute.UNUSED_RESOURCE_051,1,107],
    7:[wood, 1900,food,2000,Attribute.UNUSED_RESOURCE_059,1,67],
    8:[gold,2300,food,1900,Attribute.UNUSED_RESOURCE_060,1,91],
#-------------------------------------------------------------- Tech cavalry
    9:[gold,2000,food,1500,Attribute.UNUSED_RESOURCE_061,1,23],
    10:[gold,2300,food,3000,Attribute.UNUSED_RESOURCE_066,1,110],
    11:[gold,3000,food,1500,Attribute.UNUSED_RESOURCE_69,1,106],
    12:[gold,4000,food,2000,Attribute.UNUSED_RESOURCE_70,1,114],
    13:[gold,1800,food,2300,Attribute.UNUSED_RESOURCE_71,1,10],
    14:[gold,1100,food,750,Attribute.UNUSED_RESOURCE_72,1,19],
    15:[gold,1800,stone,600,Attribute.UNUSED_RESOURCE_73,1,91],
#--------------------------------------------------------------- Tech Archery and GUN
    16:[gold,5000,food,3500,Attribute.UNUSED_RESOURCE_74,1,35],
    17:[wood,3000,food,2300,Attribute.UNUSED_RESOURCE_75,1,112],
    18:[gold,5500,food,3000,Attribute.UNUSED_RESOURCE_76,1,124],
    19:[gold,3000,wood,3500,Attribute.UNUSED_RESOURCE_102,1,37],
    20:[gold,2000,food,2000,Attribute.UNUSED_RESOURCE_103,1,8],
    21:[gold,4500,food,3500,Attribute.UNUSED_RESOURCE_104,1,52],
    22:[gold,2300,food,2000,Attribute.UNUSED_RESOURCE_105,1,91],
#--------------------------------------------------------------- # Siege
    23: [gold, 5000, food, 3500, Attribute.UNUSED_RESOURCE_106, 1, 18],
    24: [wood, 3000, food, 2300, Attribute.UNUSED_RESOURCE_107, 1, 126],
    25: [gold, 5500, food, 3000, Attribute.UNUSED_RESOURCE_108, 1, 220],
    26: [gold, 3000, wood, 3500, Attribute.UNUSED_RESOURCE_109, 1, 107],
    27: [gold, 2000, food, 2000, Attribute.UNUSED_RESOURCE_110, 1, 25],
    28: [gold, 4500, food, 3500, Attribute.UNUSED_RESOURCE_111, 1, 86],
    29: [gold, 2300, food, 2000, Attribute.UNUSED_RESOURCE_112, 1, 100],
    30: [gold, 4800, food, 3200, Attribute.UNUSED_RESOURCE_113, 1, 60],
#--------------------------
    31: [gold, 2800, food, 1800, Attribute.UNUSED_RESOURCE_114, 1, 58],
    32: [gold, 2000, food, 1650, Attribute.UNUSED_RESOURCE_115, 1, 79],
    33: [gold, 7500, food, 6000, Attribute.UNUSED_RESOURCE_116, 1, 113],
    34: [gold, 6700, food, 5500, Attribute.UNUSED_RESOURCE_117, 1, 3],
    #35: [gold, 10000, stone, 8500, Attribute.UNUSED_RESOURCE_117, 1, 4],
    35: [wood, 2200, food, 2200, Attribute.UNUSED_RESOURCE_118, 1, 212],
    36: [gold, 4500, stone, 800, Attribute.UNUSED_RESOURCE_119, 1, 92],
#------------------------------------------------------------------------ # Villageois

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
#["cAddAttribute",904,,,],
#Amélioration infantrie
    1: ["cAddAttribute",906,9,"256*4 + 3",False], #Infantrie attaque upgrade
    2: ["cAddAttribute",906,0,15,False], #Amélioration HP
    3: ["cMulAttribute",906,10,0.90,False], # Vitesse d'attaque
    4: ["cAddAttribute",906,8,"256*4 + 2",True,906,"256*3 + 2"], #Armure
    5: ["cAddAttribute",906,109,20,False], # Régénération des PV
    6: ["cAddAttribute",906,22,0.20,False], # Radius
    7: ["cMulAttribute",906,5,1.15,False], #Vitesse de déplacement
    8: ["cMulAttribute",906,101,0.85,False], #Temps d'entrainement
#Amélioration cavalerie
    9: ["cAddAttribute",912,8,"256*4 + 3",True,912,"256*3 + 3"], #Armure
    10:["cMulAttribute",912,0,1.20,False], #Point de vie
    11:["cAddAttribute",912,12,0.50,False], # Portée maximal
    12:["cAddAttribute",912,109,30,False], #Régénaration de PV
    13:["cMulAttribute",912,5,1.10,False], #Vitesse de déplacement
    14:["cAddAttribute",912,1,1.30,False], #Ligne de mire
    15:["cMulAttribute",912,101,0.90,False], #Temps d'entrainement
#Archer tech
    16:["cAddAttribute",900,9,"256 * 3 + 2",special_case,936,"256 * 3 + 2",944,"256 * 3 + 2"], #Attaque
    17:["cMulAttribute",900,10,0.85,special_case,936,0.85,944,0.85], #Vitesse d'attaque
    18:["cAddAttribute",900,0,10,special_case,936,10,944,10], #Point de vie
    19:["cAddAttribute",900,12,2,special_case_2,936,2,944,2,1], #Portée maximal
    20:["cAddAttribute",900,22,0.10,special_case,936,0.10,944,0.10], #Radius
    21:["cAddAttribute",900,102,2,special_case_2,936,2,944,2,107], #Nombre de missile
    22:["cMulAttribute",900,101,0.90,special_case,936,0.90,944,0.90], #Temps d'entrainement
#Siege upgrade
    23:["cAddAttribute",955,9,"256 * 3 + 2",special_case,913,"256 * 4 + 2",954,"256 * 3 + 2"], #Attaque siège
    24:["cMulAttribute",913,10,0.85,special_case,954,0.85,955,0.85],#Vitesse d'attaque
    25:["cMulAttribute",913,5,1.15,special_case,42,1.15,955,1.15], #Vitesse de déplacement
    26:["cMulAttribute",42,13,1.15,False], #Vitesse de déploiement
    27:["cAddAttribute",913,12,1,special_case,954,1,955,1], #Portée
    28:["cMulAttribute",913,22,1.10,special_case,954,1.10,955,1.10],#Radius
    29:["cAddAttribute",913,102,1,special_case_2,954,1,955,1,107],#Nombre missile
    30:["cMulAttribute",913,101,0.10,special_case,42,0.10,955,0.10], #Vitesse de construction
#Eco tech
    31: ["cMulAttribute", 904, 13, 1.15, False], #Vitesse de collecte et de construction
    32: ["cMulAttribute", 904, 5, 1.10, special_case_4,"cAddAttribute",904,0,10], #PV et vitesse de déplacement
    33: ["cMulAttribute", 919, 13, 1.30, False], #Trade cart fournisse plus d'or
    34: ["cModResource", 251, "cAttributeAdd", 15, special_case,252,15,253,15], #Trade cart ressource dans le trade
    #35: ["cSetAttribute", 919, 3, 0, special_case_5,4,22], #Pas de colission trade cart
    35: ["cAddAttribute", 904, None, None, None],
    36: ["cAddAttribute", 904, None, None, None],
}

Techno_message= {
#----------------- Tech infantry
    1:"Upgrade infantry damage <cost>.\n Give +3 damages to your infantries units.\nYou can make this upgrade 3 times.",
    2:"Upgrade infantry hitpoint <cost>.\n Give +15 hitpoints to your infantries units.\nYou can make this upgrade 3 times.",
    3:"Upgrade infantry attack speed <cost>\n Infantries attack 10% faster.\nYou can make this upgrade 3 times.",
    4:"Upgrade infantry armor <cost>\n Give +2 armor and piercing armor to your infantries units.\nYou can make this upgrade 3 times.",
    5:"Upgrade infantry health regeneration <cost>.\n Infantry heal +20 hp per minutes.\nYou can make this upgrade 3 times.",
    6:"Upgrade infantry radius attack <cost>.\n Infantry gain 0.20 radius attack.\nYou can make this upgrade 3 times.",
    7:"Upgrade infantry movement speed <cost>.\nInfantry move 0.15 faster\nYou can make this upgrade 3 times.",
    8:"Reduce the training time of infantry units <cost>.\n Infantry units (Unique units included) are produced 10% faster.\nYou can make this upgrade 3 times.",
#-----------------------------------------------------------
    9:"Upgrade cavalry armor <cost>.\n Give +3 armors and piercing armor to cavalry units (elephant included)\nYou can make this upgrade 3 times.",
    10:"Upgrade cavalry hitpoints <cost>.\n Cavalry units gain %20 hitpoints (elephant included).\nYou can make this upgrade 3 times.",
    11:"Upgrade cavalry attack range <cost>.\n Give 0.50 range to cavalry attack (elephant included)\nYou can make this upgrade 3 times.",
    12:"Upgrade cavalry regeneration <cost>.\n Cavalry Heal 30 HP per minutes(elephant included).\nYou can make this upgrade 3 times.",
    13:"Upgrade cavalry movement speed <cost>.\n Cavalry move 10% faster(elephant included)\nYou can make this upgrade 3 times.",
    14:"Upgrade cavalry line of sight <cost>.\n Cavalry gain 30% line of sight (elephant included)\nYou can make this upgrade 3 times.",
    15:"Reduce the training time of cavalry units\nCavalry units are trained 10% faster (elephant and unique units included).\nYou can make this upgrade 3 times.",
#---------------------------------------------------------------------------------------------------------------------------------------------
16: "Upgrade ranged units damage <cost>.\nGive +2 attacks to every range units\nYou can make this upgrade 3 times.",
17: "Upgrade ranged units attack speed <cost>.\nRanged units attack 15% faster.\nYou can make this upgrade 3 times.",
18: "Upgrade ranged units hitpoints <cost>\nRanged units gain +10 HP.\nYou can make this upgrade 3 times.",
19: "Upgrade ranged units range <cost>\nRanged units gain +2 range and line of sight\nYou can make this upgrade 3 times.",
20: "Upgrade ranged units attack radius <cost>\nRanged units gain 0.10 radius attack.\nYou can make this upgrade 3 times.",
21: "Give +2 projectile to ranged units <cost>.\nRanged units gain +2 projectile.\nYou can make this upgrade 3 times.",
22: "Reduce ranged units training time <cost>\nRanged units (unique units included) are train 10% faster.\nYou can make this upgrade 3 times.",
#---------------------------------------------------------------------------------------------------------------------------------------------
23: "Upgrade siege attack <cost>\n Give +2 attacks to every siege units.\nYou can make this upgrade 3 times.",
24: "Upgrade siege attack speed <cost>\n Siege weapon attack 15% faster.\nYou can make this upgrade 3 times.",
25: "Upgrade siege movement speed <cost>\n Siege weapon move 15% faster.\nYou can make this upgrade 3 times.",
26: "Upgrade trebuchet unpack speed <cost>\n Trebuchet unpack 15% faster.\nYou can make this upgrade 3 times.",
27: "Upgrade siege ranged <cost>\n Sieges weapons gain +1 range.\nYou can make this upgrade 3 times.",
28: "Upgrade siege blast <cost>\nSiege weapons gain +10% blastwidth.\nYou can make this upgrade 3 times.",
29: "Give +1 projectile to siege weapons <cost>\nSiege weapons gain +1 projectile.\nYou can make this upgrade 3 times.",
30: "Reduce siege construction time <cost>\nSiege weapon are builded 10% faster(Unique units included).\nYou can make this upgrade 3 times.",
#---------------------------------------------------------------------------------------------------------------------------------------------
31: "Upgrade villager workrate <cost>.\nVillager gather and build 15% faster.\nYou can make this upgrade 3 times.",
32: "Ugrade villager speed and Hitpoints <cost>\nVillager move 10% faster and gain +10 hitpoints.\nYou can make this upgrade 3 times.",
33: "Upgrade trade cart workrate <cost>\nTrade cart carry +30% gold.\nYou can make this upgrade 3 times.",
34: "Upgrade trade cart resource carrying <cost>.\nTrade cart bring back 15%(calculated on the total gold) food, stone and wood after each trip.\nYou can make this upgrade 3 times.",
35: "Upgrade population headroom <cost>\n You gain +50 population headroom.\nYou can make this upgrade 3 times.",
36: "Upgrade relic gold generation <cost>\nYour relics gold production is doubled, also the first time you reserach this, you unlock the possibility to create relics inside monastery.\nYou can make this upgrade 3 times."
#37:
}
