import random

from Classes.game import person, bcolors
from Classes.magic import Spell
from Classes.Inventory import Items


# Create Black Magic
Fire = Spell("Fire", 10, 100, "Black")
Thunder = Spell("Thunder", 10, 100, "Black")
Blizzard = Spell("Blizzard", 10, 100, "Black")
Meteor = Spell("Meteor", 20, 200, "Black")
Quake = Spell("Quake", 15, 150, "Black")

# Create White Magic
Cure = Spell("Cure", 12, 120, "White")
Cura = Spell("Cura", 18, 200, "White")

# Create some Item
potion = Items("Potion", "potion", "Heals for 50 HP", 50)
hipotion = Items("Hi-Potion", "potion", "Heals for 100 HP", 100)
superportion = Items("Super-Potion", "potion", "Heals for 500 HP", 500)
elixir = Items("Elixir", "elixir", "Full restores HP/MP of One party Member", 9999)
hielixir = Items("Super-Elixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Items("Grenade", "attack", "deals 500 damage", 500)

player_magic = [Thunder, Blizzard, Meteor, Cura, Cure, Quake]  # initialized player Magics list
player_spells = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                 {"item": superportion, "quantity": 3}, {"item": elixir, "quantity": 2},
                 {"item": hielixir, "quantity": 1}, {"item": grenade, "quantity": 1}]  # initialized player Items list

player1 = person("ORION :", 460, 65, 60, 34, player_magic, player_spells)  # Player initialization
player2 = person("T0X1C :", 460, 65, 60, 34, player_magic, player_spells)  # Player2 initialization
player3 = person("B15H0P:", 460, 65, 60, 34, player_magic, player_spells)  # Player3 initialization
enemy = person("ENEMY :", 2400, 65, 45, 25, [], [])  # Enemy initialization

players = [player1, player2, player3]
running = True
i = 0

print("\n\n")
print("===========================================")
print(bcolors.FAIL + bcolors.BOLD + "T0X1C COMMANDLINE BATTLE GAME" + bcolors.ENDC)
while running:
    print("===========================================")
    print("\n\n")
    print("NAME:                               HP:                                        MP:")

    for player in players:
        player.get_stats()
    enemy.enemy_stat()
    print("\n")
    for player in players:
        player.choose_action()
        player_choice = input("Select Action: ")
        action_index = int(player_choice) - 1

        if action_index == 0:
            player_dmg = player.generat_damage()
            enemy.take_damage(player_dmg)
            print("You attacked for", player_dmg,
                  "Points of damage.")

        elif action_index == -1:
            continue

        elif action_index == 1:
            player.choose_magic()
            spell_index = int(input("Select Magic: ")) - 1
            spell = player.magic[spell_index]
            print("Name:", spell.name, "Spell ,",
                  "Charges:", spell.cost)

            if player.get_mp() <= int(spell.cost):
                print(bcolors.FAIL + "you don't have enough Magic Power cos your Magic Power is :",
                      str(player.get_mp()) + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                spell_dmg = spell.generate_spell_damage()
                player.heal(spell_dmg)
                print(bcolors.OKBLUE + "/n" + spell.name + "heals for", str(spell_dmg), "HP." + bcolors.ENDC)

            elif spell.type == "Black":
                spell_dmg = spell.generate_spell_damage()
                player.reduce_mp(spell.cost)
                enemy.take_damage(spell.dmg)
                print("You attacked for", spell_dmg, "Points of damage.")

        elif action_index == 2:
            player.choose_Items()
            Item_choice = int(input("Choose item: ")) - 1
            items = player.items[Item_choice]["item"]
            if player.items[Item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            quantity = player.items[Item_choice]["quantity"] - 1
            player.items[Item_choice]["quantity"] = quantity

            index = Item_choice

            if index == -1:
                continue

            if items.type == "potion":
                player.heal(items.prop)
                print(bcolors.OKGREEN + "\n" + items.name + " heals for", str(items.prop), "HP" + bcolors.ENDC)
            elif items.type == "elixir":
                player.hp = player.hp_max
                player.mp = player.mp_max
                print(bcolors.OKGREEN + "\n" + items.name + " Fully restores HP/MP." + bcolors.ENDC)
            elif items.type == "attack":
                enemy.take_damage(items.prop)
                print(bcolors.FAIL + "\n" + items.name + " deals", str(items.prop), "points of damage" + bcolors.ENDC)


        else:
            print("Invalid Action!!!")
            continue

    enemy_choice = 1
    enemy_target = random.randrange(0, 3)

    enemy_dmg = enemy.generat_damage()
    players[enemy_target].take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg,
          "Points of damage.")

    print("========================================================")

    if player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD +
              "You lost the battle to your Enemy, Try harder next time Loser!!!" + bcolors.ENDC)
        players.get_stats()
        enemy.get_stats()
        break

    elif enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "Long Live the King. Amazing you won the battle Motherfucker!!!" + bcolors.ENDC)
        players.get_stats()
        enemy.get_stats()
        break

    else:
        continue
