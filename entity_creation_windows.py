import customtkinter as ctk
from entities import Player, Monster


def is_numbers(test_string, include_decimal=False):
    """
    Takes a string and tests to see if parsing it as an integer or float
    will raise an error, also makes sure the string is not empty
    :param test_string: string to test
    :param include_decimal: whether to include a decimal in the
    :return: bool
    """
    if include_decimal:
        digits = '1234567890.'
    else:
        digits = '1234567890'
    return set(test_string).issubset(set(digits)) and test_string


class Monster_creator_frame(ctk.CTkFrame):
    """
    Fill-able template to enter all information needed
    to make an enemy or monster to be added to the
    initiative
    """

    def __init__(self, master):
        super().__init__(master)

        # Title of Box
        self.title = ctk.CTkLabel(self, text="NPC/Enemy Creation")
        self.title.grid(row=0, column=0, padx=10, pady=10)

        self.add_monsters_button = ctk.CTkButton(self, text="Add Monster(s)", command=master.add_monsters)
        self.add_monsters_button.grid(row=0, column=1, padx=10, pady=10)

        # Entry box for monster name
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Creature Name")
        self.name_entry.grid(row=1, column=0, padx=10, pady=10)

        # Entry box for monster HP
        self.HP_entry = ctk.CTkEntry(self, placeholder_text="Creature Max HP")
        self.HP_entry.grid(row=2, column=0, padx=10, pady=10)

        # Entry box for monster initiative
        self.initiative_entry = ctk.CTkEntry(self, placeholder_text="Creature Initiative Mod")
        self.initiative_entry.grid(row=1, column=1, padx=10, pady=10)

        self.copies = ctk.CTkEntry(self, placeholder_text="# of this monster")
        self.copies.grid(row=2, column=1, padx=10, pady=10)

    def get(self):

        # print('getting monster')
        values, monsters = None, None
        # check to make sure HP is a positive integer
        hp_entry = self.HP_entry.get()
        hp_valid = is_numbers(hp_entry) and hp_entry != '0'

        # check to make sure initiative mod is an integer, can be negative
        init_entry = self.initiative_entry.get()
        init_mod = is_numbers(init_entry)

        # check to make sure copies is a positive integer
        copies_entry = self.copies.get()
        copies = is_numbers(copies_entry) and copies_entry != '0'

        if hp_valid and init_mod and copies:
            values = {
                'name': self.name_entry.get(),
                'HP': int(self.HP_entry.get()),
                'init mod': int(self.initiative_entry.get()),
                'copies': int(copies_entry)
            }

            monsters = []
            if values['copies'] > 1:
                for i in range(values['copies']):
                    name = f"{values['name']} {i + 1}"
                    monsters.append(Monster(name, values['init mod'], values['HP']))
                    monsters[i].roll_initiative()
            else:
                monsters = [Monster(values['name'], values['init mod'], values['HP'])]
                monsters[0].roll_initiative()

            self.name_entry.delete(0, last_index=len(self.name_entry.get()))
            self.HP_entry.delete(0, last_index=len(self.HP_entry.get()))
            self.initiative_entry.delete(0, last_index=len(self.initiative_entry.get()))
            self.copies.delete(0, last_index=len(self.copies.get()))

        return values, monsters


class Player_creator_frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Title of Box
        self.title = ctk.CTkLabel(self, text="Player Creation")
        self.title.grid(row=0, column=0, padx=10, pady=10)

        self.add_player_button = ctk.CTkButton(self, text="Add Player", command=master.add_player)
        self.add_player_button.grid(row=0, column=1, padx=10, pady=10)

        # Entry box for player character name
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Player Name")
        self.name_entry.grid(row=1, column=0, padx=10, pady=10)

        # Entry box for player character initiative
        self.initiative_entry = ctk.CTkEntry(self, placeholder_text="Player Initiative")
        self.initiative_entry.grid(row=2, column=0, padx=10, pady=10)

        # Entry box for player initiative mod
        self.initiative_mod_entry = ctk.CTkEntry(self, placeholder_text="Player Initiative Mod")
        self.initiative_mod_entry.grid(row=1, column=1, padx=10, pady=10)

    def get(self):
        values, player = None, None
        # check to make sure HP is an initiative integer
        init_entry = self.initiative_entry.get()
        init_is_valis = is_numbers(init_entry)

        # check to make sure
        mod_entry = self.initiative_mod_entry.get()
        init_mod_is_valid = is_numbers(mod_entry)

        if init_is_valis and init_mod_is_valid:
            values = {
                'name': self.name_entry.get(),
                'initiative': int(self.initiative_entry.get()),
                'init mod': int(self.initiative_mod_entry.get())
            }

            player = Player(values['name'], values['init mod'], values['initiative'])

        self.name_entry.delete(0, last_index=len(self.name_entry.get()))
        self.initiative_entry.delete(0, last_index=len(self.initiative_entry.get()))
        self.initiative_mod_entry.delete(0, last_index=len(self.initiative_mod_entry.get()))

        return values, player
