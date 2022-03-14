# 5eCombatTracker
A program for dungeon masters to track combat rounds, initiative, and lingering effects.

This will be a combat management tool for 5e DMs. 
In the first few iterations, I will be focused on creating flexible data structures to yield the DM complete and fluid control over combat no matter the circumstance.
Basically, I'm going to make a base program that can be used out of the box for any combat with little setup on the DM's side.
Also a primary concern will be GUI. I will learning to use tkinter during the beginning phases.

When the base program is polished, I will branch out and switch my focus to customization.
Some example features for the future include:
- Allowing DM to track monster stats in combat
  - Entering specific damage types
  - Accounting for monster regeneration
  - Accounting for legendary actions
  - Ability to pull up monster stats at any point for DM's reference
 
- Allowing DM to setup macros and presets
  - Allow DM to set shortcut keys for certain actions
  - Allow DM to setup and save multiple combat scenarios ahead of time

- Make GUI so all features stated above can be used with little to no learning curve

Features for now include:
- Initiative tracker
  - Allows DM to enter creature's name and initiative count
  - Allows DM to settle ties between characters
- Temporary effect tracker (measured at beginning of affected creature's turn)
  - Allows DMs to assign an effect a name and length during a creature's  turn
