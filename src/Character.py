from src.utils.character.chr_clas.spec.barbarian import Barbarian
from src.utils.character.race.spec.dragonborn import Dragonborn

import src.utils.utils as utilities


class Character:
    def __init__(self, level):
        self.level = int(level)

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0
        utilities.init_scores(self, self.level)
        self.race = None
        self.clas = None
        self.background = ""
        self.stats = []
        self.personality = ""

    def set_stats(self):
        pass

    def set_race(self):
        race = Dragonborn(self.level)
        self.race = race

    def set_class(self):
        dnd_class = Barbarian(self)

    def set_background(self):
        pass

    def set_personality(self):
        pass

