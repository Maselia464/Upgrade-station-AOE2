from email.headerregistry import UniqueUnstructuredHeader
from gc import enable
from idlelib.rpc import objecttable
from pickle import FALSE

from AoE2ScenarioParser.datasets.effects import attributes
from AoE2ScenarioParser.objects.support import area
from numpy.f2py.crackfortran import sourcecodeform
from packaging.markers import Operator



start_value = 0
from logging import disable
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
# Information of unit/building/hero and tech IDs
from AoE2ScenarioParser.datasets.projectiles import ProjectileInfo
from AoE2ScenarioParser.datasets.object_support import Civilization, StartingAge
from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
# Information about player IDs
from AoE2ScenarioParser.datasets.players import PlayerId, PlayerColorId, ColorId
from AoE2ScenarioParser import scenarios
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
# Information about terrain IDs
from AoE2ScenarioParser.datasets.terrains import TerrainId

from AoE2ScenarioParser.datasets.trigger_lists import \
    DiplomacyState, Operation, ButtonLocation, PanelLocation, \
    TimeUnit, VisibilityState, DifficultyLevel, TechnologyState, \
    Comparison, ObjectAttribute, Attribute, UnitAIAction, \
    AttackStance, ObjectType, ObjectClass, DamageClass, \
    HeroStatusFlag, Hotkey, BlastLevel, TerrainRestrictions, \
    ColorMood, ObjectState, SecondaryGameMode, ChargeType, \
    ChargeEvent, CombatAbility, FogVisibility, GarrisonType, \
    OcclusionMode, ProjectileHitMode, ProjectileVanishMode, \
    UnitTrait, ProjectileSmartMode, Age, ActionType, VictoryTimerType

from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.support import area
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.objects.managers.message_manager import MessageManager

from AoE2ScenarioParser.objects.support.area import Area
from AoE2ScenarioParser.scenarios.support.data_triggers import DataTriggers

from AoE2ScenarioParser.objects.managers.option_manager import OptionManager

from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from pyexpat.errors import messages
from unicodedata import category
#Dictionnaire pour le script
from Upgrade_station_dictionnary import technologie_page_desc_icon, technology_cost_icon, special_case_3, special_case_7
from Upgrade_station_dictionnary import Techno_message
from Upgrade_station_dictionnary import Techno_xs
from Upgrade_station_dictionnary import Trade_workshop_placeholder_tech
from Upgrade_station_dictionnary import  Trigger_Trade_workshop
from Upgrade_station_dictionnary import  Trade_workshop_upgrade_msg
from Upgrade_station_dictionnary import  Trigger_Trade_workshop_upgrade
from Upgrade_station_dictionnary import  Demon_tech
from Upgrade_station_dictionnary import  Kill_reward
from Upgrade_station_dictionnary import  Boss_unit_spawn
from Upgrade_station_dictionnary import  Tower_upgrade_stat
from Upgrade_station_dictionnary import  Tower_upgrade_cost_desc
from AoE2ScenarioParser.objects.support.area import Area


Liste_joueur = {
    1: PlayerId.ONE,
    2: PlayerId.TWO,
    3: PlayerId.THREE,
    4: PlayerId.FOUR,
    5: PlayerId.FIVE,
    6: PlayerId.SIX,
    7:PlayerId.SEVEN,
    8:PlayerId.EIGHT
}

Lister_couleur = {
    1: "BLUE",
    2: "RED",
    3: "GREEN",
    4: "YELLOW",
    5: "AQUA",
    6: "PURPLE",
    7: "GRAY",
    8: "ORANGE",
}
input_path = "C:\\Users\\redma\\Games\\Age of Empires 2 DE\\76561198382316787\\resources\\_common\\scenario\\7v1 Orrax Maselia Hard Assault V4.0.2.BUILD.aoe2scenario"
output_path = "C:\\Users\\redma\\Games\\Age of Empires 2 DE\\76561198382316787\\resources\\_common\\scenario\\7v1 Orrax Maselia Hard Assault V4.0.3 BETA.aoe2scenario"



# Lecture et écriture du scénario
scenario = AoE2DEScenario.from_file(input_path)
trigger_manager = scenario.trigger_manager
fonction_remove = 0
# Accéder au gestionnaire de carte
map_manager = scenario.map_manager

# Obtenir la taille de la carte
map_size = map_manager.map_size
#---------------------------------------------------------------------
if fonction_remove == 0:
    trigger_remove_first = "-----Start_Plugin------"
    last_ID_for_reset_name = "-----end_Plugin------"
    trigger_id_first = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_first), None)
    trigger_id_last = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == last_ID_for_reset_name), None)
    trigger_id_last = trigger_id_last + 1
    liste_longue = list(range(trigger_id_first, trigger_id_last))
    trigger_manager.remove_triggers(liste_longue)

Header = trigger_manager.add_trigger( #Start of the plugin
            name=f"-----Start_Plugin------",
            enabled=False,
            looping=False,
        )
scenario_uuid = scenario.uuid
area = Area.from_uuid(scenario_uuid)
################################################ Special rule############################
timer_quantity_1 = 5
Script_rule = "void rule_for_friendly_fire() {"
for p in range (1,8):
    player=Liste_joueur[p]
    Script_rule +=f"xsEffectAmount(cSetAttribute, 900, 44, 4, {player});"
    Script_rule += f"xsEffectAmount(cSetAttribute, 936, 44, 4, {player});"
    Script_rule += f"xsEffectAmount(cSetAttribute, 944, 44, 4, {player});"
Script_rule += "}"

Balancing = trigger_manager.add_trigger(
            name=f"Equilibrage archer et cannonier",
            enabled=True,
            looping=False,
)
Balancing.new_condition.timer(
    timer=timer_quantity_1,
)
Balancing.new_effect.script_call(
    message=Script_rule,
)
################################################# RELIC tech ##############################
for u in range (1,8):
        quantity_number_1 = 1
        quantity_number_2 = 2500
        quantity_number_3 = 26
        cost_1 = 3
        button_location_v = 10
        player = Liste_joueur[u]
        # Fonction changer le cheval en relique gaia
        relic_buy1= trigger_manager.add_trigger(
            name=f"Première activation {player}",
            enabled=False,
            looping=False,
        )
        relic_buy2 = trigger_manager.add_trigger(
            name=f"Cheval en relique gaia {player}",
            enabled=True,
            looping=True,
        )
        # Fonction enlever le trigger de changement cheval en gaia
        relic_buy3 = trigger_manager.add_trigger(
            name=f"Enlever le trigger de changement cheval en gaia {player}",
            enabled=False,
            looping=True,
        )
        # Variable utilisé par Fonction Relique
        trigger_remove_second = f"Cheval en relique gaia {player}"
        trigger_remove_third = f"Enlever le trigger de changement cheval en gaia {player}"
        trigger_id_second = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_second), None)
        trigger_id_third = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_third), None)
        # Acheter RELIQUE
        # Conditon de Fonction de Création de Cheval pour Relique
        relic_buy1.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.HORSE_A.ID,
            enabled=True,
        )
        relic_buy1.new_effect.change_train_location(
            object_list_unit_id=UnitInfo.HORSE_A.ID,
            object_list_unit_id_2=BuildingInfo.MONASTERY.ID,
            source_player=player,
            button_location=button_location_v,
        )
        relic_buy1.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=UnitInfo.HORSE_A.ID,
            object_attributes=ObjectAttribute.ICON_ID,
            quantity=quantity_number_3,
            operation=Operation.SET,
        )
        relic_buy1.new_effect.change_object_cost(
            resource_1=cost_1,
            resource_1_quantity=quantity_number_2,
            source_player=player,
            object_list_unit_id=UnitInfo.HORSE_A.ID,
        )
        relic_buy2.new_condition.objects_in_area(
            object_list=UnitInfo.HORSE_A.ID,  # Cheval A
            source_player=player,
            **area.select_entire_map().to_dict(),
            # fonction pour sélectionner toute la carte, fonctionne avec tous les effets et condition qui ont besoin d'avoir une selection
            quantity=quantity_number_1,
        )
        relic_buy2.new_effect.change_ownership(
            object_list_unit_id=UnitInfo.HORSE_A.ID,  # cheval A
            source_player=player,
            target_player=PlayerId.GAIA,
            **area.select_entire_map().to_dict(),
            # fonction pour sélectionner toute la carte, fonctionne avec tous les effets et condition qui ont besoin d'avoir une selection
        )
        relic_buy2.new_effect.activate_trigger(
            trigger_id=trigger_id_third,
        )
        relic_buy3.new_condition.timer(
            timer=quantity_number_1,
        )
        relic_buy3.new_effect.replace_object(
            object_list_unit_id=UnitInfo.HORSE_A.ID,  # cheval A
            source_player=PlayerId.GAIA,
            **area.select_entire_map().to_dict(),
            # fonction pour sélectionner toute la carte, fonctionne avec tous les effets et condition qui ont besoin d'avoir une selection
             object_list_unit_id_2=OtherInfo.RELIC.ID,  # Relique Gaia
        )
        relic_buy3.new_effect.deactivate_trigger(
            trigger_id=trigger_id_third,
        )
###########################################################################################

Autorisation_tech = {}
bouton_techno = ["None",7,8,11,12,13,15]
for u in range (1,7):
    for p in range (1,8):
        quantity_number_1 = 0
        quantity_number_2= 1
        player = Liste_joueur[p]
        tech_obj = getattr(TechInfo, f"BLANK_TECHNOLOGY_{u}")  # <-- OK ici
        tech_id = tech_obj.ID
        bouton_placement = bouton_techno[u]
        print(f"Tech ID {u} = {tech_id}")
