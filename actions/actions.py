from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionConfirmAddTask(Action):

    def name(self) -> Text:
        return "action_confirm_add_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm adding task")
        employee = tracker.get_slot('employee')
        print(employee)
        time = tracker.get_slot("time")
        print(time)
        task_title = tracker.get_slot("task_title")
        print(task_title)
        description = tracker.get_slot("description")
        print(description)

        dispatcher.utter_message(text="confirm add task")
        return []


class ActionAddTask(Action):

    def name(self) -> Text:
        return "action_add_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("adding task")
        dispatcher.utter_message(text="adding task")

        return []


class ActionGetTask(Action):

    def name(self) -> Text:
        return "action_get_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("getting task")
        employee = tracker.get_slot('employee')
        print(employee)
        time = tracker.get_slot("time")
        print(time)
        dispatcher.utter_message(text="getting task")

        return []


class ActionConfirmAddEvent(Action):

    def name(self) -> Text:
        return "action_confirm_add_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm adding event")
        time = tracker.get_slot("time")
        print(time)
        end_time = tracker.get_slot("end_time")
        print(end_time)
        event_title = tracker.get_slot("event_title")
        print(event_title)
        description = tracker.get_slot("description")
        print(description)

        dispatcher.utter_message(text="confirm add event")
        return []


class ActionAddEvent(Action):

    def name(self) -> Text:
        return "action_add_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("adding event")
        dispatcher.utter_message(text="adding event")

        return []
