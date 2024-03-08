import customtkinter as ctk
from entity_creation_windows import is_numbers
from entities import Player, Monster
from functools import total_ordering


@total_ordering
class Creature_Display_Frame(ctk.CTkFrame):
    def __init__(self, master, creature):
        super().__init__(master)

        self.creature = creature  # be able to access attributes of the creature elsewhere
        self.active_turn = False

        self.name = ctk.CTkLabel(self, text=self.creature.name)
        self.name.grid(row=0, column=0, padx=10, pady=10)

        self.initiative = ctk.CTkLabel(self, text=f"Init: {self.creature.initiative} (+{creature.init_mod})")
        self.initiative.grid(row=0, column=2, padx=10, pady=10)

        self.active_turn_indicator = ctk.CTkLabel(self, text='----', text_color='#fc5e03')
        self.active_turn_indicator.grid(row=0, column=3, padx=10, pady=10)

    def toggle_status(self):
        self.active_turn = not self.active_turn
        if self.active_turn:
            self.active_turn_indicator.configure(self, text='Active', text_color='#45f542')
        else:
            self.active_turn_indicator.configure(self, text='----', text_color='#fc5e03')

    def __lt__(self, other):
        return self.creature < other.creature

    def __eq__(self, other):
        return self.creature == other.creature

    def __repr__(self):
        return f'{self.creature}\nActive: {self.active_turn}\nWindow Name: {self.name}'


class Monster_displayFrame(Creature_Display_Frame):
    def __init__(self, master, creature: Monster):
        super().__init__(master, creature)

        self.mon_name = ctk.CTkLabel(self, text=self.creature.name)
        self.mon_name.grid(row=0, column=0, padx=10, pady=10)

        self.HP = ctk.CTkLabel(
            self, text=f"{self.creature.current_hit_points} / {self.creature.max_hit_points}",
            text_color="#1da341"
        )
        self.HP.grid(row=0, column=1, padx=10, pady=10)

        self.damage_button = ctk.CTkButton(self, text="Damage",
                                           command=self.damage_press,
                                           text_color='#ff0000')

        self.damage_button.grid(row=1, column=0, padx=10, pady=10)

        self.heal_button = ctk.CTkButton(self, text="Heal",
                                         command=self.heal_press,
                                         text_color="#1da341")

        self.heal_button.grid(row=1, column=1, padx=10, pady=10)

    def update_hp(self):
        """
        Updates the text displayed to reflect the current HP value and changes
        color at certain thresholds
        """
        self.HP.configure(text=f"{self.creature.current_hit_points} / {self.creature.max_hit_points}")

        if self.creature.current_hit_points <= 0:  # catch 0 or negative numbers
            self.creature.current_hit_points = 0  # creatures can't have negative HP, so change to 0
            self.HP.configure(text="DEAD")

        # Conditions are in ascending order as being below 25% means you're also below 50%

        # condition: crippled
        if self.creature.current_hit_points / self.creature.max_hit_points <= 0.25:
            self.HP.configure(text_color='#ff0000')

        # condition: bloodied
        elif self.creature.current_hit_points / self.creature.max_hit_points <= 0.5:
            self.HP.configure(text_color='#db570b')

        # condition: fine
        else:
            self.HP.configure(text_color="#1da341")

    def damage_press(self):
        dialog = ctk.CTkInputDialog(title="How much damage was dealt", text="Enter Damage Value")
        value = dialog.get_input()
        if is_numbers(value):
            self.creature.damage(int(value))
            self.update_hp()

    def heal_press(self):
        dialog = ctk.CTkInputDialog(title="How much healed", text="Enter Healing Value")
        value = dialog.get_input()
        if is_numbers(value):
            self.creature.heal(int(value))
            self.update_hp()


class Player_displayFrame(Creature_Display_Frame):
    def __init__(self, master, creature: Player):
        super().__init__(master, creature)
