#heavaly inspired by undertale and deltarune...

import os
import random
import time
import pyjokes
from colorama import init, Fore, Style
import pygame
print("\n" * 10)
pygame.mixer.init()

init()
if os.getlogin().lower().capitalize() == "Nilo" or os.getlogin().capitalize() == "Suzy" or os.getlogin().capitalize() == "Noël" or os.getlogin().capitalize() == "Noel":
    rere = os.getlogin().lower().capitalize() + "a"
else:
    rere = os.getlogin().lower().capitalize()


player = {"name": rere, "hp": 100, "maxhp": 100, "mp": 0, "maxmp": 100, "mpgain": 10}
party2 = {"name": "Nilo", "hp": 70, "maxhp": 70, "mp": 0}
party3 = {"name": "Suzy", "hp": 150, "maxhp": 150, "mp": 0} #not a refrence to susie deltarune or the nitendo swich exscluseve undertale fun event. actauly its both.
#party4 = {"name": "Noël", "hp": 40, "maxhp": 40, "mp": 0}

items = ["cake", "singuler chip", "breathmint", "flatsoda", "AAA battery", "noddles", "sour pach kids", "undertale game cartrege", "glass shard", "pocket lint", "expired coupon", "rubber duck", "friendship bracelet", "emotional support pickle", "moms gross meatloaf", "note with wifi password on it", "one of Noël's ugly cristmas sweaters"]
in_battle = False
spared = None