######################################################################################################
#############################-Cette partie gère les tech qui font office de page######################
######################################################################################################
        Autorisation_tech[u] = trigger_manager.add_trigger(
            name=f"Activation des technologies pour changer de page {u}",
            enabled=True,
            looping=False,
        )
        if u != 6: #Ici on à besoin que la tech 6 qui fait office de retour arrière reste innactive
            Autorisation_tech[u].new_effect.enable_disable_technology(
                source_player=player,
                enabled=True,
                technology=tech_id,
            )
        else:
            Autorisation_tech[u].new_effect.enable_disable_technology(
                source_player=player,
                enabled=False,
                technology=tech_id,
            )
        Autorisation_tech[u].new_effect.change_technology_location(
            source_player=player,
            button_location=bouton_placement,
            object_list_unit_id_2=BuildingInfo.WONDER.ID,
            technology=tech_id,
        )
        Autorisation_tech[u].new_effect.change_technology_icon(
            source_player=player,
            technology=tech_id,
            quantity=technologie_page_desc_icon[u][quantity_number_1]
        )
        Autorisation_tech[u].new_effect.change_technology_description(
            source_player=player,
            technology=tech_id,
            message=technologie_page_desc_icon[u][quantity_number_2]
        )
#Il faut faire une vérification des techs qui ajoute 1 valeur variable pour déterminer les technologies
Recherche_check = {} #Check la tech qui est rechercher
for u in range (1,7):
    for p in range (1,8):
        player = Liste_joueur[p]
        if u != 6:
            quantity = u
            vrai_ou_faux = False #Tant qu'on arrive pas à la tech qui gère le changement de page, on désactive les autres tech au moment de la recherche.
            vrai_ou_faux_2 = True
        else:
            quantity = 0
            vrai_ou_faux = True #Quand on arrive à la tech qui fait le retour arrière alors on réactive les technologies de page.
            vrai_ou_faux_2 = False
        tech_obj = getattr(TechInfo, f"BLANK_TECHNOLOGY_{u}")  # <-- OK ici
        tech_id = tech_obj.ID
        Recherche_check[u] = trigger_manager.add_trigger(
            name=f"Vérifie la techno {tech_id} pour {player}",
            enabled=True,
            looping=True,
        )
        Recherche_check[u].new_condition.research_technology(
            technology=tech_id,
            source_player=player,
        )
        Recherche_check[u].new_effect.modify_resource(
            quantity=quantity,
            operation=Operation.SET,
            source_player=player,
            tribute_list=Attribute.UNUSED_RESOURCE_008,
        )
        for d in range(1, 7):  # Désactivation des techno
            tech_obj_2 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{d}")  # <-- OK ici
            tech_id_2 = tech_obj_2.ID
            if d != 6:
                Recherche_check[u].new_effect.enable_disable_technology(
                    technology=tech_id_2,
                    enabled=vrai_ou_faux,
                    source_player=player,
                )
            else:
                Recherche_check[u].new_effect.enable_disable_technology(
                    technology=tech_id_2,
                    enabled=vrai_ou_faux_2,
                    source_player=player,
                )


#Ensuite il faut catégoriser les techs par valeur variable
Les_tech = {}
for u in range (1,6):
    c = u + 1
    quantity_number_25 = 0
    quantity_number_26 = 1
    if u == 1:
        min_boucle = 1
        maxi_boucle = 9
    elif u == 2:
        min_boucle = 9
        maxi_boucle = 17
    elif u == 3:
        min_boucle = 17
        maxi_boucle = 24
    elif u == 4:
        min_boucle = 24
        maxi_boucle = 32
    else:
        min_boucle = 32
        maxi_boucle = 38
    for p in range (1,8):
        player = Liste_joueur[p]
        Les_tech[u] = trigger_manager.add_trigger(  # End of the plugin
            name=f"Pour les technologies {u} joueur {player}",
            enabled=True,
            looping=True,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity= u,
            inverted=False,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_008,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity=c,
            inverted=True,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_008,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity=quantity_number_25,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_498,
            inverted=False,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity=quantity_number_26,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_498,
            inverted=True,
        )
        comptage = 0
        for s in range (min_boucle,maxi_boucle):
            comptage = comptage + 1
            y = comptage + 6
            l = s - 1
            tech_obj = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # <-- OK ici
            tech_id = tech_obj.ID
            quantity_number_1 = 0
            quantity_number_2 = 1
            quantity_number_3 = 2
            quantity_number_4 = 3
            quantity_number_5 = 4
            quantity_number_6 = 5
            quantity_number_7 = 6
            Les_tech[u].new_effect.enable_disable_technology(
                enabled=True,
                technology=tech_id,
                source_player=player,
            )
            Les_tech[u].new_effect.change_technology_location(
                source_player=player,
                button_location=comptage,
                object_list_unit_id_2=BuildingInfo.WONDER.ID,
                technology=tech_id,
            )
            Les_tech[u].new_effect.change_technology_description(
                source_player=player,
                technology=tech_id,
                message=Techno_message[s],
            )
            Les_tech[u].new_effect.change_technology_cost(
                technology=tech_id,
                source_player=player,
#---------------- Type de coûts
                resource_1=technology_cost_icon[s][quantity_number_1],
                resource_2=technology_cost_icon[s][quantity_number_3],
                resource_3=technology_cost_icon[s][quantity_number_5],
#----------------- Quantité des coûts
                resource_1_quantity=technology_cost_icon[s][quantity_number_2],
                resource_2_quantity=technology_cost_icon[s][quantity_number_4],
                resource_3_quantity=technology_cost_icon[s][quantity_number_6],
#----------------- Resource non utilisée pour limiter l'upgrade
            )
            Les_tech[u].new_effect.change_technology_icon(
                source_player=player,
                technology=tech_id,
                quantity=technology_cost_icon[s][quantity_number_7],
            )
        Les_tech[u].new_effect.modify_resource(
            tribute_list=Attribute.UNUSED_RESOURCE_498,
            quantity=quantity_number_26,
            source_player=player,
            operation=Operation.SET

        )
###############################################################################################################
#                                                                                                             #
#                                                                                                             #
#                                    Séparation pour la lecture                                               #
#                                    On passe aux conditions de chaque tech                                   #
#                                                                                                             #
#                                                                                                             #
###############################################################################################################
        comptage = 0
        check_tech = {}
        for s in range(min_boucle, maxi_boucle):
            comptage = comptage + 1
            y = comptage + 6
            quantity_number_7 = 0
            quantity_number_8 = 1
            quantity_number_9 = 2
            quantity_number_10 = 3
            quantity_number_11 = 4
            quantity_number_12 = 5
            quantity_number_13 = 6
            quantity_number_14 = 101
            quantity_number_15 = 100
            quantity_number_16 = 102
            quantity_number_17 = 7
            quantity_number_18 = 8
            quantity_number_19 = 9
            quantity_number_20 = 103
            quantity_number_21 = 104
            quantity_number_22= 105
            quantity_number_23 = 106
            quantity_number_24 = 50
            quantity_number_107 = 107
            quantity_number_30 = 10
            quantity_number_31 = 11
            quantity_number_32 = 12
            quantity_number_33 = 13
            quantity_number_34 = 14
            quantity_number_35 = 15
            quantity_number_36 = 16
            quantity_number_108 = 108
            quantity_number_true = Techno_xs[s][quantity_number_11]
            if_true = 1
            special_case= 2
            special_case_2= 3
            special_case_3 = 4
            special_case_4 =5
            special_case_5 =6
            special_case_6 = 7
            special_case_7 = 8
            tech_obj_2 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # <-- OK ici
            tech_id_2 = tech_obj_2.ID
            print(quantity_number_true)
            if quantity_number_true == if_true :
                Script_XS = Techno_xs[quantity_number_14].format(s=s, u=u, player=player,operateur=Techno_xs[s][quantity_number_7],unit_ID_2=Techno_xs[s][quantity_number_12],unit_ID=Techno_xs[s][quantity_number_8],attribute=Techno_xs[s][quantity_number_9],valeur_XS=Techno_xs[s][quantity_number_10],valeur_XS_2=Techno_xs[s][quantity_number_13])
            elif quantity_number_true == special_case:
                Script_XS = Techno_xs[quantity_number_16].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS_3=Techno_xs[s][quantity_number_18])
            elif quantity_number_true == special_case_2:
                Script_XS = Techno_xs[quantity_number_20].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_19],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS_3=Techno_xs[s][quantity_number_18])
# -----------------------------------------------------------------------------------------------------------------
            elif quantity_number_true == special_case_3:
                Script_XS = Techno_xs[quantity_number_21].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10])
# -----------------------------------------------------------------------------------------------------------------
            elif quantity_number_true == special_case_4:
                Script_XS = Techno_xs[quantity_number_22].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 operateur_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_13],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_17],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_18])
