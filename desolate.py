#!/usr/bin/python3

import sys
import os
import random
import time


class Game:
    def __init__(self, day, peacekeepers, survivors, zombies, attackers, settler_count):
        self.day = day
        self.peacekeepers = peacekeepers
        self.survivors = survivors
        self.zombies = zombies
        self.attackers = attackers
        self.settler_count = settler_count

    def print_slow(self, str, delay=0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    def reset_console(self):
        print("\n")
        os.system('cls||clear')

    def fprint(self, str, delay=0):
        print("\n" + str)
        time.sleep(delay)

    def sprint(self, str, delay=0):
        print(str)
        time.sleep(delay)

    def commands(self):
        print("""\n Enter commands to interact with the world.\n
    'help'     ----    shows commands
    'quit'     ----    quits current game
    'n'        ----    go north
    's'        ----    go south
    'e'        ----    go east
    'w'        ----    go west
    'heal'     ----    restores health (costs medkit)
    'camp'     ----    restores energy (costs wood)
    'eat'      ----    restores hunger (costs food)
    'drink'    ----    restores thirst (costs water)
    'find'     ----    scavenge for items (costs energy)
    'day'      ----    shows current day
    'group'    ----    shows number of survivors in your group and your camp's fortifications
    'health'   ----    shows current health, energy, hunger and thirst
    'items'    ----    shows inventory
    'location' ----    shows current location""")

    def menu(self):
        self.reset_console()
        self.fprint("Desolate")
        print("Version 1.0")
        while True:
            action = input("\n> ")
            if action == "play":
                self.load_intro()
            elif action == "quit":
                sys.exit()
            elif action == "help":
                self.commands()
            elif action == "info":
                self.fprint("© Elijah Henderson 2021")
            else:
                self.fprint("Invalid option! Enter 'play' to launch the game,")
                print(
                    "'load' to load game, 'quit' to quit, 'info' for info, or 'help' for help.")

    def load_intro(self):
        self.reset_console()
        print("\n")
        self.print_slow("...loading...", 0.4)
        self.reset_console()
        self.fprint("Do you want to skip the intro?")
        self.fprint("(1) Yes (2) No")
        while True:
            a = input("\n> ")
            if a == "1":
                self.reset_console()
                self.fprint("You are at camp.")
                self.main()
            elif a == "2":
                self.intro()
            else:
                self.fprint("Invalid command!")

    def intro(self):
        self.reset_console()
        print("\n")
        self.print_slow(
            "The world fell apart when the dead rose from their graves.")
        self.print_slow(
            "The cities became overwhelmed quickly and the virus spread like a fire.")
        self.print_slow("Almost no one survived.")
        print("\n")
        self.print_slow(
            "Luckily, you prepared. You had the gear to go out into the countryside and ride out the apocalypse.")
        self.print_slow("But you're not the only one who had that idea.")
        self.print_slow(
            "If you want to survive, you'll have to make friends...")
        self.print_slow("Or prepare to fight to the death for resources.")
        print("\n")
        self.print_slow("You're on your own.")
        time.sleep(5)
        self.reset_console()
        self.fprint("You are at camp.")
        self.main()

    def reset_data(self):
        global game, player, camp
        game = Game(1, 100, 100, 100, 0, random.randint(0, 5))
        player = Player(0, 0, 100, 100, 100, 100, 0, 500, 0,
                        20, 0, 0, 0, "neutral", 100, False)
        camp = Camp(0, 0, 0, 0, 0, 0, 0, 0, 100)
        player.items.append("Knife")
        player.items.append("Pistol")
        self.load_intro()

    def play_again(self):
        self.fprint("Do you want to play again?", 1)
        print("(1) Yes (2) No")
        while True:
            a = input("\n> ")
            if a == "1":
                self.reset_data()
            elif a == "2":
                self.menu()
            else:
                self.fprint("Invalid command!")

    def check_victory(self):
        if self.zombies <= 0 and self.survivors <= 0 and self.peacekeepers <= 0:
            self.victory_conquest()

    def victory_conquest(self):
        time.sleep(2)
        self.print_slow(
            "The walking dead are no more... at least in these woods.")
        self.print_slow(
            "And you have defeated your enemies and you've made peace with the remaining survivors.")
        self.print_slow(
            "You have conquered the woods and you are slowly rebuilding civilization.")
        self.play_again()

    def peacekeeper_encounter(self):
        time.sleep(2)
        self.fprint("You see a man in a leather jacket weilding an AK-47.", 2)
        if player.peacekeepers_met is False:
            player.peacekeepers_met = True
            self.fprint(
                "'I represent a group called the Peacekeepers, son.'", 2)
            self.fprint("'The rules are simple in case we've never met.'", 2)
            self.fprint("'Give us your shit and we'll let you live.'", 2)
            self.fprint(
                "'We might even protect your camp from troublemakers if you're lucky.'", 2)
        else:
            self.fprint("'You ready to pay up?'", 2)
        self.fprint(
            "(1) 'Alright, here's my tribute.' (2) 'You've started a war that you can't finish, buddy.'")
        print("(3) 'Please, give me more time. I will have your tribute.'")
        while True:
            a = input("\n> ")
            if a == "1":
                player.peacekeeper_diplomacy = "alliance"
                player.pay()
                break
            elif a == "2":
                player.peacekeeper_diplomacy = "war"
                self.fprint(
                    "'Oh yeah? You're gonna cry for mercy before I'm done with you!'")
                player.fight("peacekeeper", 100, random.randint(
                    1, 25), "Rifle Bullet", True, "He")
                break
            elif a == "3":
                player.peacekeeper_diplomacy = "alliance"
                aggression = random.choice([True, False])
                if aggression is True:
                    player.pay()
                    break
                elif aggression is False:
                    self.fprint(
                        "'You know what? I'm in a good mood. I'll let you off this time.'", 1)
                    self.sprint("'But next time be ready to cough it up.'", 1)
                    self.fprint(
                        "'The Peacekeepers left without taking anything.'", 1)
                    break
            else:
                self.fprint("'What? Are you gonna cooperate, son?'")
            return True

    def peacekeeper_invasion(self):
        self.fprint("The Peacekeepers are raiding your camp!", 2)
        if camp.fortifications > 0:
            self.fprint(
                "The Peacekeepers failed to breech your fortifications.")
            damage = random.randint(1, 10)
            camp.fortifications -= damage
        else:
            self.attackers = random.randint(1, 10)
            while self.attackers > 0:
                camp.cpu_defend(100, random.randint(1, 25), "p")
                time.sleep(2)

    def survivor_invasion(self):
        self.fprint("Enemy survivors are attacking your camp!", 2)
        if camp.fortifications > 0:
            self.fprint(
                "Enemy survivors failed to breech your fortifications.")
            damage = random.randint(1, 10)
            camp.fortifications -= damage
        else:
            self.attackers = random.randint(1, 10)
            while self.attackers > 0:
                camp.cpu_defend(100, random.randint(1, 25), "s")
                time.sleep(2)

    def weaponsmith(self):
        price = (100 - player.weapon_condition) * random.randint(1, 11)
        if player.weapon_condition < 100:
            self.fprint(
                f"'Hello, stranger. I can repair your main weapon for {price} gold. Deal?'", 1)
            self.fprint("Yes(y) or no(n)?")
            while True:
                a = input("\n> ")
                if a == "y":
                    if player.gold >= price:
                        self.fprint("'Thanks! Stay vigilant, friend.'")
                        player.gold -= price
                        player.weapon_condition = 100
                        self.main()
                    else:
                        self.fprint(
                            "'I'm afraid you don't have enough gold, stranger. I'll see ya around. Goodbye!'")
                        self.main()
                elif a == "n":
                    self.fprint("'No problem. Stay vigilant, friend.'")
                    self.main()
                else:
                    self.fprint("What?")

    def peacekeeper(self):
        time.sleep(2)
        self.fprint("A Peacekeeper has emerged from the shadows.", 1)
        print("Will you fight(f) or run(r) or ask for peace(a)?")
        while True:
            a = input("\n> ")
            if a == "r":
                escape = random.choice([True, False])
                if escape == True:
                    time.sleep(2)
                    self.fprint("You manage to escape...")
                    break
                elif escape == False:
                    time.sleep(2)
                    self.fprint("You cannot escape! Prepare to fight.")
                    player.fight("peacekeeper", 100, random.randint(
                        1, 25), "Rifle Bulletbuy", True, "He")
                    break
            elif a == "f":
                player.fight("peacekeeper", 100, random.randint(
                    1, 25), "Shotgun Shell", True, "He")
                break
            elif a == "a":
                aggression = random.choice([True, False])
                if aggression == True:
                    self.fprint("The Peacekeeper pulls out a gun.", 2)
                    self.fprint(
                        "'You're the rebel who thinks he's above paying tribute.'", 1)
                    self.fprint("'There's nothing to talk about.'", 1)
                    player.fight("peacekeeper", 100, random.randint(
                        1, 25), "Pistol Bullet", True, "He")
                    break
                elif aggression == False:
                    self.fprint("The Peacekeeper lifts out his hand.", 2)
                    self.fprint(
                        "'How about a little amnesty? Don't betray us again.'", 1)
                    player.peacekeeper_diplomacy = "alliance"
                    player.pay()
                    break
            else:
                self.fprint("Invalid command!")

    def survivor(self):
        time.sleep(2)
        self.fprint("A survivor has emerged from the shadows.", 1)
        print("Will you fight(f) or run(r) or talk(t)?")
        while True:
            a = input("\n> ")
            if a == "r":
                escape = random.choice([True, False])
                if escape == True:
                    time.sleep(2)
                    self.fprint("You manage to escape...")
                    break
                elif escape == False:
                    time.sleep(2)
                    self.fprint("You cannot escape! Prepare to fight.")
                    break
            elif a == "f":
                player.fight("survivor", 100, random.randint(
                    1, 25), "Arrow", True, "He")
                break
            elif a == "t":
                aggression = random.choice([True, False])
                if aggression == True:
                    self.fprint("The survivor pulls out a gun.")
                    time.sleep(2)
                    self.fprint(
                        "'There's no room for the both of us in this world.'")
                    player.fight("survivor", 100, random.randint(
                        1, 25), "Arrow", True, "He")
                    break
                elif aggression == False:
                    self.dialog()
                    break
            else:
                self.fprint("Invalid command!")

    def dialog(self):
        self.fprint("The survivor lifts out his hand.", 2)
        self.fprint(
            "'Hello, friend. I mean you no harm. I'm just out here looking for supplies.'")
        while True:
            print(
                "(1) 'I mean no harm either. I'm just a traveler like yourself. Go in peace.'")
            print("(2) 'Oh, but I do mean harm!'")
            print("(3) 'Join me. I have a camp not far from here.'")
            a = input("\n> ")
            if a == "1":
                self.fprint("The survivor leaves in peace...")
                break
            if a == "2":
                break
            if a == "3":
                self.fprint(
                    "'We are stronger together friend! What would you have me do?'", 1)
                print("(1) 'You can help scavenge.' (2) You can help guard the camp.'")
                a = input("\n> ")
                if a == "1":
                    self.fprint("'Very well. I'll help scavenge!'", 1)
                    print("The survivor left for your camp.")
                    self.survivors -= 1
                    camp.scavengers += 1
                    break
                elif a == "2":
                    self.fprint("'Very well. I'll help guard the camp!'", 1)
                    print("The survivor left for your camp.")
                    self.survivors -= 1
                    camp.guards += 1
                    break
                else:
                    self.fprint("'What's that?'")
                return True

    def zombie(self):
        time.sleep(4)
        self.fprint("A zombie has emerged from the shadows.", 1)
        print("Will you fight(f) or run(r)?")
        while True:
            a = input("\n> ")
            if a == "r":
                escape = random.choice([True, False])
                if escape == True:
                    time.sleep(2)
                    self.fprint("You manage to escape...")
                    break
                elif escape == False:
                    time.sleep(2)
                    self.fprint("You cannot escape! Prepare to fight.")
                    player.fight("zombie", 100, random.randint(
                        1, 25), "Knife", True, "It")
                    break
            elif a == "f":
                player.fight("zombie", 100, random.randint(
                    1, 25), "Knife", True, "It")
                break

    def cabin(self):
        self.fprint("You found a cabin. Do you want to explore it?", 1)
        self.fprint("(1) Yes (2) No")
        while True:
            a = input("\n> ")
            if a == "1":
                event = random.choice([1, 2])
                if event == 1:
                    amount = random.randint(1, 51)
                    self.fprint(f"You find {amount} gold.")
                    player.gold += amount
                    break
                elif event == 2:
                    hurt = random.randint(1, 101)
                    self.fprint(
                        "A man comes out of the cabin and slashes you with a hatchet! You run away into the forest and escape.")
                    player.health -= hurt
                    break
            elif a == "2":
                self.fprint("You decide to move on...")
                break
            else:
                self.fprint("Invalid command!")

    def settlement(self):
        player.location = "settlement"
        self.fprint("You found a small settlement of survivors.")
        print("Enter 'buy', 'sell', or 'leave'.")
        while True:
            a = input("\n> ")
            if a == "leave":
                self.fprint("You left the settlement.")
                return True
            elif self.player_command(a):
                pass
            elif a == "buy":
                store_inventory = {
                    '1': ("Wood", random.randint(100, 150), "some Wood."),
                    '2': ("Water", random.randint(10, 20), "some Water."),
                    '3': ("Food", random.randint(1, 5), "some Food."),
                    '4': ("Medkit", random.randint(200, 250), "a Medkit."),
                    '5': ("Knife", random.randint(10, 20), "a Knife."),
                    '6': ("Dagger", random.randint(25, 45), "a Dagger."),
                    '7': ("Crossbow", random.randint(500, 1000), "a Crossbow."),
                    '8': ("Pistol", random.randint(2000, 3000), "a Pistol."),
                    '9': ("Shotgun", random.randint(4000, 5000), "a Shotgun."),
                    '10': ("Rifle", random.randint(6000, 7000), "a Rifle."),
                    '11': ("Pistol Bullet", random.randint(20, 40), "a Pistol Bullet."),
                    '12': ("Shotgun Shell", random.randint(50, 70), "a Shotgun Shell."),
                    '13': ("Rifle Bullet", random.randint(80, 100), "a Rifle Bullet."),
                    '14': ("Arrow", random.randint(10, 30), "an Arrow."),
                    '15': ("Grenade", random.randint(100, 200), "a Grenade.")
                }
                self.fprint("SETTLEMENT MARKETPLACE:\n")
                for key, item_data in store_inventory.items():
                    item, cost, description = item_data
                    print(f"a {item}({key}) for {cost} gold")
                self.fprint(f"You have {player.gold} gold.")
                self.fprint("Enter 'exit' if you don't want to buy anything.")
                while True:
                    a = input("\n> ")
                    if a in store_inventory:
                        item, cost, description = store_inventory[a]
                        player.buy(item, cost, description)
                    elif a == "exit":
                        self.fprint("Enter 'buy', 'sell', or 'leave'.")
                        break
                    else:
                        self.fprint("'I don't have that yet. Sorry, friend.'")
            elif a == "sell":
                store_inventory = {
                    '1': ("Wood", random.randint(100, 150), "some Wood."),
                    '2': ("Water", random.randint(10, 20), "some Water."),
                    '3': ("Food", random.randint(1, 5), "some Food."),
                    '4': ("Medkit", random.randint(200, 250), "a Medkit."),
                    '5': ("Knife", random.randint(10, 20), "a Knife."),
                    '6': ("Dagger", random.randint(25, 45), "a Dagger."),
                    '7': ("Crossbow", random.randint(500, 1000), "a Crossbow."),
                    '8': ("Pistol", random.randint(2000, 3000), "a Pistol."),
                    '9': ("Shotgun", random.randint(4000, 5000), "a Shotgun."),
                    '10': ("Rifle", random.randint(6000, 7000), "a Rifle."),
                    '11': ("Pistol Bullet", random.randint(20, 40), "a Pistol Bullet."),
                    '12': ("Shotgun Shell", random.randint(50, 70), "a Shotgun Shell."),
                    '13': ("Rifle Bullet", random.randint(80, 100), "a Rifle Bullet."),
                    '14': ("Arrow", random.randint(10, 30), "an Arrow."),
                    '15': ("Grenade", random.randint(100, 200), "a Grenade.")
                }
                self.fprint("SETTLEMENT MARKETPLACE:\n")
                for key, item_data in store_inventory.items():
                    item, cost, description = item_data
                    print(f"a {item}({key}) for {cost} gold")
                self.fprint(f"You have {player.gold} gold.")
                self.fprint("Enter 'exit' if you don't want to sell anything.")
                while True:
                    a = input("\n> ")
                    if a in store_inventory:
                        item, cost, description = store_inventory[a]
                        player.sell(item, cost, description)
                    elif a == "exit":
                        self.fprint("Enter 'buy', 'sell', or 'leave'.")
                        break
                    else:
                        self.fprint("You don't have that.")
            else:
                self.fprint("Invalid command!")

    def stranger(self):
        gift = random.choice(["Wood", "Water", "Food", "Medkit"])
        player.items.append(gift)
        if gift == "Wood":
            self.fprint(
                "A kind stranger saw you shiver and gave you some firewood.")
        elif gift == "Water":
            self.fprint(
                "A kind stranger noticed you panting and gave you a bottle of cold water.")
        elif gift == "Food":
            self.fprint(
                "A kind stranger heard your stomach growl and gave you some canned food.")
        elif gift == "Medkit":
            self.fprint(
                "A kind stranger noticed you were wounded and gave you a medical kit.")

    def check_event(self):
        self.check_victory()
        event = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                               11, 12, 13, 14, 15, 16, 17])
        if player.x == 0 and player.y == 0:
            event = 17
        if event == 1:
            self.weaponsmith()
        elif event == 2:
            if self.zombies > 0:
                self.zombie()
            else:
                self.fprint("The forest is quiet.")
        elif event == 3:
            if self.survivors > 0:
                self.survivor()
            else:
                self.fprint("You see no sign of survivors.")
        elif event == 4:
            self.cabin()
        elif event == 5:
            self.settlement()
        elif event == 6:
            self.stranger()
        elif event == 7:
            invasion_type = random.choice(["p", "s"])
            if invasion_type == "p" and self.peacekeepers > 0:
                if player.peacekeeper_diplomacy == "war":
                    self.peacekeeper_invasion()
                else:
                    self.fprint("A wolf howls in the distance.")
            elif invasion_type == "s" and self.survivors > 0:
                if player.peacekeeper_diplomacy == "alliance":
                    self.fprint(
                        "The Peacekeepers defended your camp from enemy survivors.")
                else:
                    self.survivor_invasion()
        elif event == 8:
            if player.peacekeeper_diplomacy == "war":
                self.peacekeeper()
            else:
                self.peacekeeper_encounter()
        elif event == 9:
            self.fprint("You hear sound of frogs and crickets.")
        elif event == 10:
            self.fprint("The wind gently blows against the trees.")
        elif event == 11:
            self.fprint("You shiver from the cold.")
        elif event == 12:
            self.fprint("The moon shines bright over the forest.")
        elif event == 13:
            self.fprint("You hear water rushing through a creek.")
        elif event == 14:
            self.fprint("The leaves crinkle underneath your feet.")
        elif event == 15:
            self.fprint(
                "You find the half-eaten remains of a man below your feet.")
        elif event == 16:
            self.fprint("You feel a great sense of dread come over you.")
        elif event == 17:
            pass

    def print_survivors(self):
        print("\nScavengers:", camp.scavengers)
        print("Guards:", camp.guards)
        print("Camp Fortifications:", str(camp.fortifications) + "%")

    def print_health(self):
        print("\nHealth:", player.health)
        print("Hunger:", player.hunger)
        print("Energy:", player.energy)
        print("Thirst:", player.thirst)

    def print_items(self):
        player.update_ammo()
        self.fprint("PACK:")
        print("Gold:", player.gold)
        print("Pistol Ammo:", player.pistol_ammo)
        print("Shotgun Ammo:", player.shotgun_ammo)
        print("Rifle Ammo:", player.rifle_ammo)
        print("Arrows:", player.arrows)
        print("Grenades:", player.grenades)
        for things in player.items:
            print(things)
        self.fprint("CAMP:")
        print("Gold:", camp.camp_gold)
        print("Pistol Ammo:", camp.camp_pistol_ammo)
        print("Shotgun Ammo:", camp.camp_shotgun_ammo)
        print("Rifle Ammo:", camp.camp_rifle_ammo)
        print("Arrows:", camp.camp_arrows)
        print("Grenades:", camp.camp_grenades)
        for things in camp.camp_items:
            print(things)

    def print_location(self):
        print(f"\nLocation: {player.x},{player.y}")

    def print_day(self):
        print("\nDay:", game.day)

    def update_state(self):
        player.lose_energy()
        player.lose_hunger()
        player.lose_thirst()
        camp.check_survivors()
        camp.check_camp()
        player.check_condition()

    def player_command(self, a):
        if a == "heal":
            player.heal()
        elif a == "eat":
            player.eat()
        elif a == "drink":
            player.drink()
        elif a == "camp":
            player.camp()
        elif a == "find":
            player.forage()
        elif a == "day":
            self.print_day()
        elif a == "group":
            self.print_survivors()
        elif a == "health":
            self.print_health()
        elif a == "items":
            self.print_items()
        elif a == "location":
            self.print_location()
        elif a == "help":
            self.commands()
        elif a == "quit":
            self.menu()
        else:
            return False
        return True

    def main(self):
        while True:
            a = input("\n> ")
            if a == "n":
                self.fprint("You went north.", 1)
                player.y += 1
                self.update_state()
                self.check_event()
            elif a == "s":
                self.fprint("You went south.")
                player.y -= 1
                self.update_state()
                self.check_event()
            elif a == "e":
                self.fprint("You went east.")
                player.x += 1
                self.update_state()
                self.check_event()
            elif a == "w":
                self.fprint("You went west.")
                player.x -= 1
                self.update_state()
                self.check_event()
            elif self.player_command(a):
                pass
            else:
                self.fprint("Invalid command!")


