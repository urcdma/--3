import genanki

class AnkiDeck:
    def __init__(self, deck_id: int, deck_name: str):
        """
        Initialize the Anki deck with the provided deck id and name
        """
        self.deck = genanki.Deck(deck_id, deck_name)
        self.model = genanki.Model(
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

    def create_deck(self) -> None:
        """
        Create a new Anki deck
        """
        self.deck = genanki.Deck(self.deck_id, self.deck_name)

    def add_card(self, front: str, back: str) -> None:
        """
        Add a card to the Anki deck
        """
        note = genanki.Note(
            model=self.model,
            fields=[front, back],
        )
        self.deck.add_note(note)

    def download_deck(self) -> genanki.Deck:
        """
        Return the Anki deck
        """
        return self.deck
