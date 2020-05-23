import random
from .magic import Spell
from .Inventory import Items

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class person:
    def __init__(self, name, hp, mp, attk, dp, magic, items):
        self.hp_max = hp
        self.hp = hp
        self.mp_max = mp
        self.mp = mp
        self.attkl = attk - 10
        self.attkh = attk + 10
        self.dp = dp
        self.magic = magic
        self.items = items
        self.name = name
        self.action = ["ATTACK", "MAGIC", "ITEMS"]

    def generat_damage(self):
        return random.randrange(self.attkl, self.attkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.hp_max

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.mp_max

    def reduce_mp(self, cost):
        self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTION" + bcolors.ENDC)
        for item in self.action:
            print("    " + str(i) + "." + item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGICS" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + "." + spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_Items(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for items in self.items:
            print("    " + str(i) + "." + items["item"].name, ":",
                  items["item"].description, " (x" + str(items["quantity"]) + ")")
            i += 1

    def enemy_stat(self):
        e_bar = ""
        e_bar_ticks = (self.hp / self.hp_max) * 100 / 1.75 - 1

        while e_bar_ticks >= 0:
            e_bar += "♥"
            e_bar_ticks -= 1

        while len(e_bar) < 57:
            e_bar += " "

        e_string = str(self.hp) + "/" + str(self.hp_max)
        current_e = ""

        if len(e_string) < 9:
            decreased = 9 - len(e_string)

            while decreased > 0:
                current_e += " "
                decreased -= 1

            current_e += e_string
        else:
            current_e = e_string

        print("                             _________________________________________________________")
        print(bcolors.BOLD + self.name + "            " + current_e +
              "|" + bcolors.FAIL + e_bar + bcolors.ENDC + "|")

    def get_stats(self):

        hp_bar = ""
        hp_bar_ticks = (self.hp / self.hp_max) * 100/4
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.mp_max) * 100 / 10

        while hp_bar_ticks >= 0:
            hp_bar += "♥"
            hp_bar_ticks -= 1

        while mp_bar_ticks >= 0:
            mp_bar += "♥"
            mp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while len(mp_bar) < 11:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.hp_max)
        current_hp = ""

        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.mp_max)
        current_mp = ""

        if len(mp_string) < 5:
            decreasedmp = 5 - len(mp_string)

            while decreasedmp > 0:
                current_mp += " "
                decreasedmp -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                           __________________________                      ___________")
        print(bcolors.BOLD + self.name +"            " + current_hp +
               "|" + bcolors.OKGREEN + hp_bar +
              bcolors.ENDC + bcolors.BOLD + "|               " + current_mp + "|"
              + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "| ")