#-----------------------------------------------------------------------------------------------------------------
            elif quantity_number_true == special_case_5:
                Script_XS = Techno_xs[quantity_number_23].format(s=s, u=u, player=player,# ICI !!!!!!!!!!
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_12],
                                                                 attribute_3=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],)
            elif quantity_number_true == special_case_6:
                Script_XS = Techno_xs[quantity_number_107].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 operateur_2=Techno_xs[s][quantity_number_36],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],
                                                                 unit_ID_4=Techno_xs[s][quantity_number_30],
                                                                 unit_ID_5=Techno_xs[s][quantity_number_31],
                                                                 unit_ID_6=Techno_xs[s][quantity_number_32],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_19],
                                                                 attribute_3=Techno_xs[s][quantity_number_34],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS_3=Techno_xs[s][quantity_number_18],
                                                                 valeur_XS_4=Techno_xs[s][quantity_number_33],
                                                                 valeur_XS_5=Techno_xs[s][quantity_number_35],)
            elif quantity_number_true == special_case_7:
                Script_XS = Techno_xs[quantity_number_108].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 operateur_2=Techno_xs[s][quantity_number_32],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],

                                                                 unit_ID_4=Techno_xs[s][quantity_number_19],
                                                                 unit_ID_5=Techno_xs[s][quantity_number_30],
                                                                 unit_ID_6=Techno_xs[s][quantity_number_31],

                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_34],

                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_4=Techno_xs[s][quantity_number_33],
                                                                 valeur_XS_5=Techno_xs[s][quantity_number_35],)
                print(Script_XS)


            else:
                Script_XS = Techno_xs[quantity_number_15].format(s=s,u=u,player=player,operateur=Techno_xs[s][quantity_number_7],unit_ID=Techno_xs[s][quantity_number_8],attribute=Techno_xs[s][quantity_number_9],valeur_XS=Techno_xs[s][quantity_number_10])
            check_tech[y] = trigger_manager.add_trigger(
                name=f"vérifie si la tech à été recherché {tech_id_2}",
                enabled=True,
                looping=True,
            )
            check_tech[y].new_condition.research_technology(
                technology=tech_id_2,
                source_player=player,
            )
            check_tech[y].new_condition.accumulate_attribute(
                quantity=u,
                inverted=False,
                source_player=player,
                attribute=Attribute.UNUSED_RESOURCE_008, #Ceci est la condition qui check les tech ne te fait pas avoir
            )
            check_tech[y].new_condition.accumulate_attribute(
                quantity=c,
                inverted=True,
                source_player=player,
                attribute=Attribute.UNUSED_RESOURCE_008,
            )
            if s not in [36,37]:
                check_tech[y].new_effect.script_call(
                    message=Script_XS,
                )
            elif s == 36:
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.POPULATION_HEADROOM,
                    source_player=player,
                    quantity=quantity_number_24,
                    operation=Operation.ADD,
                )
            else:
                trigger_remove_first = f"Première activation {player}"
                trigger_id_first = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_first),None)
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.RELIC_GOLD_PRODUCTION_RATE,
                    source_player=player,
                    quantity=quantity_number_9,
                    operation=Operation.MULTIPLY,
                )
                check_tech[y].new_effect.activate_trigger(
                    trigger_id=trigger_id_first,
                )
            check_tech[y].new_effect.enable_disable_technology(
                technology=tech_id_2,
                source_player=player,
                enabled=True,
            )

Retour_0 = {}
for p in range (1,8):
    player = Liste_joueur[p]
    quantity_number_1 = 1
    quantity_number_2 = 0
    Retour_0[p] = trigger_manager.add_trigger(
        name="Désactivation des triggers",
        enabled=True,
        looping=True,
    )
    Retour_0[p].new_condition.accumulate_attribute(
        quantity=quantity_number_2,
        source_player=player,
        attribute=Attribute.UNUSED_RESOURCE_008,
        inverted=False,
    )
    Retour_0[p].new_condition.accumulate_attribute(
        quantity=quantity_number_1,
        source_player=player,
        attribute=Attribute.UNUSED_RESOURCE_008,
        inverted=True,
    )
    Retour_0[p].new_effect.modify_resource(
        tribute_list=Attribute.UNUSED_RESOURCE_498,
        quantity=quantity_number_2,
        source_player=player,
        operation=Operation.SET
    )
    for y in range (7,15):
        tech_obj_3 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # Faire une double conditio, check 1 en inver et 0,et désact les tech de 7 à 16
        tech_id_3 = tech_obj_3.ID
        vrai_ou_faux_2 = False
        Retour_0[p].new_effect.enable_disable_technology(
            technology=tech_id_3,
            enabled=False,
            source_player=player,
        )
###########################################################################################################################################################################################################################################
#
#
#
#
#
#                                                                   Séparation, la suite c'est le Attribution ressource
#
#
#
#
#
###########################################################################################################################################################################################################################################
#---------------------------- ATTRIBUTION DES RESSOURCES POUR LES TECHNOLOGIES

for chinese_check in range (1,3):
    for p in range (1,8):
        if chinese_check == 1:
            true_false = True
            quantity_number_3 = 6
            quantity_number_1_real = 2
        else:
            true_false = False
            quantity_number_3 = 3
            quantity_number_1_real = 1
        player=Liste_joueur[p]
        color=Lister_couleur[p]
        quantity_number_1 = 4
        quantity_number_2 = 2


        quantity_number_2250 = 2250
        attribution_resource_pour_tech = trigger_manager.add_trigger(
            name=f"Attribution des resources pour tech {player}",
            enabled=True,
            looping=False,
        )
        attribution_resource_pour_tech.new_condition.technology_state(
            source_player=player,
            technology=TechInfo.CHINESE.ID,
            quantity=TechnologyState.DONE,
            inverted=true_false,
        )
        for y in range (1,38):
            attribution_resource_pour_tech.new_effect.modify_resource(
                tribute_list=technology_cost_icon[y][quantity_number_1],
                source_player=player,
                quantity=quantity_number_3,
                operation=Operation.SET,
            )
        attribution_resource_pour_tech_2250 = trigger_manager.add_trigger(
            name=f"Attribution des resources pour tech {player}",
            enabled=True,
            looping=False,
        )
        attribution_resource_pour_tech_2250.new_condition.accumulate_attribute(
            source_player=player,
            attribute=Attribute.UNITS_KILLED,
            quantity= quantity_number_2250,
        )
        attribution_resource_pour_tech_2250.new_condition.technology_state(
            source_player=player,
            technology=TechInfo.CHINESE.ID,
            quantity=TechnologyState.DONE,
            inverted=true_false,
        )
        attribution_resource_pour_tech_2250.new_effect.display_instructions(
            object_list_unit_id=UnitInfo.MONK.ID,
            instruction_panel_position=quantity_number_2,
            message=f"<{color}>Player {player} has reached 2250 kill ! Reward: All the tech at the wonder can be researched a fourth time !",
            sound_name="Play_m2i"
        )
        for m in range(1, 38):
            attribution_resource_pour_tech_2250.new_effect.modify_resource(
                tribute_list=technology_cost_icon[m][quantity_number_1],
                source_player=player,
                quantity=quantity_number_1_real,
                operation=Operation.ADD,
            )
    #---------------------------- ATTRIBUTION DES RESSOURCES POUR LES TECHNOLOGIES
for p in range (1,8):
    player =Liste_joueur[p]
    quantity_number_1 = 1
    check_wonder = trigger_manager.add_trigger(
        name=f"Vérification merveille",
        enabled = True,
        looping=False,
    )
    check_wonder.new_condition.objects_in_area(
        source_player=player,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
        object_list=BuildingInfo.WONDER.ID,
        object_state=ObjectState.ALIVE,
        inverted=False,
    )
    check_wonder.new_effect.modify_resource(
        source_player=player,
        tribute_list=Attribute.UNUSED_RESOURCE_122,
        quantity=quantity_number_1,
        operation=Operation.SET,
    )
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
quantity_number_20 = 20
quantity_number_19 = 19
quantity_number_1000 = 1000
display_table = trigger_manager.add_trigger(
        name=f"display table text",
        enabled = True,
        looping=False,
    )
display_table_2 = trigger_manager.add_trigger(
        name=f"display table text 2",
        enabled = True,
        looping=False,
    )
display_table.new_condition.accumulate_attribute(
        source_player=PlayerId.EIGHT,
        attribute=Attribute.UNUSED_RESOURCE_359,
        quantity=quantity_number_1000,
        inverted=False,
    )
display_table_2.new_condition.accumulate_attribute(
        source_player=PlayerId.EIGHT,
        attribute=Attribute.UNUSED_RESOURCE_359,
        quantity=quantity_number_1000,
        inverted=False,
    )
display_table.short_description = str(f"7vs1 Upgrade station statistic, build wonder, make upgrade and kick enemy ass ")
display_table_2.short_description = str(f"|KILL|POINTS|WONDER|")
display_table.display_on_screen = True
display_table_2.display_on_screen = True
display_table.description_order = quantity_number_20
display_table_2.description_order = quantity_number_19
display_obj = 19
for p in range (1,8):
    player = Liste_joueur[p]
    quantity_number_1 = 1
    timer_quantity_1 = 210
    timer_quantity_2 = 180
    timer_quantity_3 = 150
    timer_3min30 = trigger_manager.add_trigger(
            name=f"3 minutes and 30 seconds timer for res{player}",
            enabled = True,
            looping=True,
    )
    timer_3min30.new_condition.objects_in_area(
        source_player=player,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
        object_list=BuildingInfo.TRADE_WORKSHOP.ID,
        object_state=ObjectState.ALIVE,
    )
    timer_3min30.new_condition.timer(
        timer=timer_quantity_1,
    )
    timer_3min30.new_effect.modify_resource(
        quantity=quantity_number_1,
        operation=Operation.ADD,
        source_player=player,
        tribute_list=Attribute.UNUSED_RESOURCE_120,
    )
    timer_3min = trigger_manager.add_trigger(
        name=f"3 minutes for res {player}",
        enabled=False,
        looping=True,
    )
    timer_3min.new_condition.objects_in_area(
        source_player=player,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
        object_list=BuildingInfo.TRADE_WORKSHOP.ID,
        object_state=ObjectState.ALIVE,
    )
    timer_3min.new_condition.timer(
        timer=timer_quantity_2,
    )
    timer_3min.new_effect.modify_resource(
        quantity=quantity_number_1,
        operation=Operation.ADD,
        source_player=player,
        tribute_list=Attribute.UNUSED_RESOURCE_120,
    )
    timer_2min30 = trigger_manager.add_trigger(
        name=f"2 minutes and 30 sec for res {player}",
        enabled=False,
        looping=True,
    )
    timer_2min30.new_condition.objects_in_area(
        source_player=player,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
        object_list=BuildingInfo.TRADE_WORKSHOP.ID,
        object_state=ObjectState.ALIVE,
    )
    timer_2min30.new_condition.timer(
        timer=timer_quantity_3,
    )
    timer_2min30.new_effect.modify_resource(
        quantity=quantity_number_1,
        operation=Operation.ADD,
        source_player=player,
        tribute_list=Attribute.UNUSED_RESOURCE_120,
)
timer_quantity = 80 #570
timer_quantity_2= 20
Trade_workshop_unlock_dialog = trigger_manager.add_trigger(
        name=f"Trade workshop unlock",
        enabled = True,
)
Trade_workshop_unlock_dialog.new_condition.timer(
    timer=timer_quantity,
)
Trade_workshop_unlock_dialog.new_effect.display_instructions(
        message="The trade workshop is unlocked, building it will allow you to exchange resources for points, you can build with your villager",
        display_time=timer_quantity_2,
        object_list_unit_id=UnitInfo.MERCHANT.ID,
        sound_name="Play_71714",
)

