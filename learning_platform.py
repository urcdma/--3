import genanki
from gpt_model import GPTModel
from typing import List, Tuple

class LearningPlatform:
    def __init__(self):
        self.knowledge_points = []
        self.memory_cards = []
        self.gpt_model = GPTModel()
        self.deck = genanki.Deck(2059400110, "Python Learning Deck")

    def list_knowledge_points(self) -> None:
        """
        List Python knowledge points
        """
        # TODO: Define the list of Python knowledge points
        self.knowledge_points = ["Variables", "Data Types", "Operators", "Control Flow", "Functions", "Classes", "Modules"]

    def generate_memory_cards(self) -> None:
        """
        Generate memory cards for the knowledge points
        """
        for point in self.knowledge_points:
            front = point
            back = self.gpt_model.interpret_knowledge_point(point)
            self.memory_cards.append((front, back))
            self.add_card(front, back)

    def display_memory_cards(self) -> List[Tuple[str, str]]:
        """
        Display the generated memory cards
        """
        return self.memory_cards

    def add_card(self, front: str, back: str) -> None:
        """
        Add a card to the Anki deck
        """
        my_model = genanki.Model(
            1607392319,
            "Simple Model",
            fields=[
                {"name": "Question"},
                {"name": "Answer"},
            ],
            templates=[
                {
                    "name": "Card 1",
                    "qfmt": "{{Question}}",
                    "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ],
        )
        my_note = genanki.Note(
            model=my_model,
            fields=[front, back],
        )
        self.deck.add_note(my_note)

    def download_deck(self) -> genanki.Deck:
        """
        Download the Anki deck
        """
        return self.deck
