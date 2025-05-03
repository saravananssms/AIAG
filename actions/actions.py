from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendPolicy(Action):
    def name(self) -> Text:
        return "action_recommend_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        vehicle = tracker.get_slot("vehicle_type")
        postcode = tracker.get_slot("postcode")

        recommendation = self.get_recommendation(vehicle, postcode)

        dispatcher.utter_message(text=recommendation)
        return []

    def get_recommendation(self, vehicle: Text, postcode: Text) -> str:
        if vehicle == "Tesla" or vehicle == "electric":
            return f"Based on your {vehicle} in {postcode}, I recommend our *Comprehensive Electric Vehicle Plan*."
        elif postcode.startswith("200") or postcode.startswith("300"):
            return f"Given your location in {postcode}, I recommend our *Natural Disaster Protection Plan*."
        else:
            return f"Based on your {vehicle} and location, I recommend our *Standard Comprehensive Plan*."