for p in range (1,8):
    display_obj_result = display_obj - p
    player = Liste_joueur[p]
    quantity_number_1000 = 1000
    affichage = trigger_manager.add_trigger(
        name=f"Affichage pour joueur {player}",
        enabled = True,
    )
    affichage.new_condition.accumulate_attribute(
        source_player=player,
        attribute=Attribute.UNUSED_RESOURCE_359,
        quantity=quantity_number_1000,
        inverted=False,
    )
    affichage.short_description = str(f"P{player}: <Units Killed, {player}> | <Unused Resource 120, {player}> | <Unused Resource 122, {player}>/1 | ")
    affichage.display_on_screen = True
    affichage.description_order = display_obj_result
for chinese_check in range (1,4):
    for p in range (1,8):
        if chinese_check == 1: # Toute les civ sauf china
            true_false = True
            Age_tech = None
        elif chinese_check == 2: # china et dark age
            true_false = False
            Age_tech = TechInfo.DARK_AGE.ID
        else: #China et pas dark age
            true_false= False
            Age_tech = TechInfo.FEUDAL_AGE.ID

        player=Liste_joueur[p]
        timer_quantity = 80 #570
        timer_quantity_2= 20 # Texte de présentation du trade workshop
        timer_quantity_3 = timer_quantity + 10
        button_location_number = 13
        quantity_number_200 = 200
        activation_trade_workshop = trigger_manager.add_trigger(
            name=f"Trade workshop enabling {player}",
            enabled=True,
            looping=False,
        )
        activation_trade_workshop.new_condition.technology_state(
            quantity=TechnologyState.DONE,
            technology=TechInfo.CHINESE.ID,
            inverted=true_false,
            source_player=player,
        )
        if chinese_check != 1:
            activation_trade_workshop.new_condition.technology_state(
                quantity=TechnologyState.DONE,
                technology=Age_tech,
                inverted=False,
                source_player=player,
            )
        activation_trade_workshop.new_condition.timer(
            timer= timer_quantity,
        )
        activation_trade_workshop.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=BuildingInfo.TRADE_WORKSHOP.ID,
            enabled=True,
        )
        activation_trade_workshop.new_effect.modify_attribute(
            source_player=player,
            object_attributes=ObjectAttribute.WORK_RATE,
            object_list_unit_id=BuildingInfo.TRADE_WORKSHOP.ID,
            quantity=quantity_number_200,
            operation=Operation.SET
        )
        activation_trade_workshop.new_effect.change_object_description(
            source_player=player,
            object_list_unit_id=BuildingInfo.TRADE_WORKSHOP.ID,
            message="Build the Trade workshop <cost>\n Allow you to exchange points for resource, you receive a point every 3 minutes and 30 seconds\n upgrading the trade workshop will reduce this time..."
        )
        for vill in range (1,3):
            if vill == 1:
                villageois = UnitInfo.VILLAGER_MALE.ID
            else:
                villageois = UnitInfo.VILLAGER_FEMALE.ID
            activation_trade_workshop.new_effect.change_train_location(
                object_list_unit_id=BuildingInfo.TRADE_WORKSHOP.ID,
                source_player=player,
                button_location=button_location_number,
                object_list_unit_id_2=villageois,
            )
        for t in range (1,6):
            quantity_number_0 = 0
            quantity_number_1 = 1
            quantity_number_2 = 2
            quantity_number_1200 = 1200
            quantity_number_3 = 3
            tech_id=Trade_workshop_placeholder_tech[t][quantity_number_0]
            if t == 5:
                button_location_number = 15
            else:
                button_location_number = t
            activation_trade_workshop.new_effect.enable_disable_technology(
                technology=tech_id,
                source_player=player,
                enabled=True,
            )
            activation_trade_workshop.new_effect.change_technology_location(
                technology=tech_id,
                source_player=player,
                object_list_unit_id_2=BuildingInfo.TRADE_WORKSHOP.ID,
                button_location=button_location_number,
            )
            activation_trade_workshop.new_effect.change_technology_description(
                message=Trade_workshop_placeholder_tech[t][quantity_number_1],
                technology=tech_id,
                source_player=player,
            )
            activation_trade_workshop.new_effect.change_technology_icon(
                technology=tech_id,
                source_player=player,
                quantity=Trade_workshop_placeholder_tech[t][quantity_number_2],
            )
            if t != 5 and chinese_check != 3:
                activation_trade_workshop.new_effect.change_technology_cost(
                    source_player=player,
                    resource_1=Attribute.UNUSED_RESOURCE_120,
                    resource_1_quantity=quantity_number_1,
                    technology=tech_id
                )
            elif t != 5 and chinese_check == 3:
                activation_trade_workshop.new_effect.change_technology_cost(
                    source_player=player,
                    resource_1=Attribute.UNUSED_RESOURCE_120,
                    resource_1_quantity=quantity_number_2,
                    technology=tech_id
                )
            else:
                activation_trade_workshop.new_effect.change_technology_cost(
                    technology=tech_id,
                    source_player=player,
                    resource_1_quantity= quantity_number_1200,
                    resource_1= quantity_number_1,
                    resource_2_quantity=quantity_number_1200,
                    #resource_3_quantity=quantity_number_3,
                )
for p in range (1,8):
    for t in range (1,25):
        player =Liste_joueur[p]
        quantity_number_0 = 0 # Get the trigger name
        quantity_number_1 = 1
        quantity_number_2 = 2
        quantity_number_3 = 3
        quantity_number_4 = 4
        quantity_number_5 = 5
        quantity_number_6 = 6
        technology_name = Trigger_Trade_workshop[t][quantity_number_0]
        trigger_name = Trigger_Trade_workshop[t][quantity_number_0].format(player=player)
        exchange_ticket_for_res = trigger_manager.add_trigger(
            name=trigger_name,
            enabled=True,
            looping=True,
        )
        exchange_ticket_for_res.new_condition.accumulate_attribute(
            source_player=player,
            inverted=False,
            attribute=Trigger_Trade_workshop[t][quantity_number_3],
            quantity=Trigger_Trade_workshop[t][quantity_number_1],
        )
        exchange_ticket_for_res.new_condition.accumulate_attribute(
            source_player=player,
            inverted=True,
            attribute=Trigger_Trade_workshop[t][quantity_number_3],
            quantity=Trigger_Trade_workshop[t][quantity_number_2],
        )
        exchange_ticket_for_res.new_condition.research_technology(
            source_player=player,
            technology=Trigger_Trade_workshop[t][quantity_number_6],
        )
        exchange_ticket_for_res.new_effect.modify_resource(
            source_player=player,
            tribute_list=Trigger_Trade_workshop[t][quantity_number_4],
            quantity=Trigger_Trade_workshop[t][quantity_number_5],
            operation=Operation.ADD,
        )
        exchange_ticket_for_res.new_effect.enable_disable_technology(
            source_player=player,
            technology=Trigger_Trade_workshop[t][quantity_number_6],
            enabled=True,
        )
        # Instead of using the dictionary directly, extract the text


for p in range (1,8):
    player = Liste_joueur[p]
    for y in range (1,6):
        quantity_number_0 = 0
        quantity_number_1 = 1
        quantity_number_2 = 2
        quantity_number_3 = 3
        quantity_number_4 = 4
        quantity_number_5 = 5
        quantity_number_6 = 6
        quantity_number_7 = 7
        quantity_number_10 = 10
        quantity_number_20 = 20
        if y == quantity_number_1:
            min_boucle = 1
            maxi_boucle = 6
            set_value_for_upgrade = 1
            set_boundary_for_upgrade_min = 0
            set_boundary_for_upgrade_max = 1
        elif y == quantity_number_2:
            min_boucle = 6
            maxi_boucle = 11
            set_boundary_for_upgrade_min = 1
            set_boundary_for_upgrade_max = 2
            set_value_for_upgrade = 2
        elif y == quantity_number_3:
            min_boucle = 11
            maxi_boucle = 16
            set_value_for_upgrade = 3
            set_boundary_for_upgrade_min = 2
            set_boundary_for_upgrade_max = 3
        elif y == quantity_number_4:
            min_boucle = 16
            maxi_boucle = 21
            set_value_for_upgrade = 4
            set_boundary_for_upgrade_min = 3
            set_boundary_for_upgrade_max = 4
        else:
            min_boucle = 21
            maxi_boucle = 26
            set_value_for_upgrade = 5
            set_boundary_for_upgrade_min = 4
            set_boundary_for_upgrade_max = 5
        if maxi_boucle != 26:
            change_desc_upgrade_tech = maxi_boucle - 1
        else:
            change_desc_upgrade_tech = 1000
        trigger_name = Trigger_Trade_workshop_upgrade[y][quantity_number_0].format(player=player)
        upgrade_station = trigger_manager.add_trigger(
            name=trigger_name,
            enabled=True,
            looping=False,
        )
        upgrade_station.new_condition.accumulate_attribute(
            source_player=player,
            inverted=False,
            attribute=Trigger_Trade_workshop[y][quantity_number_3],
            quantity=set_boundary_for_upgrade_min,
        )
        upgrade_station.new_condition.accumulate_attribute(
            source_player=player,
            inverted=True,
            attribute=Trigger_Trade_workshop[y][quantity_number_3],
            quantity=set_boundary_for_upgrade_max,
        )
        upgrade_station.new_condition.research_technology(
            source_player=player,
            technology=TechInfo.TECHNOLOGY_PLACEHOLDER_05.ID,
        )
        for h in range (min_boucle,maxi_boucle):
            upgrade_station.new_effect.change_technology_description(
                source_player=player,
                message=Trade_workshop_upgrade_msg[h][quantity_number_1],
                technology=Trade_workshop_upgrade_msg[h][quantity_number_0],
            )
            if h ==  change_desc_upgrade_tech:
                print(f"Index {Trade_workshop_upgrade_msg[h][quantity_number_2]},")
                upgrade_station.new_effect.change_technology_cost(
                    source_player=player,
                    resource_1=Trade_workshop_upgrade_msg[h][quantity_number_2],
                    resource_1_quantity=Trade_workshop_upgrade_msg[h][quantity_number_3],
                    resource_2=Trade_workshop_upgrade_msg[h][quantity_number_4],
                    resource_2_quantity=Trade_workshop_upgrade_msg[h][quantity_number_5],
                    resource_3=Trade_workshop_upgrade_msg[h][quantity_number_6],
                    resource_3_quantity=Trade_workshop_upgrade_msg[h][quantity_number_7],
                    technology=Trade_workshop_upgrade_msg[h][quantity_number_0],
                )
                upgrade_station.new_effect.enable_disable_technology(
                    technology=Trade_workshop_upgrade_msg[h][quantity_number_0],
                    enabled=True,
                    source_player=player,
                )
                if h == quantity_number_10:
                    trigger_remove_first = f"3 minutes and 30 seconds timer for res{player}"
                    trigger_id_first = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_first),None)
                    trigger_activate_first = f"3 minutes for res {player}"
                    trigger_id_second = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_activate_first),None)
                    upgrade_station.new_effect.deactivate_trigger(
                        trigger_id=trigger_id_first,
                    )
                    upgrade_station.new_effect.activate_trigger(
                        trigger_id=trigger_id_second
                    )
                elif h == quantity_number_20:
                    trigger_remove_first = f"3 minutes for res {player}"
                    trigger_id_first = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_first), None)
                    trigger_activate_first = f"2 minutes and 30 sec for res {player}"
                    trigger_id_second = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_activate_first), None)
                    upgrade_station.new_effect.deactivate_trigger(
                        trigger_id=trigger_id_first,
                    )
                    upgrade_station.new_effect.activate_trigger(
                        trigger_id=trigger_id_second
                    )
        upgrade_station.new_effect.modify_resource(
            tribute_list=Trigger_Trade_workshop[y][quantity_number_3],
            quantity=set_value_for_upgrade,
            operation=Operation.SET,
            source_player=player,
        )
