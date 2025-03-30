from email.headerregistry import UniqueUnstructuredHeader
from gc import enable
from idlelib.rpc import objecttable
from pickle import FALSE

from AoE2ScenarioParser.datasets.effects import attributes
from AoE2ScenarioParser.objects.support import area
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
from Upgrade_station_dictionnary import technologie_page_desc_icon, technology_cost_icon, special_case_3
from Upgrade_station_dictionnary import Techno_message
from Upgrade_station_dictionnary import Techno_xs
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
input_path = "CHANGE PATH HERE"
output_path = "CHANGE PATH HERE"



# Lecture et écriture du scénario
scenario = AoE2DEScenario.from_file(input_path)
trigger_manager = scenario.trigger_manager
fonction_remove = 1

#---------------------------------------------------------------------
if fonction_remove == 1:
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
        maxi_boucle = 16
    elif u == 3:
        min_boucle = 16
        maxi_boucle = 23
    elif u == 4:
        min_boucle = 23
        maxi_boucle = 31
    else:
        min_boucle = 31
        maxi_boucle = 37
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
            quantity_number_true = Techno_xs[s][quantity_number_11]
            if_true = 1
            special_case= 2
            special_case_2= 3
            special_case_3 = 4
            special_case_4 =5
            special_case_5 =6
            tech_obj_2 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # <-- OK ici
            tech_id_2 = tech_obj_2.ID
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
            if s not in [35,36]:
                check_tech[y].new_effect.script_call(
                    message=Script_XS,
                )
            elif s == 35:
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.POPULATION_HEADROOM,
                    source_player=player,
                    quantity=quantity_number_24,
                    operation=Operation.ADD,
                )
            else:
                trigger_remove_first = f"Première activation {player}"
                trigger_id_first = next(
                    (i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_first),None)
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

for p in range (1,8):
    player=Liste_joueur[p]
    quantity_number_1 = 4
    quantity_number_2 = 2
    quantity_number_3 = 3
    attribution_resource_pour_tech = trigger_manager.add_trigger(
        name=f"Attribution des resources pour tech {player}",
        enabled=True,
        looping=False,
    )
    for y in range (1,37):
        attribution_resource_pour_tech.new_effect.modify_resource(
            tribute_list=technology_cost_icon[y][quantity_number_1],
            source_player=player,
            quantity=quantity_number_3,
            operation=Operation.SET,
        )





Header_end = trigger_manager.add_trigger( #End of the plugin
            name=f"-----end_Plugin------",
            enabled=False,
            looping=False,
        )


scenario.write_to_file(output_path)