def trun():
    global player, party2, party3, in_battle, ena, maxmp, spared
    trun = 1
    
    while trun != 4:
        
        print("\n")

        if trun == 1:
            
            if player["hp"] > player["maxhp"]:
                player["hp"] = player["maxhp"]
            elif player["hp"] < -player["maxhp"]:
                player["hp"] = -player["maxhp"]
            
            if player["hp"] <= 0:
                print(f"{player['name']} cannot attack because they are too hurt!")
                player["hp"] = player["hp"] + random.randint(10, 25)
                pass
            
            if ena["spare"] >= 100:
                in_battle = False
                print(f"you spared {ena['name']}! ")
                spared = True
                return
            
            print(f"{player['name']}:")
            
            eee = player["hp"] / 5
            ttt = (player["maxhp"] - player["hp"]) / 5
            while eee > 0:
                print(Fore.GREEN + "█" + Style.RESET_ALL, end="")
                eee = eee - 1
            while ttt > 0:
                print(Fore.RED + "█" + Style.RESET_ALL, end="") #Fore.RED + "Danger Zone!" + Style.RESET_ALL
                ttt = ttt - 1
            print(f" {player['hp']}/{player['maxhp']} HP")
                
            ee = player["mp"] / 5
            tt = (player["maxmp"] - player["mp"]) / 5
            while ee > 0:
                print(Fore.MAGENTA + "█" + Style.RESET_ALL, end="")
                ee = ee - 1
            while tt > 0:
                print(Fore.LIGHTRED_EX + "█" + Style.RESET_ALL, end="") #Fore.RED + "Danger Zone!" + Style.RESET_ALL
                tt = tt - 1
            print(f" {player['mp']}/{player['maxmp']} MP")
            
            print("1.fight\n2.act\n3.item\n4.magic\n5.focus")
            print("\n")
            trun = trun + 1
            
            try:
                op = int(input("what to do?: "))
                if op > 5 or op < 1:
                    print("you frose up like a deer in headlights. trun skiped.")
                    op = "skip"
            except:
                print("you frose up like a deer in headlights. trun skiped.")
                op = "skip"
            
            if op == 1:
                dmg = random.randint(25, 125)
                ena["hp"] = ena["hp"] - dmg
                print(f"you did {dmg}dmg!")
            elif op == 2:
                print(f'you told a joke to {ena["name"]}: "{pyjokes.get_joke()}" (+{ena["spae"]}% spare)!')
                ena["spare"] = ena["spare"] + ena["spae"]
            elif op == 3:
                hpre = random.randint(50, 100)
                print(f"you ate {random.choice(items)}, recovered {hpre} hp!")
                player["hp"] = player["hp"] + hpre
                
                if player["hp"] >= player["maxhp"]:
                    player["hp"] = player["maxhp"]
            elif op == 4:
                print("testing!")
            elif op == 5:
                print(f"you focused... gained {player['mpgain']} MP!")
                player["mp"] = player["mp"] + player['mpgain']
            elif op == "skip":
                pass
            
            if ena["hp"] == 0 or ena["hp"] <= 0:
                print(f"you beat {ena['name']}!")
                in_battle = False
                trun = 4
                spared = False
        
        elif trun == 2:
            
            if party2["hp"] > party2["maxhp"]:
                party2["hp"] = party2["maxhp"]
            elif party2["hp"] < -party2["maxhp"]:
                party2["hp"] = -party2["maxhp"]
            
            if party2["hp"] <= 0:
                print(f"{party2['name']} cannot attack because they are too hurt!")
                party2["hp"] = party2["hp"] + random.randint(10, 25)
                pass
            
            if ena["spare"] >= 100:
                in_battle = False
                print(f"{player['name']} spared {ena['name']}! ")
                spared = True
                return
            
            print(f"{party2['name']}:")
            
            eee = party2["hp"] / 5
            ttt = (party2["maxhp"] - party2["hp"]) / 5
            
            while eee > 0:
                print(Fore.GREEN + "█" + Style.RESET_ALL, end="")
                eee = eee - 1
            while ttt > 0:
                print(Fore.RED + "█" + Style.RESET_ALL, end="") #Fore.RED + "Danger Zone!" + Style.RESET_ALL
                ttt = ttt - 1
            
            print(f" {party2['hp']}/{party2['maxhp']}")
            
            print("1.fight\n2.act\n3.item")
            print("\n")
            trun = trun + 1
            
            try:
                op = int(input("what to do?: "))
                if op > 3 or op < 1:
                    print(f"{party2['name']} frose up like a deer in headlights. trun skiped.")
                    op = "skip"
            except:
                print(f"{party2['name']} frose up like a deer in headlights. trun skiped.")
                op = "skip"
            
            if op == 1:
                dmg = random.randint(15, 75)
                ena["hp"] = ena["hp"] - dmg
                print(f"{party2['name']} did {dmg}dmg!")
            elif op == 2:
                print(f'{party2["name"]} triped while trying to grab a butterfly, {ena["name"]} laughed. (+{ena["spae"]}% spare)!')
                ena["spare"] = ena["spare"] + ena["spae"]
            elif op == 3:
                hpre = random.randint(50, 100)
                print(f"{party2['name']} absorbed {random.choice(items)}, recovered {hpre} hp!")
                party2["hp"] = party2["hp"] + hpre
                
                if party2["hp"] >= party2["maxhp"]:
                    party2["hp"] = party2["maxhp"]
            elif op == "skip":
                pass
            
            if ena["hp"] == 0 or ena["hp"] <= 0:
                print(f"{party2['name']} beat {ena['name']}!")
                in_battle = False
                trun = 4
                spared = False
                
        if trun == 3:
            
            if party3["hp"] > party3["maxhp"]:
                party3["hp"] = party3["maxhp"]
            elif party3["hp"] < -party3["maxhp"]:
                party3["hp"] = -party3["maxhp"]
            
            if party3["hp"] <= 0:
                print(f"{party3['name']} cannot attack because they are too hurt!")
                party3["hp"] = party3["hp"] + random.randint(10, 25)
                pass
            
            if ena["spare"] >= 100:
                in_battle = False
                print(f"{player['name']} spared {ena['name']}! ")
                spared = True
                return
            
            print(f"{party3['name']}:")
            
            eee = party3["hp"] / 5
            ttt = (party3["maxhp"] - party3["hp"]) / 5
            
            while eee > 0:
                print(Fore.GREEN + "█" + Style.RESET_ALL, end="")
                eee = eee - 1
            while ttt > 0:
                print(Fore.RED + "█" + Style.RESET_ALL, end="") #Fore.RED + "Danger Zone!" + Style.RESET_ALL
                ttt = ttt - 1
            
            print(f" {party3['hp']}/{party3['maxhp']}")
            
            print("1.fight\n2.act\n3.item")
            print("\n")
            trun = trun + 1
            
            try:
                op = int(input("what to do?: "))
                if op > 3 or op < 1:
                    print(f"{party3['name']} curled up and went to sleep. trun skiped.")
                    op = "skip"
            except:
                print(f"{party3['name']} curled up and went to sleep. trun skiped.")
                op = "skip"
            
            if op == 1:
                dmg = random.randint(75, 200)
                ena["hp"] = ena["hp"] - dmg
                print(f"{party3['name']} did {dmg}dmg!")
            elif op == 2:
                if random.randint(1, 10) == 10:
                    print(f'{party3["name"]} bit {ena["name"]}, {ena["name"]} became {player["name"]}s friend so you can end the battle faster! (+100% spare)!')
                    ena["spare"] = 100
                else:
                    print(f'{party3["name"]} yelled at {ena["name"]} to stop fisghting them. (+{ena["spae"]}% spare)!')
                    ena["spare"] = ena["spare"] + ena["spae"]
            elif op == 3:
                hpre = random.randint(50, 100)
                print(f"{party3['name']} ate {random.choice(items)}, recovered {hpre} hp!")
                party3["hp"] = party3["hp"] + hpre
                
                if party3["hp"] >= party3["maxhp"]:
                    party3["hp"] = party3["maxhp"]
            elif op == "skip":
                pass
            
            if ena["hp"] == 0 or ena["hp"] <= 0:
                print(f"{party3['name']} beat {ena['name']}!")
                in_battle = False
                trun = 4
                spared = False