#################################################################################################################################################################
#
#
#
#
#                                                                               FIN DE TRADE WORKSHOP
#                                                                           SUITE, TECHNOLOGIE DU DEMON
#
#
#
#
#################################################################################################################################################################
for p in range (1,8):
    player = Liste_joueur[p]
    quantity_number_624 = 624
    quantity_number_10 = 10
    quantity_number_5000 = 5000
    demon_tech_attribut = trigger_manager.add_trigger(
        name=f"Attribut demon tech {player}",
        enabled=True,
        looping=False,
    )
    demon_tech_attribut.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=HeroInfo.CHARLEMAGNE.ID,
        operation=Operation.SET,
        quantity=quantity_number_10,
        object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    )
    two_player = player
    demon_tech_attribut.new_effect.modify_attribute(
        source_player=two_player,
        object_list_unit_id=HeroInfo.JADWIGA.ID,
        operation=Operation.SET,
        quantity=quantity_number_5000,
        object_attributes=ObjectAttribute.HIT_POINTS,
        )
    demon_tech_attribut.new_effect.modify_attribute(
       source_player=two_player,
        object_list_unit_id=HeroInfo.TAMAR.ID,
        operation=Operation.SET,
        quantity=quantity_number_5000,
        object_attributes=ObjectAttribute.HIT_POINTS,
    )
    demon_tech_attribut.new_effect.modify_attribute(
        source_player=two_player,
        object_list_unit_id=HeroInfo.JADWIGA.ID,
        operation=Operation.SET,
        quantity=quantity_number_10,
        object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    )
    demon_tech_attribut.new_effect.modify_attribute(
        source_player=two_player,
        object_list_unit_id=HeroInfo.TAMAR.ID,
        operation=Operation.SET,
        quantity=quantity_number_10,
        object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    )
for p in range (1,8):
    Last_hero = 0
    for DT in range (1,5):
        quantity_number_0 = 0
        quantity_number_1 = 1
        quantity_number_2 = 2
        quantity_number_3 = 3
        #Res 1 and quantity
        quantity_number_4 = 4
        quantity_number_5 = 5
        #Res 2 and quantity
        quantity_number_6 = 6
        quantity_number_7 = 7
        #Res 3 and quantity
        quantity_number_8 = 8
        quantity_number_9 = 9
        #Description tech
        quantity_number_10 = 10
        quantity_number_11 = 11
        quantity_number_14 = 14
        quantity_number_16417 = 16417
        timer_1s = 1
        timer_7s = 7
        player=Liste_joueur[p]
        Nom_de_trigger = Demon_tech[DT][quantity_number_0].format(player=player)
        Tech_du_demon = trigger_manager.add_trigger(
            name=Nom_de_trigger,
            enabled=True,
            looping=False,
        )
        Tech_du_demon.new_condition.research_technology(
            source_player=player,
            technology=Demon_tech[DT][quantity_number_1],
            inverted=False,
        )
        if Demon_tech[DT][quantity_number_2] != TechInfo.IMPERIAL_AGE.ID:
            Tech_du_demon.new_condition.research_technology(
                source_player=player,
                technology=Demon_tech[DT][quantity_number_2],
                inverted=True,
            )
        Tech_du_demon.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=Demon_tech[DT][quantity_number_3],
            enabled=True,
        )

        Tech_du_demon.new_effect.change_train_location(
            source_player=player,
            object_list_unit_id=Demon_tech[DT][quantity_number_3],
            object_list_unit_id_2=BuildingInfo.TOWN_CENTER.ID,
            button_location=quantity_number_14,
        )
        Tech_du_demon.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=Demon_tech[DT][quantity_number_3],
            object_attributes=ObjectAttribute.HOTKEY_ID,
            operation=Operation.SET,
            quantity=quantity_number_16417,
        )

        Tech_du_demon.new_effect.change_object_cost(
            source_player=player,
            object_list_unit_id=Demon_tech[DT][quantity_number_3],
            resource_1=Demon_tech[DT][quantity_number_4],
            resource_1_quantity=Demon_tech[DT][quantity_number_5],
            resource_2=Demon_tech[DT][quantity_number_6],
            resource_2_quantity=Demon_tech[DT][quantity_number_7],
            resource_3=Demon_tech[DT][quantity_number_8],
            resource_3_quantity=Demon_tech[DT][quantity_number_9],
        )
        Tech_du_demon.new_effect.change_object_description(
            source_player=player,
            object_list_unit_id=Demon_tech[DT][quantity_number_3],
            message=Demon_tech[DT][quantity_number_10],
        )
        Tech_du_demon.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=Demon_tech[DT][quantity_number_3],
            message=Demon_tech[DT][quantity_number_11],
            object_attributes=ObjectAttribute.SHORT_DESCRIPTION_ID,
        )
        if Last_hero != quantity_number_0:
            Tech_du_demon.new_effect.enable_disable_object(
                source_player=player,
                object_list_unit_id=Last_hero,
                enabled=False,
            )
        Last_hero=Demon_tech[DT][quantity_number_3]
        Tech_du_demon_action = trigger_manager.add_trigger(
            name=f"Tech du demon action {DT} {player}",
            enabled=True,
            looping=False,
        )
        Tech_du_demon_action.new_condition.objects_in_area(
            source_player=player,
            **area.select_entire_map().to_dict(),
            object_list=Demon_tech[DT][quantity_number_3],
            object_state=ObjectState.ALIVE,
            quantity=quantity_number_1,
        )