class Player:
    def __init__(self, x, y, health, hunger, energy, thirst, attack, gold, grenades, pistol_ammo,
                 shotgun_ammo, rifle_ammo, arrows, peacekeeper_diplomacy, weapon_condition,
                 peacekeepers_met):
        self.items = []
        self.x = x
        self.y = y
        self.health = health
        self.hunger = hunger
        self.energy = energy
        self.thirst = thirst
        self.attack = attack
        self.gold = gold
        self.grenades = grenades
        self.pistol_ammo = pistol_ammo
        self.shotgun_ammo = shotgun_ammo
        self.rifle_ammo = rifle_ammo
        self.arrows = arrows
        self.peacekeeper_diplomacy = peacekeeper_diplomacy
        self.weapon_condition = weapon_condition
        self.peacekeepers_met = peacekeepers_met

    def heal(self):
        if "Medkit" in self.items and self.health < 100:
            self.health += 25
            game.fprint("You perform first aid.")
            self.items.remove("Medkit")
            if self.health > 100:
                self.health = 100
        elif "Medkit" not in self.items:
            game.fprint("You don't have any medkits.")
        else:
            game.fprint("Your health is already full.")

    def camp(self):
        if "Wood" in self.items:
            self.items.remove("Wood")
            self.items = 100
            self.lose_hunger()
            self.lose_thirst()
            game.day += 1
            game.fprint("You camp out for the night.")
        else:
            game.fprint("You don't have any wood.")

    def eat(self):
        if "Food" in self.items and self.hunger < 100:
            self.items.remove("Food")
            self.hunger = 100
            game.fprint("You sit down for a meal. Your strength is restored.")
        elif "Food" not in self.items:
            game.fprint("You don't have any food to eat.")
        else:
            game.fprint("You aren't hungry.")

    def drink(self):
        if "Water" in self.items and self.thirst < 100:
            self.items.remove("Water")
            self.thirst = 100
            game.fprint(
                "You gulp down cold fresh water. Your thirst is quenched.")
        elif "Water" not in self.items:
            game.fprint("You don't have any water to drink.")
        else:
            game.fprint("You aren't thirsty.")

    def lose_health(self):
        self.health -= 1
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            self.die()

    def lose_energy(self):
        self.energy -= random.randint(1, 6)
        if self.energy < 0:
            self.energy = 0
        if self.energy == 0:
            self.lose_health()

    def lose_hunger(self):
        self.hunger -= random.randint(1, 6)
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger == 0:
            self.lose_health()

    def lose_thirst(self):
        self.thirst -= random.randint(1, 6)
        if self.thirst < 0:
            self.thirst = 0
        if self.thirst == 0:
            self.lose_health()

    def forage(self):
        self.lose_energy()
        find = random.randint(1, 10)
        item_found = random.choice(["Wood", "Water", "Food", "Medkit"])
        if find <= 3:
            game.fprint(f"You found {item_found}!")
            self.items.append(item_found)
        else:
            game.fprint("You couldn't find anything!")

    def update_ammo(self):
        total_pistol_ammo = self.items.count("Pistol Bullet")
        total_shotgun_ammo = self.items.count("Shotgun Shell")
        total_rifle_ammo = self.items.count("Rifle Bullet")
        total_arrows = self.items.count("Arrow")
        total_grenades = self.items.count("Grenade")
        self.pistol_ammo += total_pistol_ammo
        self.shotgun_ammo += total_shotgun_ammo
        self.rifle_ammo += total_rifle_ammo
        self.arrows += total_arrows
        self.grenades += total_grenades
        while "Pistol Bullet" in self.items:
            self.items.remove("Pistol Bullet")
        while "Shotgun Shell" in self.items:
            self.items.remove("Shotgun Shell")
        while "Rifle Bullet" in self.items:
            self.items.remove("Rifle Bullet")
        while "Arrow" in self.items:
            self.items.remove("Arrow")
        while "Grenade" in self.items:
            self.items.remove("Grenade")

    def sell(self, item, cost, description):
        if item not in self.items:
            game.fprint("I don't have one to sell!")
        else:
            self.items.remove(item)
            self.gold += cost
            game.fprint(f"You sold {description}")

    def buy(self, item, cost, description):
        if self.gold >= cost:
            self.items.append(item)
            self.gold -= cost
            game.fprint("'Here you go!'")
            game.fprint(f"You bought {description}")
        else:
            game.fprint("Sorry, you don't have enough for this.")

    def pay(self):
        game.fprint(
            "You give all the supplies you're carrying with you to the Peacekeepers.", 2)
        self.gold = 0
        self.pistol_ammo = 0
        self.shotgun_ammo = 0
        self.rifle_ammo = 0
        self.arrows = 0
        self.grenades = 0
        self.items.clear()

    def die(self):
        time.sleep(2)
        game.fprint("You are dead.", 2)
        game.fprint(f"You survived for {game.day} days.", 2)
        game.play_again()

    def lose_weapon_condition(self):
        self.weapon_condition -= random.randint(1, 5)

    def check_condition(self):
        if self.weapon_condition <= 0:
            self.weapon_condition = 0
            if "Rifle" in self.items:
                self.items.remove("Rifle")
                game.fprint("Your rifle has broken beyond repair.")
            elif "Shotgun" in self.items:
                self.items.remove("Shotgun")
                game.fprint("Your shotgun has broken beyond repair.")
            elif "Pistol" in self.items:
                self.items.remove("Pistol")
                game.fprint("Your pistol has broken beyond repair.")
            elif "Crossbow" in self.items:
                self.items.remove("Crossbow")
                game.fprint("Your crossbow has broken beyond repair.")
            elif "Dagger" in self.items:
                self.items.remove("Dagger")
                game.fprint("Your dagger has broken beyond repair.")
            elif "Knife" in self.items:
                self.items.remove("Knife")
                game.fprint("Your knife has broken beyond repair.")

    def fight(self, enemy, enemy_health, enemy_attack, item_drop, unit, pronoun):
        self.update_ammo()
        time.sleep(2)
        while True:
            if self.grenades > 0:
                self.attack = random.randint(80, 100)
                self.grenades -= 1
                game.fprint("You are equipped with a Grenade.")
            elif "Rifle" in self.items and self.rifle_ammo > 0:
                self.attack = random.randint(20, 80)
                self.rifle_ammo -= 1
                game.fprint("You are equipped with a Rifle.")
                self.lose_weapon_condition()
            elif "Shotgun" in self.items and self.shotgun_ammo > 0:
                self.attack = random.randint(20, 60)
                self.shotgun_ammo -= 1
                game.fprint("You are equipped with a Shotgun.")
                self.lose_weapon_condition()
            elif "Pistol" in self.items and self.pistol_ammo > 0:
                self.attack = random.randint(20, 40)
                self.pistol_ammo -= 1
                game.fprint("You are equipped with a Pistol.")
                self.lose_weapon_condition()
            elif "Crossbow" in self.items and self.arrows > 0:
                self.attack = random.randint(20, 30)
                self.arrows -= 1
                game.fprint("You are equipped with a Crossbow.")
                self.lose_weapon_condition()
            elif "Dagger" in self.items:
                self.attack = random.randint(10, 20)
                game.fprint("You are equipped with a Dagger.")
                self.lose_weapon_condition()
            elif "Knife" in self.items:
                self.attack = random.randint(5, 10)
                game.fprint("You are equipped with a Knife.")
                self.lose_weapon_condition()
            else:
                game.fprint("You are unarmed!")
                self.attack = random.randint(1, 5)
            time.sleep(2)
            enemy_health -= self.attack
            if enemy_health > 0:
                if unit == True:
                    game.fprint(
                        f"You strike the {enemy}! {pronoun} has {enemy_health} health left.", 3)
                else:
                    game.fprint(
                        f"You strike {enemy}! {pronoun} has {enemy_health} health left.", 3)
            if enemy_health <= 0:
                if unit == True:
                    game.fprint(f"You slayed the {enemy}.", 2)
                else:
                    game.fprint(f"You slayed {enemy}.", 2)
                find_chance = random.randint(1, 10)
                if find_chance <= 3:
                    amount = random.randint(1, 100)
                    self.gold += amount
                    game.fprint(f"You found {amount} gold.", 2)
                self.items.append(item_drop)
                game.fprint(f"You found a {item_drop}.", 2)
                return True
            self.health -= enemy_attack
            if self.health <= 0:
                if unit == True:
                    game.fprint(f"The {enemy} strikes you down...", 3)
                else:
                    game.fprint(f"{enemy} strikes you down...", 3)
                self.die()
            if enemy_attack > 0:
                if unit == True:
                    game.fprint(
                        f"The {enemy} strikes at you! You have {self.health} health left.", 3)
                else:
                    game.fprint(
                        f"{enemy} strikes at you! You have {self.health} health left.", 3)


