from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from encounter import Encounter
from player import Player
from statblock import StatBlock
import random

commands = {"act": "Opens action menu.",
            "end": "Ends the current turn",
            "exit": "Ends the program.",
            "help": "Displays list of commands.",
            "move": "Changes your current position.",
            "profile": "Displays your stats."}

enc = Encounter("slot")
enc.add_entity(Player("Fjord", random.randint(1, 10000), "Orc", "Warlock", 10, StatBlock()))
enc.add_entity(Player("Jester Lavorre", random.randint(1, 10000), "Tiefling", "Cleric", 10, StatBlock()))
enc.add_entity(Player("Caleb Widowgast", random.randint(1, 10000), "Human", "Wizard", 10, StatBlock()))
enc.add_entity(Player("Yasha Nyoodrin", random.randint(1, 10000), "Aasimar", "Barbarian", 10, StatBlock()))
enc.add_entity(Player("Veth Brenatto", random.randint(1, 10000), "Goblin", "Rogue", 10, StatBlock()))

for i in range(5):
    hero = enc.get_entity(True, i)
    hero.set_coors(0, 0, 0)
    hero.set_stats("Current HP", 125)
    hero.set_stats("Max HP", 125)
    hero.set_stats("Animal Handling", -3)
enc.determineInitiative()

print("\nWelcome to the AutoCamp Demonstration v0.1")
enc.start_encounter()


while True:
    can_act = True
    actor = enc.get_actor()
    speed = actor.get_stat("Speed")

    print("\n[", actor.get_name(), "] what would you like to do?")
    ans = input("> ")

    if ans.lower() == "help":
        print("\nList of Commands:")
        for com, desc in commands.items():
            print("> ", com.ljust(7), "\t", desc)
        ans = input("> ")

    if ans.lower() == "act":
        print("\nPlease select an action to take:")
        print("> attack", "\n> use item", "\n> hold action")
        ans = input("> ")

        if ans.lower() == "back":
            continue

    elif ans.lower() == "move":
        if speed <= 0:
            print("You've exhausted all your movement!")
            continue
        else:
            print("You are currently at x = ", actor.get_coors()[0], ", y = ", actor.get_coors()[1])
            print("Where would you like to go?")
            x = y = -1
            cancel = False
            while True:
                if x == -1:
                    x = input("X: ")
                    if x == "cancel":
                        cancel = True
                        break
                    elif not isinstance(x, int):
                        print("[ER] Invalid input. Please try again.")
                        continue
                if y == -1:
                    y = input("Y: ")
                    if y == "cancel":
                        cancel = True
                        break
                    if not isinstance(y, int):
                        print("[ER] Invalid input. Please try again.")
                        continue

            if not cancel:
                enc.enc_move(actor, x, y, enc.get_map_tile_z(x, y))

    elif ans.lower() == "profile":
        enc.showStats()

    elif ans.lower() == "end":
        print("Your turn has ended.")
        enc.next_turn()
        continue