#print(f"Demon tech int debug{DT}")

        if DT == 1:
            print("We are inside the IF")
            Tech_du_demon_spawn_unit = trigger_manager.add_trigger(
                name=f"Tech du demon spawn unit A {player}",
                enabled=False,
                looping=False,
            )
            Tech_du_demon_spawn_unit_B = trigger_manager.add_trigger(
                name=f"Tech du demon spawn unit B {player}",
                enabled=False,
                looping=False,
            )
            Tech_du_demon_spawn_unit_C = trigger_manager.add_trigger(
                name=f"Tech du demon spawn unit C {player}",
                enabled=False,
                looping=False,
            )
            Tech_du_demon_spawn_unit_D = trigger_manager.add_trigger(
                name=f"Tech du demon spawn unit D {player}",
                enabled=False,
                looping=False,
            )
            trigger_name_search_first = f"Tech du demon spawn unit B {player}"
            trigger_name_search_second = f"Tech du demon spawn unit C {player}"
            trigger_name_search_thirst = f"Tech du demon spawn unit A {player}"
            trigger_name_search_fourth = f"Tech du demon spawn unit D {player}"
            trigger_id_first = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_first),
                None)
            trigger_id_second = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_second),
                None)
            trigger_id_thirst = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_thirst),
                None)
            trigger_id_fourth = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_fourth),
                None)
            Tech_du_demon_action.new_effect.activate_trigger(
                trigger_id=trigger_id_thirst,
            )
            Tech_du_demon_action.new_effect.create_garrisoned_object(
                source_player=player,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                object_list_unit_id_2=BuildingInfo.TOWN_CENTER_PACKED.ID,
                **area.select_entire_map().to_dict(),
            )
            for tech in range (1,6):
                ID_Value = tech + 5
                if ID_Value != 10:
                    tech_enum = getattr(TechInfo, f"TECHNOLOGY_PLACEHOLDER_0{ID_Value}")
                else:
                    tech_enum = getattr(TechInfo, f"TECHNOLOGY_PLACEHOLDER_{ID_Value}")
                tech_obj = tech_enum.ID
                Tech_du_demon_action.new_effect.enable_disable_technology(
                    source_player=player,
                    technology=tech_obj,
                    enabled=True,
                )
            Tech_du_demon_action.new_effect.remove_object(
                source_player=player,
                object_list_unit_id=HeroInfo.ZAWISZA_THE_BLACK.ID,
                object_state=ObjectState.ALIVE,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_action.new_effect.task_object(
                source_player=player,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                **area.select_entire_map().to_dict(),
                action_type=ActionType.UNLOAD,
            )
################Fonction de spawn
            Tech_du_demon_spawn_unit.new_effect.create_garrisoned_object(
                source_player=player,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                object_list_unit_id_2=HeroInfo.CHARLEMAGNE.ID,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_spawn_unit.new_effect.activate_trigger(
                trigger_id=trigger_id_first,
            )
            Tech_du_demon_spawn_unit.new_effect.change_ownership(
                source_player=player,
                object_list_unit_id=HeroInfo.CHARLEMAGNE.ID,
                target_player=PlayerId.EIGHT,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_spawn_unit_B.new_condition.timer(
                timer = timer_1s,
            )
            Tech_du_demon_spawn_unit_B.new_effect.task_object(
                source_player=player,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                **area.select_entire_map().to_dict(),
                action_type=ActionType.UNLOAD,
            )
            Tech_du_demon_spawn_unit_B.new_effect.activate_trigger(
                trigger_id=trigger_id_second,
            )
            Tech_du_demon_spawn_unit_C.new_condition.timer(
                timer=timer_1s,
            )
            Tech_du_demon_spawn_unit_D.new_condition.timer(
                timer=timer_7s,
            )
            Tech_du_demon_spawn_unit_C.new_effect.activate_trigger(
                trigger_id=trigger_id_fourth,
            )
            Tech_du_demon_spawn_unit_D.new_effect.kill_object(
                source_player=PlayerId.EIGHT,
                **area.select_entire_map().to_dict(),
                object_list_unit_id=HeroInfo.CHARLEMAGNE.ID,
            )
            for m in range(0,10):
                units_1 = UnitInfo.KNIGHT.ID
                units_2 = UnitInfo.MILITIA.ID
                units_3 = UnitInfo.ARCHER.ID
                units_4 = UnitInfo.SKIRMISHER.ID
                units_5 = UnitInfo.SPEARMAN.ID
                Units_loop = [units_1,units_2,units_2,units_2,units_3,units_3,units_4,units_4,units_5,units_5]
                Tech_du_demon_spawn_unit_C.new_effect.create_garrisoned_object(
                    object_list_unit_id=HeroInfo.CHARLEMAGNE.ID,
                    object_list_unit_id_2=Units_loop[m],
                    source_player=PlayerId.EIGHT,
                    **area.select_entire_map().to_dict(),
                )
                if m == 9:
                    Tech_du_demon_spawn_unit_C.new_effect.task_object(
                        object_list_unit_id=HeroInfo.CHARLEMAGNE.ID,
                        source_player=PlayerId.EIGHT,
                        **area.select_entire_map().to_dict(),
                        action_type=ActionType.UNGARRISON,
                    )
                    Tech_du_demon_spawn_unit_C.new_effect.activate_trigger(
                        trigger_id=trigger_id_fourth,
                    )

        if DT == 2:
            timer_quantity_1 = 1
            quantity_number_1 = 1
            Tech_du_demon_feudal_A = trigger_manager.add_trigger(
                name=f"Tech du demon feudal spawn A {player}",
                enabled=False,
                looping=False,
            )
            Tech_du_demon_feudal_B = trigger_manager.add_trigger(
                name=f"Tech du demon feudal spawn B {player}",
                enabled=False,
                looping=False,
            )
            trigger_name_search_first = f"Tech du demon feudal spawn A {player}"
            trigger_id_first = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_first),
                None)
            Tech_du_demon_action.new_effect.remove_object(
                source_player=player,
                object_list_unit_id=HeroInfo.ZAKARE.ID,
                **area.select_entire_map().to_dict()
            )
            Tech_du_demon_action.new_effect.activate_trigger(
                trigger_id=trigger_id_first,
            )
            trigger_name_search_second = f"Tech du demon feudal spawn B {player}"
            trigger_id_second = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_second),None)
            Tech_du_demon_feudal_A.new_effect.task_object(
                source_player=player,
                action_type=ActionType.UNGARRISON,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                **area.select_entire_map().to_dict()
            )
            Tech_du_demon_feudal_A.new_effect.create_garrisoned_object(
                source_player=player,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                object_list_unit_id_2=UnitInfo.COBRA_CAR.ID,
                **area.select_entire_map().to_dict()
            )
            
            Tech_du_demon_feudal_A.new_effect.activate_trigger(
                trigger_id=trigger_id_second,
            )
            Tech_du_demon_feudal_B.new_condition.timer(
                timer=timer_quantity_1,
            )
            Tech_du_demon_feudal_B.new_effect.change_ownership(
                object_list_unit_id=UnitInfo.COBRA_CAR.ID,
                source_player=player,
                target_player=PlayerId.EIGHT,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_feudal_B.new_effect.modify_resource(
                source_player=player,
                tribute_list=Attribute.NO_DROPSITE_FARMERS,
                quantity=quantity_number_1,
            )
            Tech_du_demon_feudal_B.new_effect.task_object(
                source_player=player,
                action_type=ActionType.UNGARRISON,
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                **area.select_entire_map().to_dict()
            )
            for tech_change in range (0,2):
                Techno_to_change = [TechInfo.CASTLE_AGE.ID,TechInfo.IMPERIAL_AGE.ID]
                Time_to_change = [105,124]
                Tech_du_demon_feudal_B.new_effect.change_technology_research_time(
                    source_player=player,
                    technology=Techno_to_change[tech_change],
                    quantity=Time_to_change[tech_change],
                )
        if DT == 3:
            Tech_du_demon_castle = trigger_manager.add_trigger(
                name=f"Tech du demon castle {player}",
                enabled=False,
                looping=False,
            )
            trigger_name_search_first = f"Tech du demon castle {player}"
            trigger_id_first = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_first),
                None)
            Tech_du_demon_action.new_effect.activate_trigger(
                trigger_id=trigger_id_first,
            )
            Tech_du_demon_action.new_effect.remove_object(
                source_player=player,
                object_list_unit_id=HeroInfo.YURY.ID,
                **area.select_entire_map().to_dict()
            )
            for vill in range (0,8):
                quantity_number_3 = 3
                villager_job = [UnitInfo.VILLAGER_MALE_FARMER, UnitInfo.VILLAGER_MALE_HUNTER,
                                UnitInfo.VILLAGER_MALE_BUILDER, UnitInfo.VILLAGER_MALE_STONE_MINER,
                                UnitInfo.VILLAGER_MALE_GOLD_MINER, UnitInfo.VILLAGER_MALE_FISHERMAN,
                                UnitInfo.VILLAGER_MALE_LUMBERJACK, UnitInfo.VILLAGER_MALE_REPAIRER,UnitInfo.VILLAGER_MALE_FORAGER]
                villager_job_2 = [
                                    UnitInfo.VILLAGER_FEMALE_FARMER,
                                    UnitInfo.VILLAGER_FEMALE_HUNTER,
                                    UnitInfo.VILLAGER_FEMALE_BUILDER,
                                    UnitInfo.VILLAGER_FEMALE_STONE_MINER,
                                    UnitInfo.VILLAGER_FEMALE_GOLD_MINER,
                                    UnitInfo.VILLAGER_FEMALE_FISHERMAN,
                                    UnitInfo.VILLAGER_FEMALE_LUMBERJACK,
                                    UnitInfo.VILLAGER_FEMALE_REPAIRER,
                                    UnitInfo.VILLAGER_FEMALE_FORAGER
                                ]
                First_print = villager_job[vill]
                print(f"For Male worker I have the value {First_print}")
                Tech_du_demon_castle.new_effect.modify_attribute(
                    source_player=player,
                    object_attributes=ObjectAttribute.WORK_RATE,
                    quantity=quantity_number_3,
                    object_list_unit_id=villager_job[vill].ID,
                    operation=Operation.MULTIPLY,
                )
                Tech_du_demon_castle.new_effect.modify_attribute(
                    source_player=player,
                    object_attributes=ObjectAttribute.WORK_RATE,
                    quantity=quantity_number_3,
                    object_list_unit_id=villager_job_2[vill].ID,
                    operation=Operation.MULTIPLY,
                )
                Tech_du_demon_castle.new_effect.kill_object(
                    source_player=player,
                    object_list_unit_id=villager_job[vill].ID,
                    **area.select_entire_map().to_dict(),
                )
        if DT == 4:
            timer_quantity_1 = 1
            Tech_du_demon_imperial_A = trigger_manager.add_trigger(
                name=f"Tech du demon imperial A {player}",
                enabled=False,
                looping=False,
            )
            Tech_du_demon_imperial_B = trigger_manager.add_trigger(
                name=f"Tech du demon imperial B {player}",
                enabled=False,
                looping=False,
            )
            trigger_name_search_first = f"Tech du demon imperial A {player}"
            trigger_id_first = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_first),
                None)
            Tech_du_demon_action.new_effect.activate_trigger(
                trigger_id=trigger_id_first,
            )
            Tech_du_demon_action.new_effect.remove_object(
                source_player=player,
                object_list_unit_id=HeroInfo.YODIT.ID,
                **area.select_entire_map().to_dict()
            )
            trigger_name_search_second = f"Tech du demon imperial B {player}"
            trigger_id_second = next(
                (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_search_second),
                None)

            Tech_du_demon_imperial_A.new_effect.create_garrisoned_object(
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                object_list_unit_id_2=HeroInfo.TAMAR.ID,
                source_player=player,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_imperial_A.new_effect.create_garrisoned_object(
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                object_list_unit_id_2=HeroInfo.JADWIGA.ID,
                source_player=player,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_imperial_A.new_effect.task_object(
                object_list_unit_id=BuildingInfo.TOWN_CENTER.ID,
                source_player=player,
                **area.select_entire_map().to_dict(),
                action_type=ActionType.UNGARRISON,
            )
            Tech_du_demon_imperial_A.new_effect.activate_trigger(
                trigger_id=trigger_id_second,
            )
            Tech_du_demon_imperial_B.new_condition.timer(
                timer=timer_quantity_1,
            )
            Tech_du_demon_imperial_B.new_effect.change_ownership(
                object_list_unit_id=HeroInfo.TAMAR.ID,
                source_player=player,
                target_player=PlayerId.EIGHT,
                **area.select_entire_map().to_dict(),
            )
            Tech_du_demon_imperial_B.new_effect.change_ownership(
                object_list_unit_id=HeroInfo.JADWIGA.ID,
                source_player=player,
                target_player=PlayerId.EIGHT,
                **area.select_entire_map().to_dict(),
            )
            commercial_unit = [UnitInfo.TRADE_CART_EMPTY.ID,UnitInfo.TRADE_CART_FULL.ID,UnitInfo.TRADE_COG.ID]
            for i in range(len(commercial_unit)):
                quantity_number_3 = 3
                Tech_du_demon_imperial_B.new_effect.modify_attribute(
                    object_list_unit_id=commercial_unit[i],
                    source_player=player,
                    object_attributes=ObjectAttribute.WORK_RATE,
                    quantity=quantity_number_3,
                    operation=Operation.MULTIPLY,
                )

spawn_boss_jag_tamar = trigger_manager.add_trigger(
    name="Jagwiga and tamar spawn",
    enabled=True,
    looping=True,
)
timer_15s = 15
spawn_boss_jag_tamar.new_condition.timer(
        timer=timer_15s,
    )
for spawn in range (1,11):
    quantity_number_1 = 1
    quantity_number_0 = 0

    spawn_boss_jag_tamar.new_effect.create_garrisoned_object(
        source_player=PlayerId.EIGHT,
        **area.select_entire_map().to_dict(),
        object_list_unit_id=HeroInfo.JADWIGA.ID,
        object_list_unit_id_2=Boss_unit_spawn[spawn][quantity_number_1],
    )
    spawn_boss_jag_tamar.new_effect.create_garrisoned_object(
        source_player=PlayerId.EIGHT,
        **area.select_entire_map().to_dict(),
        object_list_unit_id=HeroInfo.TAMAR.ID,
        object_list_unit_id_2=Boss_unit_spawn[spawn][quantity_number_0],
    )
spawn_boss_jag_tamar.new_effect.task_object(
    source_player=PlayerId.EIGHT,
    object_list_unit_id=HeroInfo.JADWIGA.ID,
    **area.select_entire_map().to_dict(),
    action_type=ActionType.UNGARRISON,
)
spawn_boss_jag_tamar.new_effect.task_object(
    source_player=PlayerId.EIGHT,
    object_list_unit_id=HeroInfo.TAMAR.ID,
    **area.select_entire_map().to_dict(),
    action_type=ActionType.UNGARRISON,
)



######################################################################################################
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                  Reward for kill                                   #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
######################################################################################################
for p in range (1,8):
    quantity_number_1 = 1
    quantity_number_2 = 2
    quantity_number_3 = 3
    quantity_number_4 = 4
    quantity_number_5 = 5
    quantity_number_6 = 6
    player = Liste_joueur[p]
    kill_reward_loop_value = len(Kill_reward[1])
    for x in range (kill_reward_loop_value):
        name_trigger_value = Kill_reward[quantity_number_1][x]
        Food_value = Kill_reward[quantity_number_2][x]
        wood_value = Kill_reward[quantity_number_3][x]
        stone_value = Kill_reward[quantity_number_4][x]
        gold_value = Kill_reward[quantity_number_5][x]
        tickets_value = Kill_reward[quantity_number_6][x]
        kill_reward = trigger_manager.add_trigger(
            name=f"Kill reward for value {name_trigger_value} and player {player}",
            enabled=True,
            looping=False,
        )
        kill_reward.new_condition.accumulate_attribute(
            source_player=player,
            attribute=Attribute.UNITS_KILLED,
            quantity=Kill_reward[quantity_number_1][x],
        )
        if Food_value:
            kill_reward.new_effect.tribute(
                source_player=PlayerId.GAIA,
                target_player=player,
                tribute_list=Attribute.FOOD_STORAGE,
                quantity= Kill_reward[quantity_number_2][x],
            )
        if wood_value:
            kill_reward.new_effect.tribute(
                source_player=PlayerId.GAIA,
                target_player=player,
                tribute_list=Attribute.WOOD_STORAGE,
                quantity=Kill_reward[quantity_number_3][x],
            )
        if stone_value:
            kill_reward.new_effect.tribute(
                source_player=PlayerId.GAIA,
                target_player=player,
                tribute_list=Attribute.STONE_STORAGE,
                quantity=Kill_reward[quantity_number_4][x],
            )
        if gold_value:
            kill_reward.new_effect.tribute(
                source_player=PlayerId.GAIA,
                target_player=player,
                tribute_list=Attribute.GOLD_STORAGE,
                quantity=Kill_reward[quantity_number_5][x],
            )
        if tickets_value:
            kill_reward.new_effect.tribute(
                source_player=PlayerId.GAIA,
                target_player=player,
                tribute_list=Attribute.UNUSED_RESOURCE_120,
                quantity=Kill_reward[quantity_number_6][x],
            )
res_demon_tech = trigger_manager.add_trigger(
            name=f"Resource for everyone demon tech",
            enabled=True,
            looping=False,
        )
for p in range (1,8):
    quantity_number_8 = 8
    quantity_number_1 = 1
    player = Liste_joueur[p]
    for res in range(1,5):
        res_demon_tech.new_effect.modify_resource(
            source_player=player,
            tribute_list=Demon_tech[res][quantity_number_8],
            quantity=quantity_number_1,
            operation=Operation.SET,
        )
for p in range (1,8):
    quantity_number_8 = 8
    quantity_number_0 = 0
    quantity_number_1 = 1
    quantity_number_2 = 2
    quantity_number_3 = 3
    quantity_number_4 = 4
    quantity_number_5 = 5
    player = Liste_joueur[p]
    for tech in range (1,6):
        ID_Value = tech + 5
        if ID_Value != 10:
            tech_enum = getattr(TechInfo, f"TECHNOLOGY_PLACEHOLDER_0{ID_Value}")
        else:
            tech_enum = getattr(TechInfo, f"TECHNOLOGY_PLACEHOLDER_{ID_Value}")
        tech_obj = tech_enum.ID
        tower_id = [BuildingInfo.WATCH_TOWER.ID,BuildingInfo.GUARD_TOWER.ID,BuildingInfo.DONJON.ID,BuildingInfo.KEEP.ID]
        techno_tower = trigger_manager.add_trigger(
            name=f"Technologie {tech_obj} for player {player}",
            enabled=True,
            looping=False,
        )
        techno_tower.new_condition.research_technology(
            source_player=player,
            technology=tech_obj,
        )
        for i in range(len(tower_id)):
            print(f"Tech={tech}, i={i}, attr0={Tower_upgrade_stat[tech][0]}, attr1={Tower_upgrade_stat[tech][1]}, attr2={Tower_upgrade_stat[tech][2]}")
            if tech ==2:
                techno_tower.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=tower_id[i],
                    armour_attack_class=quantity_number_3,
                    object_attributes=Tower_upgrade_stat[tech][quantity_number_0],
                    armour_attack_quantity=Tower_upgrade_stat[tech][quantity_number_1],
                    operation=Tower_upgrade_stat[tech][quantity_number_2],
                )
            elif tech == 3:
                techno_tower.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=tower_id[i],
                    object_attributes=Tower_upgrade_stat[tech][quantity_number_0],
                    quantity=Tower_upgrade_stat[tech][quantity_number_1],
                    operation=Tower_upgrade_stat[tech][quantity_number_2],
                )
                techno_tower.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=tower_id[i],
                    object_attributes=Tower_upgrade_stat[tech][quantity_number_3],
                    quantity=Tower_upgrade_stat[tech][quantity_number_4],
                    operation=Tower_upgrade_stat[tech][quantity_number_5],
                )
            else:
                techno_tower.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=tower_id[i],
                    object_attributes=Tower_upgrade_stat[tech][quantity_number_0],
                    quantity=Tower_upgrade_stat[tech][quantity_number_1],
                    operation=Tower_upgrade_stat[tech][quantity_number_2],
                )

        techno_tower_stat = trigger_manager.add_trigger(
            name=f"Technologie {tech_obj} for player {player}",
            enabled=True,
            looping=False,
        )
        bouton_placement = 10 + tech
        techno_tower_stat.new_effect.change_technology_location(
            source_player=player,
            object_list_unit_id_2=BuildingInfo.BLACKSMITH.ID,
            technology=tech_obj,
            button_location=bouton_placement,
        )
        techno_tower_stat.new_effect.change_technology_cost(
            source_player=player,
            technology=tech_obj,
            resource_1=Tower_upgrade_cost_desc[tech][quantity_number_0],
            resource_1_quantity=Tower_upgrade_cost_desc[tech][quantity_number_1],
            resource_2=Tower_upgrade_cost_desc[tech][quantity_number_2],
            resource_2_quantity=Tower_upgrade_cost_desc[tech][quantity_number_3],
        )
        techno_tower_stat.new_effect.change_technology_description(
            source_player=player,
            technology=tech_obj,
            message=Tower_upgrade_cost_desc[tech][quantity_number_4],
        )
        techno_tower_stat.new_effect.change_technology_research_time(
            source_player=player,
            technology=tech_obj,
            quantity=quantity_number_2,

        )
        techno_tower_stat.new_effect.change_technology_icon(
            source_player=player,
            technology=tech_obj,
            quantity=Tower_upgrade_cost_desc[tech][quantity_number_5],
        )
