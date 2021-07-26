##################################################################################
#  You can add your actions in this file or create any other file in this folder #
##################################################################################

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ReminderScheduled, ConversationPaused, ConversationResumed, FollowupAction, Restarted, ReminderScheduled


class MyAction(Action):

    def name(self):
        return 'action_my_action'

    def run(self, dispatcher, tracker, domain):
        # do something.
        return []

class SetColor(Action):
    def name(self):
        return 'action_set_color'
    def run(self, dispatcher, tracker, domain):
        return [SlotSet("color","azul")]

class FetchStatus(Action):
    def name(self):
        return 'action_fetch_status'
    def run(self, dispatcher, tracker, domain):
        status = ... # a function that will get the user status from your api
        return [SlotSet("status", status)]