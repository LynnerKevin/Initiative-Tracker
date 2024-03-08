import customtkinter as ctk
from entity_creation_windows import Monster_creator_frame, Player_creator_frame
from scrolling_pane import initiative_queue
from entities import Player, Monster


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        #self.grid_columnconfigure()

        self.title("Initiative Tracker")
        self.initiative_visible = False

        # List to hold the creatures in initiative
        self.creatures = []

        self.monster_creator = Monster_creator_frame(self)
        self.monster_creator.grid(row=0, column=0, padx=10, pady=10)

        self.player_creator = Player_creator_frame(self)
        self.player_creator.grid(row=1, column=0, padx=10, pady=10)

        self.reset_initiative = ctk.CTkButton(self, text="Reset Initiative", command=self.reset)
        self.reset_initiative.grid(row=1, column=1, padx=10, pady=10)

        self.show_order = ctk.CTkButton(self, text="Show Order", command=self.display_order)
        self.show_order.grid(row=0, column=1, padx=10, pady=10)

        self.creature_couter = ctk.CTkLabel(self, text=f'Creature Count: {len(self.creatures)}')
        self.creature_couter.grid(row=2, column=0, padx=10, pady=10, rowspan=1)

        self.initiative_box = initiative_queue(self, self.creatures, False)
        self.initiative_box.grid(row=0, column=2, padx=10, pady=10, rowspan=5)

        self.advance_turn_button = ctk.CTkButton(self, text='Advance Turn', command=self.next_turn)
        self.advance_turn_button.grid(row = 2, column = 1, padx = 10, pady = 10, rowspan=1)


    def add_monsters(self):
        monster_values, monsters = self.monster_creator.get()
        if monsters:
            #print(f"adding {len(monsters)} monsters, total creatures: {len(self.initiative)}")
            self.creatures.extend(monsters)
            self.creature_couter.configure(text=f'Creature Count: {len(self.creatures)}')
        else:
            pass
            #print("Monster values invalid")

    def add_player(self):
        player_values, player = self.player_creator.get()
        if player:
            #print(f"adding {player}, total creatures: {len(self.creatures)}")
            self.creatures.append(player)
            self.creature_couter.configure(text=f'Creature Count: {len(self.creatures)}')
        #print("adding player")

    def display_order(self):
        if len(self.creatures):
            self.initiative_box = initiative_queue(self, self.creatures, self.initiative_visible)
            self.initiative_box.grid(row=0, column=2, padx=10, pady=10, rowspan=5)
            self.initiative_visible = True
            self.initiative_box.initiative_queue[0].toggle_status()
            #self.mainloop()

    def reset(self):
        self.creatures=[]
        self.initiative_box = initiative_queue(self, self.creatures, self.initiative_visible)
        self.initiative_box.grid(row=0, column=2, padx=10, pady=10, rowspan=5)
        self.creature_couter.configure(text=f'Creature Count: {len(self.creatures)}')
        self.initiative_visible = False
        #self.mainloop()

    def next_turn(self):

        if self.initiative_visible:
            self.initiative_box.advance_turn()