class Camp:
    def __init__(self, camp_gold, camp_pistol_ammo, camp_shotgun_ammo,
                 camp_rifle_ammo, camp_arrows, camp_grenades,
                 scavengers, guards, fortifications):
        self.camp_items = []
        self.camp_gold = camp_gold
        self.camp_pistol_ammo = camp_pistol_ammo
        self.camp_shotgun_ammo = camp_shotgun_ammo
        self.camp_rifle_ammo = camp_rifle_ammo
        self.camp_arrows = camp_arrows
        self.camp_grenades = camp_grenades
        self.scavengers = scavengers
        self.guards = guards
        self.fortifications = fortifications

    def cpu_defend(self, enemy_health, enemy_attack, enemy_type):
        cpu_health = 100
        if camp.guards == 0:
            if enemy_type == "p":
                game.fprint("You camp was overrun by the peacekeepers.", 2)
            elif enemy_type == "s":
                game.fprint("You camp was overrun by enemy survivors.", 2)
            game.fprint("All of your supplies at camp were stolen.")
            self.camp_gold = 0
            self.camp_pistol_ammo = 0
            self.camp_shotgun_ammo = 0
            self.camp_rifle_ammo = 0
            self.camp_arrows = 0
            self.camp_grenades = 0
            self.camp_items.clear()
            game.main()
        while True:
            cpu_attack = random.randint(50, 101)
            enemy_health -= cpu_attack
            if enemy_health <= 0:
                if enemy_type == "p":
                    game.peacekeeprs -= 1
                    game.fprint("A survivor slayed a peacekeeper.")
                elif enemy_type == "s":
                    game.survivors -= 1
                    game.fprint("A survivor slayed an enemy survivor.")
                game.attackers -= 1
                return True
            cpu_health -= enemy_attack
            if cpu_health <= 0:
                time.sleep(2)
                camp.guards -= 1
                game.zombies += 1
                if enemy_type == "p":
                    game.fprint(
                        "One of your survivors was killed by a peacekeeper while defending your camp...", 1)
                elif enemy_type == "s":
                    game.fprint(
                        "One of your survivors was killed by an enemy survivor while defending your camp...", 1)
                return True

    def cpu_fight(self, zombie_health, zombie_attack):
        cpu_health = 100
        escape = random.choice([True, False])
        if game.zombies <= 0:
            escape = True
        if escape == True:
            return True
        while True:
            cpu_attack = random.randint(50, 100)
            zombie_health -= cpu_attack
            if zombie_health <= 0:
                game.zombies -= 1
                game.fprint("A survivor slayed a zombie.")
                return True
            cpu_health -= zombie_attack
            if cpu_health <= 0:
                time.sleep(2)
                game.fprint(
                    "One of your survivors was eaten by the dead on a scavenging mission...", 1)
                camp.scavengers -= 1
                game.zombies += 1
                return True

    def cpu_scavenge(self):
        scavenge_chance = random.randint(1, 10)
        if scavenge_chance <= 3:
            item_type = random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            gain = 0
            if item_type == 1:
                item = "gold"
                gain = random.randint(1, 10)
                self.camp_gold += gain
            elif item_type == 2:
                item = "wood"
                gain = random.randint(1, 10)
                for i in range(gain):
                    self.camp_items.append("Wood")
            elif item_type == 3:
                item = "water"
                gain = random.randint(1, 10)
                for i in range(gain):
                    self.camp_items.append("Water")
            elif item_type == 4:
                item = "food"
                gain = random.randint(1, 10)
                for i in range(gain):
                    self.camp_items.append("Food")
            elif item_type == 5:
                item = "medkits"
                gain = random.randint(1, 10)
                for i in range(gain):
                    self.camp_items.append("Medkit")
            elif item_type == 6:
                item = "pistol bullets"
                gain = random.randint(1, 10)
                self.camp_pistol_ammo += gain
            elif item_type == 7:
                item = "shotgun shells"
                gain = random.randint(1, 10)
                self.camp_shotgun_ammo += gain
            elif item_type == 8:
                item = "rifle bullets"
                gain = random.randint(1, 10)
                self.camp_rifle_ammo += gain
            elif item_type == 9:
                item = "arrows"
                gain = random.randint(1, 10)
                self.camp_arrows += gain
            elif item_type == 10:
                item = "grenades"
                gain = random.randint(1, 10)
                self.camp_grenades += gain
            game.fprint(
                f"One of your survivors scavenged for the camp and found {gain} {item}.", 1)
            return True
        else:
            game.fprint(
                f"One of your survivors scavenged for the camp but found nothing.", 1)
            return True

    def check_survivors(self):
        for i in range(self.scavengers):
            self.cpu_fight(100, random.randint(1, 25))
            time.sleep(1)
            self.cpu_scavenge()

    def check_camp(self):
        if player.x == 0 and player.y == 0:
            game.fprint("You are at camp.")
            player.gold += self.camp_gold
            if self.camp_gold > 0:
                game.fprint(f"You retrieved {self.camp_gold} gold from camp.")
            self.camp_gold = 0
            player.pistol_ammo += self.camp_pistol_ammo
            if self.camp_pistol_ammo > 0:
                game.fprint(
                    f"You retrieved {self.camp_pistol_ammo} pistol bullets from camp.")
            self.camp_pistol_ammo = 0
            player.shotgun_ammo += self.camp_shotgun_ammo
            if self.camp_shotgun_ammo > 0:
                game.fprint(
                    f"You retrieved {self.camp_shotgun_ammo} shotgun shells from camp.")
            self.camp_shotgun_ammo = 0
            player.rifle_ammo += self.camp_rifle_ammo
            if self.camp_rifle_ammo > 0:
                game.fprint(
                    f"You retrieved {self.camp_rifle_ammo} rifle bullets from camp.")
            self.camp_rifle_ammo = 0
            player.arrows += self.camp_arrows
            if self.camp_arrows > 0:
                game.fprint(
                    f"You retrieved {self.camp_arrows} arrows from camp.")
            self.camp_arrows = 0
            player.grenades += self.camp_grenades
            if self.camp_grenades > 0:
                game.fprint(
                    f"You retrieved {self.camp_grenades} grenades from camp.")
            self.camp_grenades = 0
            if "Wood" in self.camp_items:
                gain = self.camp_items.count("Wood")
                for i in range(gain):
                    player.items.append("Wood")
                game.fprint(f"You retrieved {gain} wood from camp.")
            if "Water" in self.camp_items:
                gain = self.camp_items.count("Water")
                for i in range(gain):
                    player.items.append("Water")
                game.fprint(f"You retrieved {gain} water from camp.")
            if "Food" in self.camp_items:
                gain = self.camp_items.count("Food")
                for i in range(gain):
                    player.items.append("Food")
                game.fprint(f"You retrieved {gain} food from camp.")
            if "Medkit" in self.camp_items:
                gain = self.camp_items.count("Medkit")
                for i in range(gain):
                    player.items.append("Medkit")
                game.fprint(f"You retrieved {gain} medkits from camp.")
            self.camp_items.clear()
            if self.fortifications < 100:
                damage = 100 - self.fortifications
                total = damage * 2
                game.fprint(
                    f"Would you like to hire a survivor to repair your fortifications for {total} gold?")
                print("(1) Yes (2) No")
                while True:
                    a = input("\n> ")
                    if a == "1" and player.gold >= total:
                        player.gold -= total
                        self.fortifications = 100
                        game.fprint(
                            "Your camp's fortifications were repaired.")
                        break
                    elif a == "1" and player.gold <= total:
                        game.fprint("You don't have enough gold.")
                        break
                    elif a == "2":
                        break
                    else:
                        game.fprint("Invalid command!")
            if camp.camp_gold > 0:
                game.fprint(
                    "Enter the amount of gold you want to withdrawal.")
                print("Enter 0 if you've don't want to withdrawal any gold.")
                while True:
                    a = input("\n> ")
                    if a == "0":
                        fprint("You decided to keep your gold in your pack.")
                        break
                    elif a.isdigit() and int(a) > camp.camp_gold:
                        game.fprint("You don't have that much gold at camp.")
                    elif a.isdigit():
                        player.gold += int(a)
                        camp.camp_gold -= int(a)
                        game.fprint(f"You withdrew {a} gold from camp.")
                        break
                    else:
                        game.fprint("Enter a number.")
            if player.gold > 0:
                game.fprint(
                    "Enter the amount of gold you want to store.")
                print("Enter 0 if you've don't want to store any gold.")
                while True:
                    a = input("\n> ")
                    if a == "0":
                        break
                    elif a.isdigit() and int(a) > player.gold:
                        game.fprint(
                            "You don't have that much gold in your pack.")
                    elif a.isdigit():
                        camp.camp_gold += int(a)
                        player.gold -= int(a)
                        game.fprint(f"You stashed {a} gold at camp.")
                        break
                    else:
                        game.fprint("Enter a number.")


game = Game(1, 100, 100, 100, 0, random.randint(0, 5))
player = Player(0, 0, 100, 100, 100, 100, 0, 500, 0,
                20, 0, 0, 0, "neutral", 100, False)
camp = Camp(0, 0, 0, 0, 0, 0, 0, 0, 100)
player.items.append("Knife")
player.items.append("Pistol")
game.menu()
