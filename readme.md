# Initiative Tracker for TTRPGS

This is a simple tracker for TTRPGS with a graphical interface. It will
keep track of the health pools of multiple enemies as well as the current
place in the turn order.

This was mostly made for my personal use, additional features may be added in future *if* I decide that my personal 
needs grow to a point that more features are something that I want enough to be worth adding.

It is built for D&D5E, but if you wanted to adjust it for other systems I doubt that would be particularly difficult 

## Use:

### Adding NPCs/Enemies and player characters

NPC/Enemy creation
All fields must be filled in

| Field Name              | usage                                                           | Input Type |
|-------------------------|-----------------------------------------------------------------|------------|
| Creature Name           | Name of the creature, will be appended with numbers if multiple | Str        |
| Creature Max HP         | HP of the creature, system will not let HP go over this         | Int[^1]    |
| Creature Initiative Mod | The value to be added to the initiative roll                    | Int        |
| # of this monster       | Copies of this monster to add                                   | Int[^1]    |


Player character adding
All fields must be filled in

| Field Name            | usage                                                                        | Input Type |
|-----------------------|------------------------------------------------------------------------------|------------|
| Player Name           | Can be the name of the player or their character                             | Str        |        
| Player Initiative     | The player's initiative roll, system assumes the players roll for themselves | Int        |        
| Player Initiative Mod | This is used to break ties during the sorting (higher wins)                  | int        |       

After filling in the fields, press the "Add Monster(s)" or "Add Player" button to insert the configured creature(s) into the internal array.
Every time you do so the running tally of creatures will update with the total number of creatures that have been added so far.
Once you have added all the creatures you want, press the "Show Order" button to display all the creatures in the scrolling plane.

### During the combat

The "Reset Initiative" Button will empty the scrolling plane and delete all creatures from the internal storage, which 
will leave the tracker ready for you to insert new creatures.
The "Advance Turn" button will move the "Active" indication down the turn order, looping back to the top after it reaches the bottom.

Each of the NPC/Enemy tiles in the scrolling plane on the right displays its current and max health as a fraction,
the color changes at certain damage thresholds: Green means over half, orange is between a quarter and a half, and red
is under a quarter. The indicator will change to "Dead" when the creature's current HP reaches 0 (no matter how much damage was
done, there are caveats in place to prevent the stored value of current HP from staying below 0 in case the creature may
be healed later).

When pressed, the "Damage" and "Heal" buttons will bring up a dialog window for you to input the amount of damage/healing
to apply to the creature

[^1] must be >= 1