for p in range (1,8):
    player = Liste_joueur[p]
    timer_5s = 5
    quantity_number_1 = 1
    quantity_number_5 = 5
    armour_class_melee = 4
    cobra_car_att = trigger_manager.add_trigger(
        name=f"cobra car stat for player {player}"
    )
    cobra_car_att.new_condition.timer(
        timer=timer_5s,
    )
    cobra_car_att.new_effect.modify_attribute(
        source_player=player,
        quantity=quantity_number_1,
        object_attributes=ObjectAttribute.ATTACK_RELOAD_TIME,
        object_list_unit_id=UnitInfo.COBRA_CAR.ID,
        operation=Operation.SET,
    )
    cobra_car_att.new_effect.modify_attribute(
        source_player=player,
        quantity=quantity_number_1,
        object_attributes=ObjectAttribute.MOVEMENT_SPEED,
        object_list_unit_id=UnitInfo.COBRA_CAR.ID,
        operation=Operation.SET,
    )
    cobra_car_att.new_effect.modify_attribute(
        source_player=player,
        armour_attack_class= armour_class_melee,
        armour_attack_quantity= quantity_number_5,
        object_attributes=ObjectAttribute.ATTACK,
        object_list_unit_id=UnitInfo.COBRA_CAR.ID,
        operation=Operation.SET,
    )

