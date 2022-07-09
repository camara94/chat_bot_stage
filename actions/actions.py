# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# on importe ses from pour supporter les fonctionnalités du framework rasa au cas python installé dans le pc ne reconnait pas
from __future__ import absolute_import, unicode_literals
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from email import message
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# la classe SlotSet permet de stocker des informations en mémoire.
from rasa_sdk.events import SlotSet

#
#
# class ActionHelloWorld(Action): une  classe prposée par le framework rasa pour pouvoir personnaliser les actions du framework
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionAfficherMenu(Action):
    def name(self) -> Text:
        return "action_afficher_menu"

    def run(self,
            dispatcher: CollectingDispatcher,  # permet d'afficher les messages
            tracker: Tracker,  # permet de recuperer les Slot .
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        menu = ""
        with open("C:/Users/damaro/chat_bot_stage/static/menu.txt", "r", encoding="UTF-8") as f:
            menu += f.read()

        dispatcher.utter_message(text=menu)

        return []


class ActionSelectionnerMenu(Action):

    def name(self) -> Text:
        return "action_selectionner_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gerer_menu = tracker.latest_message['text']
        return [SlotSet('menu', gerer_menu)]


class ActionDemandeConfirmation(Action):
    def name(self) -> Text:
        return "action_demande_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gerer_menu = tracker.latest_message['text']
        repas = open("C:/Users/damaro/chat_bot_stage/static/menu.txt",
                     "r", encoding="UTF-8").readlines()

        nombres = []
        if gerer_menu.find(',') <= 0 and gerer_menu.find(' ') >= 0:
            nombres = [int(n.strip()) for n in gerer_menu.split(' ')]
        elif gerer_menu.find(',') >= 0:
            nombres = [int(n.strip()) for n in gerer_menu.split(',')]
        else:
            if int(gerer_menu) < len(repas):
                nombres.append(int(gerer_menu))

        if len(nombres) > 0:
            lesrepas = ""
            for i, n in enumerate(nombres):
                try:
                    lesrepas += "  " + repas[n]
                except:
                    pass
            choixRepas = "Avez-vous choisi le(s) menu(s):\n{} \n Oui(O)\n Non(N)".format(
                lesrepas)
        else:
            choixRepas = "Veuillez demander le menu au serveur à nouveau !\ncar ce choix n'existe pas dans notre menu"

        dispatcher.utter_message(text=choixRepas)
        return []


class ActionValiderConfirmation(Action):
    def name(self) -> Text:
        return "action_valider_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gerer_menu = tracker.get_slot('menu')
        reponse = tracker.latest_message['text']
        print("Valeurs: ", gerer_menu)
        addition = open("C:/Users/damaro/chat_bot_stage/static/prix.txt",
                        "r", encoding="UTF-8").readlines()
        ##choix = int(gerer_menu)
        nombres = []
        if gerer_menu.find(',') < 0 and gerer_menu.find(' ') >= 0:
            nombres = [int(i) for i in gerer_menu.split(' ')]
        elif gerer_menu.find(',') >= 0:
            nombres = [int(i.strip()) for i in gerer_menu.split(',')]
        else:
            nombres.append(int(gerer_menu))
        total = 0
        for i in nombres:
            try:
                total += float(addition[i])
            except:
                print('')

        message = "Veuillez patienter\nVotre addition est {} TND".format(total)
        #print('====================================reponse: ', reponse, "***menu: ", gerer_menu)
        if reponse == "Oui" or reponse == 'oui' or reponse == 'O' or reponse == 'o':
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(
                text="Veuillez demander le menu au serveur à nouveau !")

        return [SlotSet('reponse', reponse)]
