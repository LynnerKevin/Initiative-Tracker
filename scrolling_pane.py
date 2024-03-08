import customtkinter as ctk
from creature_dispay_tile import Monster_displayFrame, Player_displayFrame
from random import shuffle
from entities import Player, Monster


class initiative_queue(ctk.CTkScrollableFrame):
    def __init__(self, master, creatures, initiative_visible):
        super().__init__(master)

        self.configure(width=500, height=800)

        self.initiative_visible = initiative_visible
        self.active_turn_index = 0
        self.creatures = creatures.copy()
        self.initiative_queue = []
        # shuffling first coin-flips true ties
        shuffle(self.creatures)
        # Make sure all entries are Monsters or Players,
        self.creatures = [x for x in self.creatures if (isinstance(x, Monster) or isinstance(x, Player))]
        # Sort the list in descending order
        self.creatures.sort(reverse=True)

        for creature in self.creatures:
            if type(creature) is Monster:
                self.initiative_queue.append(Monster_displayFrame(self, creature))

            elif type(creature) is Player:
                self.initiative_queue.append(Player_displayFrame(self, creature))

        for i, creature in enumerate(self.initiative_queue):
            creature.grid(row=i, column=1, padx=10, pady=10)


    def advance_turn(self):
        # Advance the turn marker to the next in the order
        self.initiative_queue[self.active_turn_index].toggle_status()
        self.active_turn_index += 1

        if self.active_turn_index == len(self.initiative_queue):
            self.active_turn_index = 0

        #print(self.initiative_queue[self.active_turn_index].name)
        self.initiative_queue[self.active_turn_index].toggle_status()