for p in range (1,8):
    player = Liste_joueur[p]
    button_placement = 10
    quantity_number_0 = 0
    quantity_number_1 = 1
    quantity_number_295 = 295
    food = Attribute.FOOD_STORAGE
    stone = Attribute.STONE_STORAGE
    Unused_resource_136 = Attribute.UNUSED_RESOURCE_136
    food_quantity = 15000
    stone_quantity = 15000
    timer_potion = 1800
    special_res_quantity=1
### Toute cette partie fait le enable de la potion qui est le héro ENVOY dans la merveille
    potion = trigger_manager.add_trigger(
        name =f"enable Potion for player {player}",
        enabled=True,
        looping=False,
    )
    potion.new_effect.enable_disable_object(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        enabled=True,
    )
    potion.new_effect.change_train_location(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        object_list_unit_id_2=BuildingInfo.WONDER.ID,
        button_location=button_placement,
    )
    potion.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        quantity=quantity_number_295,
        object_attributes=ObjectAttribute.ICON_ID,
    )
    potion.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        quantity=quantity_number_0,
        object_attributes=ObjectAttribute.OBJECT_NAME_ID,
        message="The holy potion of steroid"
    )
    potion.new_effect.change_object_cost(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        # RES TYPE
        resource_1=Attribute.FOOD_STORAGE,
        resource_2=Attribute.STONE_STORAGE,
        resource_3=Unused_resource_136,
        # quantity
        resource_1_quantity=food_quantity,
        resource_2_quantity=stone_quantity,
        resource_3_quantity=special_res_quantity,
    )
    potion.new_effect.change_object_description(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        message="Use the holy potion of steroid <cost> \n Your troops drink this sacred beverage, they gain +10 armor and attacks and +150 HP for 30 minutes.\n You will not be able to re-used the potion while your troops are under the effect"
    )
    potion.new_effect.modify_resource(
        source_player=player,
        tribute_list=Unused_resource_136,
        quantity=quantity_number_1,
        operation=Operation.SET,
    )
#Script des effet et inversement
    #Effet de potion positif
    script_potion = f"void potion_effect_{player}()"
    script_potion += "{"
    #Armure melee
    script_potion += f"xsEffectAmount(cAddAttribute, 906, cArmor, 4*256 + 10, {player});" # INFANTRY
    script_potion += f"xsEffectAmount(cAddAttribute, 912, cArmor, 4*256 + 10, {player});" # CAVALRY
    script_potion += f"xsEffectAmount(cAddAttribute, 900, cArmor, 4*256 + 10, {player});" # ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 936, cArmor, 4*256 + 10, {player});" # CAV ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 944, cArmor, 4*256 + 10, {player});" # Canonier
    script_potion += f"xsEffectAmount(cAddAttribute, 913, cArmor, 4*256 + 10, {player});" # Mangonel et belier
    script_potion += f"xsEffectAmount(cAddAttribute, 955, cArmor, 4*256 + 10, {player});" # # Scorpion
    #Armure range
    script_potion += f"xsEffectAmount(cAddAttribute, 906, cArmor, 3*256 + 10, {player});"  # INFANTRY
    script_potion += f"xsEffectAmount(cAddAttribute, 912, cArmor, 3*256 + 10, {player});"  # CAVALRY
    script_potion += f"xsEffectAmount(cAddAttribute, 900, cArmor, 3*256 + 10, {player});"  # ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 936, cArmor, 3*256 + 10, {player});"  # CAV ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 944, cArmor, 3*256 + 10, {player});"   #Canonier
    script_potion += f"xsEffectAmount(cAddAttribute, 913, cArmor, 3*256 + 10, {player});"  # Mangonel et belier
    script_potion += f"xsEffectAmount(cAddAttribute, 955, cArmor, 3*256 + 10, {player});"  # # Scorpion
    #PV
    script_potion += f"xsEffectAmount(cAddAttribute, 906, 0, 150, {player});"  # INFANTRY
    script_potion += f"xsEffectAmount(cAddAttribute, 912, 0, 150, {player});"  # CAVALRY
    script_potion += f"xsEffectAmount(cAddAttribute, 900, 0, 150, {player});"  # ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 936, 0, 150, {player});"  # CAV ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 944, 0, 150, {player});"  # Canonier
    script_potion += f"xsEffectAmount(cAddAttribute, 913, 0, 150, {player});"  # Mangonel et belier
    script_potion += f"xsEffectAmount(cAddAttribute, 955, 0, 150, {player});"  # # Scorpion
    # Attaque
    script_potion += f"xsEffectAmount(cAddAttribute, 906, 9, 4*256 + 10, {player});"  # INFANTRY
    script_potion += f"xsEffectAmount(cAddAttribute, 912, 9, 4*256 + 10, {player});"  # CAVALRY
    script_potion += f"xsEffectAmount(cAddAttribute, 900, 9, 3*256 + 10, {player});"  # ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 936, 9, 3*256 + 10, {player});"  # CAV ARCHER
    script_potion += f"xsEffectAmount(cAddAttribute, 944, 9, 3*256 + 10, {player});"  # Canonier
    script_potion += f"xsEffectAmount(cAddAttribute, 913, 9, 4*256 + 10, {player});"  # Mangonel et belier
    script_potion += f"xsEffectAmount(cAddAttribute, 955, 9, 3*256 + 10, {player});"  # # Scorpion
    script_potion += "}"
# EFFET INVERSE POTION
    rev_script_potion = f"void potion_reveffect_{player}()"
    rev_script_potion += "{"
    # Armure melee
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 906, cArmor,-4*256-10, {player});"  # INFANTRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 912, cArmor,-4*256-10, {player});"  # CAVALRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 900, cArmor,-4*256-10, {player});"  # ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 936, cArmor,-4*256-10, {player});"  # CAV ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 944, cArmor,-4*256-10, {player});"  # Canonier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 913, cArmor,-4*256-10, {player});"  # Mangonel et belier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 955, cArmor,-4*256-10, {player});"  # # Scorpion
    # Armure range
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 906, cArmor,-3*256-10, {player});"  # INFANTRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 912, cArmor,-3*256-10, {player});"  # CAVALRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 900, cArmor,-3*256-10, {player});"  # ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 936, cArmor,-3*256-10, {player});"  # CAV ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 944, cArmor,-3*256-10, {player});"  # Canonier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 913, cArmor,-3*256-10, {player});"  # Mangonel et belier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 955, cArmor,-3*256-10, {player});"  # # Scorpion
    # PV
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 906, 0, -150, {player});"  # INFANTRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 912, 0, -150, {player});"  # CAVALRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 900, 0, -150, {player});"  # ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 936, 0, -150, {player});"  # CAV ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 944, 0, -150, {player});"  # Canonier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 913, 0, -150, {player});"  # Mangonel et belier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 955, 0, -150, {player});"  # # Scorpion
    # Attaque
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 906, 9,-4*256-10, {player});"  # INFANTRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 912, 9,-4*256-10, {player});"  # CAVALRY
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 900, 9,-3*256-10, {player});"  # ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 936, 9,-3*256-10, {player});"  # CAV ARCHER
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 944, 9,-3*256-10, {player});"  # Canonier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 913, 9,-4*256-10, {player});"  # Mangonel et belier
    rev_script_potion += f"xsEffectAmount(cAddAttribute, 955, 9,-4*256-10, {player});"  # # Scorpion
    rev_script_potion += "}"

    ### Toute fait partie va faire la detection du héro sur le terrain et activer le timer
    potion_on_land = trigger_manager.add_trigger(
            name =f"potion on land {player}",
            enabled=True,
            looping=True,
        )
    potion_timer = trigger_manager.add_trigger(
        name=f"Timer effect {player}",
        enabled=False,
        looping=True,
    )
    potion_on_land.new_condition.objects_in_area(
        source_player=player,
        object_list=HeroInfo.ENVOY.ID,
        **area.select_entire_map().to_dict(),
        quantity=quantity_number_1,
        object_state=ObjectState.ALIVE,
    )
    potion_on_land.new_effect.script_call(
        message=script_potion
    )
    potion_on_land.new_effect.remove_object(
        source_player=player,
        object_list_unit_id=HeroInfo.ENVOY.ID,
        **area.select_entire_map().to_dict(),
        object_state=ObjectState.ALIVE,
    )
    trigger_remove_first = f"Timer effect {player}"
    trigger_id_first = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_first), None)
    potion_on_land.new_effect.activate_trigger(
        trigger_id=trigger_id_first,
    )
    potion_timer.new_condition.timer(
        timer=timer_potion,
    )
    potion_timer.new_effect.script_call(
        message=rev_script_potion,
    )
    potion_timer.new_effect.modify_resource(
        source_player=player,
        tribute_list=Unused_resource_136,
        quantity=quantity_number_1,
        operation=Operation.SET,
    )
    potion_timer.new_effect.deactivate_trigger(
        trigger_id=trigger_id_first,
    )

Header_end = trigger_manager.add_trigger( #End of the plugin
            name=f"-----end_Plugin------",
            enabled=False,
            looping=False,
        )

scenario.write_to_file(output_path)