def battle(b):
    global player
    global party2
    global party3
    global in_battle
    global ena
    global atk
    in_battle = True
    
    if b == -1: #nedigive numberd indatcate test enamys.
        ena = {"name": "test eanamy sans undertale", "hp": 1, "spare": 0, "spae": 25, "taunt": ["its a butiful day outside", "wanta have a bad time?", "erererer", "im just a janoter", "i 'befreinded' your mom last night"]}
    elif b == -2:
        ena = {"name": "test eanamy god", "hp": float("inf"), "spare": 99., "spae": 1, "taunt": ['glorp: "gleep"', 'glorp: "blorp"', 'glorp: "glap"']}
    elif b == -3:
        ena = {"name": "test eanamy glorp", "hp": 200, "spare": 0, "spae": 15, "taunt": ['glorp: "gleep"', 'glorp: "blorp"', 'glorp: "glap"']}
    elif b == 1: #boss
        ena = {"name": "shark sir.fluffyfins", "hp": 1000, "spare": 0, "spae": 10, "taunt": ["sir.fluffyfins adjusts his monocle", f"sir.fluffyfins tells {party3['name']} to take a bath.", "sir.fluffyfins gives you cologne."]}
        taun = random.choice(ena['taunt'])
        if taun == "sir.fluffyfins gives you cologne.":
            items.append("cologne")
        pygame.mixer.music.load("fluffyfins.ogg")
        pygame.mixer.music.play(-1)
    
    print(f"{ena['name']} encountered you!")
    while in_battle:
        
        trun()
        
        if in_battle:
            atkqq = random.choice([player["name"], party2["name"], party3["name"]])
            atkq = random.randint(20, 50)
        
            if atkqq == player["name"]:
                player["hp"] = player["hp"] - atkq
            elif atkqq == party2["name"]:
                    party2["hp"] = party2["hp"] - atkq
            elif atkqq == party3["name"]:
                party3["hp"] = party3["hp"] - atkq
        
            print(f"\n{ena['name']} attacked {atkqq} for {atkq} dmg!")
            taun = random.choice(ena['taunt'])
            print(taun)
        else:
            pygame.mixer.music.fadeout(4500)
        
        if ena["hp"] == 0 or ena["hp"] <= 0:
            in_battle = False
            spared = False
            pass
        else:
            spared = True

def text(char, txt, delay=0.07, afterdelay=2, blip=None):
    global player
    char = char.lower().capitalize()
    if not isinstance(char, str) or not isinstance(txt, str) or not isinstance(delay, (float, int, complex)) or not isinstance(afterdelay, (float, int, complex)):
        raise TypeError("the chrater and the text must be a str, and the delay and afterdelay must be a number")
    elif delay > 1.5:
        raise ValueError("delay to big, must be less then 1.5")
    
    print(f"{char}: ", end="", flush=True)
    e = 0
    time.sleep(1)
    for _ in range(len(txt)):
        print(txt[e], end="", flush=True)
        if char == "Nilo":
            sound = pygame.mixer.Sound("niloblip.wav")
            pygame.mixer.Sound.play(sound)
        elif char == "Suzy":
            sound = pygame.mixer.Sound("suzyblip.wav")
            pygame.mixer.Sound.play(sound)
        elif char == player["name"].lower().capitalize():
            sound = pygame.mixer.Sound("plrblip.wav")
            pygame.mixer.Sound.play(sound)
        else:
            if blip == None:
                pass
            else:
                sound = pygame.mixer.Sound(blip)
                pygame.mixer.Sound.play(sound)
        e = e + 1
        time.sleep(delay)
    
    time.sleep(afterdelay)
    print("") #to reset end
        
        
text("nilo", "this is uh.... testing text")
text("suzy", "hey that kinda rhymes")
text(player["name"], "e")
time.sleep(3)
battle(1)
time.sleep(5)
if spared:
    text(ena["name"], "spared text 1.")
    text("suzy", f"spared text 1. why not 2? or 3? or 92? or {float('inf')}")
    text("nilo", "i dont think thats how numbers work...")
else:
    text(ena["name"], "fight text 1.")
    text(player["name"], "wait thare isnt a 2 right?")
    text("nilo", "no i dont think thares a 2.")
