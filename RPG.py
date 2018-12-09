#Import and set basic values
import sys
import random
from time import sleep
ph = 200
mh = 0
mon = True
monp = True
de1 = True
de2 = True
bp = 0
bm = 0
J = 1
C = 1
T = 1
B = 0
cave = 0
village = 0
beach = 0
la1 = 0
esc = 0
gold = 50

m = 'blank'

n = "north"
s = "south"
e = "east"
w = "west"
yes = "yes"
no = "no"


def combat():
    global m
    global esc
    global ph

    def pwin(x, y):
        global mh
        global ph
        global bp
        global bm
        bdp = random.randint(1, 10)
        bdm = random.randint(1, 10)
        blp = random.randint(1, 100)
        blm = random.randint(1, 100)
        ed = random.randint(1, 5)
        pd = random.randint(11, 20)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Dan chooses to", x, "and deals", pd, "Damage!")
        if bm == 0:
            if blm <= 10:
                print("")
                print("FATAL HIT! Monster is now bleeding")
                bm = 1
        if pd == 20:
            print("")
            print("### CRTITCAL! ###")
        print("")
        print(m, "chooses to", y, "and deals", ed, "Damage!")
        if bp == 0:
            if blp <= 5:
                print("")
                print("FATAL HIT! You are now bleeding")
                bp = 1
        ph = int(ph) - int(ed)
        mh = int(mh) - int(pd)
        print("")
        if bp == 1:
            print("You take", bdp, "bleeding damage!")
            ph = int(ph) - int(bdp)
            print("")

        if bm == 1:
            print(m, "takes", bdm, "bleeding damage!")
            mh = int(mh) - int(bdm)
            print("")

        print("Dan has", ph, "health!")
        print("")
        print(m, "has", mh, "health!")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def plose(x, y):
        global mh
        global ph
        global bp
        global bm
        bdp = random.randint(1, 10)
        bdm = random.randint(1, 10)
        ed = random.randint(11, 20)
        pd = random.randint(1, 5)
        blp = random.randint(1, 100)
        blm = random.randint(1, 100)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Dan chooses to", x, "and deals", pd, "Damage!")
        if bm == 0:
            if blm <= 5:
                print("")
                print("FATAL HIT! Monster is now bleeding")
                bm = 1
        print("")
        print(m, "chooses to", y, "and deals", ed, "Damage!")
        if bp == 0:
            if blp <= 10:
                print("")
                print("FATAL HIT! You are now bleeding")
                bp = 1

        if ed == 20:
            print("")
            print("### CRTITCAL! ###")
        ph = int(ph) - int(ed)
        mh = int(mh) - int(pd)
        print("")
        if bp == 1:
            print("")
            print("You take", bdp, "bleeding damage!")
            ph = int(ph) - int(bdp)
        if bm == 1:
            print("")
            print(m, "takes", bdm, "bleeding damage!")
            mh = int(mh) - int(bdm)
        print("")
        print("Player has", ph, "health!")
        print("")
        print(m, "has", mh, "health!")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def pdraw(x, y):
        global mh
        global ph
        global bp
        global bm
        bdp = random.randint(1, 10)
        bdm = random.randint(1, 10)
        ed = random.randint(6, 10)
        pd = random.randint(6, 10)
        blp = random.randint(1, 100)
        blm = random.randint(1, 100)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Dan chooses to", x, "and deals", pd, "Damage!")
        if bm == 0:
            if blm <= 7:
                print("")
                print("FATAL HIT! Monster is now bleeding")
                bm = 1
        print("")
        print(m, "chooses to", y, "and deals", ed, "Damage!")
        if bp == 0:
            if blp <= 7:
                print("")
                print("FATAL HIT! You now bleeding!")
                bp = 1
        ph = int(ph) - int(ed)
        mh = int(mh) - int(pd)
        if bp == 1:
            print("")
            print("You take", bdp, "bleeding damage!")
            ph = int(ph) - int(bdp)
            print("")

        if bm == 1:
            print(m, "takes", bdm, "bleeding damage!")
            mh = int(mh) - int(bdm)
        print("")
        print("Player has", ph, "health!")
        print("")
        print(m, "has", mh, "health!")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    replyr = "rush"
    replyc = "counter"
    replys = "strike"
    replye = "run"
    replyh = "help"
    heal = "heal"

    print("""
  ###################
  
   COMBAT INITIATED
   
  ###################
  """)
    print(m, "challenged you to a fight, it has", mh, "health!")
    print("You have", ph, "health!")
    print("Rules: rush > strike > counter > rush")

    while mon:
        global J
        global C
        global T
        global B
        THI = int(J) + int(C) + int(T) + int(B)
        if int(mh) >= 1:
            print("You currently have:")
            print(J, "bottle(s) of Juice")
            print(T, "cup(s) of Tea")
            print(C, "cup(s) of Coffee")
            print(B, "Bandage(s)")
            print("")
            attack = input("""Choose your move! 
      - Strike
      - Rush
      - Counter
      - Heal
      - Run
      Your move:""")
            if attack.lower() == replyh:
                print("")
                print("Rules: rush > strike > counter > rush")
                print("")
            if attack.lower() == heal:
                if int(THI) > 0:
                    print(
                        "Select the number of the item which you would like to use"
                    )
                    print("(1) Juice  Heals:10 ", J, "Left")
                    print("(2) Tea    Heals:25 ", T, "Left")
                    print("(3) Coffee Heals:45 ", C, "Left")
                    print("(4) Bandage Stops bleeding ", B, "Left")
                    print("")
                    wh = input("Select one: ")
                    if int(wh) == 1:
                        if J > 0:
                            F = random.randint(1, 3)
                            if F == 1:
                                flav = 'Orange'
                            if F == 2:
                                flav = 'Apple'
                            if F == 3:
                                flav = 'Blackcurrant'
                            print("")
                            print("You take drink of juice")
                            sleep(2)
                            print("It's very refreshing!")
                            sleep(2)
                            print("mmm, its flavoured", flav)
                            sleep(2)
                            ph = int(ph) + 10
                            J = int(J) - 1
                            if ph > 200:
                                ph = 200
                            print("")
                            print("You now have", ph, "health and", J,
                                  "bottles(s) of juice remaining")
                        if J <= 0:
                            print("")
                            print("You dont have any of this item")
                            print("")
                    if int(wh) == 2:
                        if T > 0:
                            F = random.randint(1, 3)
                            if F == 1:
                                flav = 'Ginger'
                            if F == 2:
                                flav = 'Chocolate'
                            if F == 3:
                                flav = 'Passion fruit'
                            print("")
                            print("You take a sip of tea")
                            sleep(2)
                            print("Somehow its still warm.... and intact")
                            sleep(2)
                            print("mmm, its flavoured", flav)
                            sleep(2)
                            ph = int(ph) + 25
                            T = int(T) - 1
                            if ph > 200:
                                ph = 200
                            print("")
                            print("You now have", ph, "health and", T,
                                  "cups(s) of tea remaining")
                        if T <= 0:
                            print("You dont have any of this item")
                    if int(wh) == 3:
                        if C > 0:
                            print("You take a sip of coffee")
                            sleep(2)
                            print("Somehow its still warm.... and intact")
                            sleep(2)
                            ph = int(ph) + 45
                            C = int(C) - 1
                            if ph > 200:
                                ph = 200
                            print("")
                            print("You now have", ph, "health and", C,
                                  "cups(s) of coffee remaining")
                        if C <= 0:
                            print("You dont have any of this item")
                    if int(wh) == 4:
                        global bp
                        if B > 0:
                            if bp == 0:
                                print("You aren't bleeding")
                            if bp == 1:
                                print("You wrap the bandage around the wound")
                                print("")
                                bp = 0
                                B = int(B) - 1
                                print("You are no longer bleeding!")
                                print("")
                                print("You have", B, "Bandages left")
                            else:
                                print("")
                                print("Invalid answer")
                        else:
                            print("")
                            print("You have no bandages")
                else:
                    print("")
                    print("You don't have any healing items!")
                    print("")
            if attack.lower() == replyr:
                ma = random.randint(1, 3)
                if ma == 1:
                    pc = 'rush'
                    mc = 'rush'
                    pdraw(pc, mc)
                if ma == 2:
                    pc = 'rush'
                    mc = 'counter'
                    plose(pc, mc)
                if ma == 3:
                    pc = 'rush'
                    mc = 'strike'
                    pwin(pc, mc)
            if attack.lower() == replyc:
                ma = random.randint(1, 3)
                if ma == 1:
                    pc = 'counter'
                    mc = 'rush'
                    pwin(pc, mc)
                if ma == 2:
                    pc = 'counter'
                    mc = 'counter'
                    pdraw(pc, mc)
                if ma == 3:
                    pc = 'counter'
                    mc = 'strike'
                    plose(pc, mc)
            if attack.lower() == replys:
                ma = random.randint(1, 3)
                if ma == 1:
                    pc = 'strike'
                    mc = 'rush'
                    plose(pc, mc)
                if ma == 2:
                    pc = 'strike'
                    mc = 'counter'
                    pwin(pc, mc)
                if ma == 3:
                    pc = 'strike'
                    mc = 'strike'
                    pdraw(pc, mc)
            if attack.lower() == replyh:
                print("Rules: rush > strike > counter > rush")
            if attack.lower() == replye:
                esc = 1
                break

        if ph <= 0:
            print("You died, GAME OVER")
            sys.exit()

        if mh <= 0:
            print("Congratulations, you win!")
            break


def heal():
    global J
    global C
    global T
    global B
    global ph
    heal = True
    while heal:
        print("Select the number of the item which you would like to use")
        print("(1) Juice  Heals:10 ", J, "Left")
        print("(2) Tea    Heals:25 ", T, "Left")
        print("(3) Coffee Heals:45 ", C, "Left")
        print("(4) Bandage  Stops Bleeding ", B, "Left")
        print("")
        wh = input("Select one(Enter to quit): ")
        if wh == '1':
            if J > 0:
                F = random.randint(1, 3)
                if F == 1:
                    flav = 'Orange'
                if F == 2:
                    flav = 'Apple'
                if F == 3:
                    flav = 'Blackcurrant'
                print("")
                print("You take drink of juice")
                sleep(2)
                print("It's very refreshing!")
                sleep(2)
                print("mmm, its flavoured", flav)
                sleep(2)
                ph = int(ph) + 10
                J = int(J) - 1
                if ph > 200:
                    ph = 200
                print("")
                print("You now have", ph, "health and", J,
                      "bottles(s) of juice   remaining")
                hq2l = True
                while hq2l:
                    print("")
                    hq2 = input("Would you like to use anything else?")
                    if hq2.lower() == yes:
                        print("")
                        hq2l = False
                    if hq2.lower() == no:
                        hq2l = False
                        break
                    else:
                        print("")
                        print("Invalid answer")
            if J <= 0:
                print("You dont have any of this item")
        if wh == '2':
            if T > 0:
                F = random.randint(1, 3)
                if F == 1:
                    flav = 'Ginger'
                if F == 2:
                    flav = 'Chocolate'
                if F == 3:
                    flav = 'Passion fruit'
                print("")
                print("You take a sip of tea")
                sleep(2)
                print("Somehow its still warm.... and intact")
                sleep(2)
                print("mmm, its flavoured", flav)
                sleep(2)
                ph = int(ph) + 25
                T = int(T) - 1
                if ph > 200:
                    ph = 200
                print("")
                print("You now have", ph, "health and", T,
                      "cups(s) of tea   remaining")
                hq2l = True
                while hq2l:
                    print("")
                    hq2 = input("Would you like to use anything else?")
                    if hq2.lower() == yes:
                        print("")
                        hq2l = False
                    if hq2.lower() == no:
                        hq2l = False
                        break
                    else:
                        print("")
                        print("Invalid answer")
            if T <= 0:
                print("You dont have any of this item")
        if wh == '3':
            if C > 0:
                print("You take a sip of tea")
                sleep(2)
                print("Somehow its still warm.... and intact")
                sleep(2)
                ph = int(ph) + 45
                C = int(C) - 1
                if ph > 200:
                    ph = 200
                print("")
                print("You now have", ph, "health and", T,
                      "cups(s) of tea   remaining")
                hq2l = True
                while hq2l:
                    print("")
                    hq2 = input("Would you like to use anything else?")
                    if hq2.lower() == yes:
                        print("")
                        hq2l = False
                    if hq2.lower() == no:
                        hq2l = False
                        break
                    else:
                        print("")
                        print("Invalid answer")
            if C <= 0:
                print("You dont have any of this item")
        if wh == '4':
            global bp
            if B > 0:
                if bp == 0:
                    print("You aren't bleeding")
                if bp == 1:
                    print("You wrap the bandage around the wound")
                    print("")
                    bp = 0
                    B = int(B) - 1
                    print("You are no longer bleeding!")
                    print("")
                    print("You have", B, "Bandages left")
                else:
                    print("")
                    print("Invalid answer")
            else:
                print("")
                print("You have no bandages")
        if wh == '':
            break
        else:
            print("Invalid response")


def result():
    global esc
    global hp
    global ph
    global gold

    if esc == 1:
        print("")
        print("You manage to get away from the the monster")
        hpl = random.randint(1, 20)
        gl = random.randint(20, 40)
        print("")
        print("but you fell over and lost", hpl, "health and", gl, "gold")
        ph = int(ph) - int(hpl)
        gold = gold - gl
        if gold <= 0:
            gold = 0
        if ph <= 0:
            print("You died, GAME OVER")
            sys.exit()
        print("You now have", ph, "health and", gold, "gold")
        heal()
        esc = 0
    elif esc == 0:
        gg = random.randint(1, 40)
        gold = int(gold) + gg
        print("From that battle,you gained", gg, "gold, you now have", gold,
              "gold.")
        print("")
        zas = True
        while zas:
            wyl2h = input("Would you like to heal up?")
            if wyl2h.lower() == yes:
                heal()
            if wyl2h.lower() == no:
                break
            else:
                print("Invalid response")


def noesc():
    global esc
    if esc == 1:
        print("")
        print("Cant escape!")
        print("")
        esc = 0
        norun()


def shop():
    global gold
    x = True
    while x:
        print("You have", gold, "gold")
        print("")
        print(
            "What would you like to buy (Input the number that corresponds to the Item)?"
        )
        print("")
        print("-Juice   Cost:05  Heals:10       (1)")
        print("-Tea     Cost:10  Heals:25       (2)")
        print("-Coffee  Cost:20  Heals:45       (3)")
        print("-Bandage Cost:30  Stops bleeding (4)")
        print("")
        sq = input("Your answer here (0 to exit):")
        if sq.isnumeric():
            if int(sq) == 0:
                x = False
            if int(sq) == 1:
                global J
                sq2 = input("How many bottles would you like to buy")
                tc = int(sq2) * 5
                if int(tc) > int(gold):
                    print("Sorry, you cant afford that")
                else:
                    J = int(J) + int(sq2)
                    gold = int(gold) - int(tc)
                    print("you now have", J, "bottle(s) of Juice and", gold,
                          "gold left!")
                    xd = True
                    while xd:
                        sq3 = input("Would you like anything else?")
                        if sq3.lower() == yes:
                            print("")
                            xd = False
                        if sq3.lower() == no:
                            print("'Thank you for visiting, come back soon!'")
                            lol = False
                            break
                        else:
                            print("'I didnt understand that'")
            if int(sq) == 2:
                global T
                sq2 = input("How many cups of Tea would you like to buy")
                tc = int(sq2) * 10
                if int(tc) > int(gold):
                    print("Sorry, you cant afford that")
                else:
                    T = int(T) + int(sq2)
                    gold = int(gold) - int(tc)
                    print("you now have", T, "cup(s) of tea and", gold,
                          "gold left!")
                    xd = True
                    while xd:
                        sq3 = input("Would you like anything else?")
                        if sq3.lower() == yes:
                            print("")
                            xd = False
                        if sq3.lower() == no:
                            print("'Thank you for visiting, come back soon!'")
                            lol = False
                            break
                        else:
                            print("'I didnt understand that'")
            if int(sq) == 3:
                global C
                sq2 = input("How many cups of coffee would you like to buy")
                tc = int(sq2) * 20
                if int(tc) > int(gold):
                    print("Sorry, you cant afford that")
                else:
                    C = int(C) + int(sq2)
                    gold = int(gold) - int(tc)
                    print("you now have", C, "cups(s) of coffee and", gold,
                          "gold left!")
                    xd = True
                    while xd:
                        sq3 = input("Would you like anything else?")
                        if sq3.lower() == yes:
                            print("")
                            xd = False
                        if sq3.lower() == no:
                            print("'Thank you for visiting, come back soon!'")
                            lol = False
                            break
                        else:
                            print("'I didnt understand that'")
            if int(sq) == 4:
                global B
                sq2 = input("How many bandages would you like to buy")
                tc = int(sq2) * 30
                if int(tc) > int(gold):
                    print("Sorry, you cant afford that")
                else:
                    B = int(B) + int(sq2)
                    gold = int(gold) - int(tc)
                    print("you now have", B, "bandages and", gold,
                          "gold left!")
                    xd = True
                    while xd:
                        sq3 = input("Would you like anything else?")
                        if sq3.lower() == yes:
                            print("")
                            xd = False
                        if sq3.lower() == no:
                            print("'Thank you for visiting, come back soon!'")
                            lol = False
                            break
                        else:
                            print("'I didnt understand that'")
            else:
                print("Invalid number")
        else:
            print("That is not a number")


def norun():
    combat()
    noesc()


def reset():
    global bm
    bm = 0


def fightE():
    combat()
    result()
    reset()


def fightNE():
    combat()
    noesc()
    result()
    reset()


print(
    """ __          __  _                            _          _____              _____  _____   _____ 
 \ \        / / | |                          | |        |  __ \            |  __ \|  __ \ / ____|
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |  | | __ _ _ __ | |__) | |__) | |  __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |  | |/ _` | '_ \|  _  /|  ___/| | |_ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |__| | (_| | | | | | \ \| |    | |__| |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \_\____/  |_____/ \__,_|_| |_|_|  \_\_|     \_____|
                                                                                                 
                                                                                                """
)
sleep(1)
print("Created by: Haren")
sleep(2)
print("Inspired from: Discord Duels by Darkspine77")
print("")
sleep(3)

print(
    "You wake up from your bed, to suddenly realise everything looks cartoony..."
)
sleep(2)
print("Your Mom comes into the room, it looks like she needs something")
sleep(2)
print("'Dear, can you help your mother out and kill a boar for dinner'")
sleep(2)
print("You put your equipment on and set out into the field")
sleep(2)
print("After not too long, you encounter a boar, it rushes towards you")
m = 'Wild boar'
mh = random.randint(30, 50)
fightNE()
print("You go back home and give the boar your mother asked you")
sleep(2)
print("The door seems to be open")
sleep(3)
print("It seems that you can't find your mother...")
print(1)
print("strange...")
print(
    "You look around the house to find your mother, but as you look around the house, you begin to find signs of a fight, and some blood"
)
sleep(3)
print("you begin to fear the worst, when you find a note")
sleep(2)
print("'If you want your mother back, come to Rarotonga'")
sleep(2)
print("Without any hesitation you grab 50 gold, and your house key")
print("")
gold = int(gold) + 50
print("you now have", gold, "gold")
sleep(2)
print(
    "You run out the house (Locking the door behind you), you run out into a feild, you should gather supplies before you look for your mother"
)
sleep(3)
print("You look around to see a few structures...")
sleep(2)
print("To your north, you see a cave")
sleep(2)
print("To your east, you see a beach")
sleep(2)
print("To your west, you see a small town")
sleep(2)
while de1:
    d1 = input("Where would you like to go? (North, South, East or West)")
    if d1.lower() == n:
        if cave == 0:
            print(
                "You cautiously enter the cave, you see a pile of bones and a chest inside. You instinctively go for the chest, desiring the loot inside!"
            )
            gold = gold + 30
            sleep(3)
            print("You open the chest to find 30 gold, you now have", gold,
                  "gold")
            sleep(3)
            print(
                "You hear some footsteps behind you, and you turn around to see a Goblin"
            )
            m = 'Goblin'
            mh = random.randint(30, 50)
            sleep(2)
            combat()
            cave = 1
            result()
            print("You return the the field.")
        elif cave == 1:
            print("You have already been here, you return the the feild.")
    if d1.lower() == w:
        if village == 0:
            lol = True
            print(
                "As you apporach the small village, you see a shop offering healing items"
            )
            print("")
            sleep(2)
            print(
                "The Shop Owner waves to you, as you approach him, he starts talking to you"
            )
            print("")
            sleep(2)
            print("'Hi there! my name is Daylon, what's yours?")
            print("")
            sleep(2)
            print("'Dan, nice to meet you', you reply")
            print("")
            sleep(2)
            print("'Nice to meet you too Dan!")
            print("")
            sleep(2)
            while lol:
                vq1 = input("'Are you interesting in what im selling?'")
                if vq1.lower() == yes:
                    shop()
                    village = 1
                    print("'Farewell Dan, hope to see you soon'")
                    sleep(1)
                    print(
                        "After exploring the rest of the village, you return to the field"
                    )
                    lol = False
                elif vq1.lower() == no:
                    print("'No problem, good luck on your travels'")
                    sleep(1)
                    village = 1
                    print(
                        "After exploring the rest of the village, you return to the   field"
                    )
                    lol = False
                else:
                    print("I dont understand that!")
        elif village == 1:
            lol = True
            while lol:
                vq1 = input(
                    "'Welcome back Dan, are you interested in my wares?'")
                if vq1.lower() == yes:
                    shop()
                    village = 1
                    print("'Goodbye Dan, hope to see you soon'")
                    sleep(1)
                    print("You return to the field")
                    break
                    if vq1.lower() == no:
                        print("'No problem, good luck on your travels'")
                        sleep(1)
                        print("You return to the field")
    if d1.lower() == s:
        print("Theres nothing interesting here...")
    if d1.lower() == e:
        ship = True
        if beach == 0:
            print("As you approach the beach, you see a sign...")
            sleep(2)
            print("""
    ###########################
    |                         |
    |  Boat Trip to Rarotonga |
    |          5 GOLD         |
    |                         |
    ###########################
    """)
            sleep(2)
            print("The Sailor looks at you, he then smirks")
            sleep(2)
            print(
                "'Welcome Traveller, i am feeling generous today, you can ride for free!"
            )
            sleep(2)
            while ship:
                l = input(
                    "'Would you like to take the trip now?(You wont be able to come back.)'"
                )
                if l.lower() == yes:
                    print("'Hop on the ship and we will get sailing soon!'")
                    sleep(2)
                    de1 = False
                    ship = False
                    break
                if l.lower() == no:
                    print("'Do not worry, you can come back later'")
                    sleep(1)
                    print("You return to the field")
                    ship = False
                    beach = 1
                else:
                    print("'What? Answer yes or no.")
        elif beach == 1:
            while ship:
                l = input(
                    "'Welcome back! Would you like to take the trip now?(You wont be able to come back.)'"
                )
                if l.lower() == yes:
                    print("'Hop on the ship and we will get sailing soon!'")
                    sleep(2)
                    de1 = False
                    ship = False
                    break
                if l.lower() == no:
                    print("'Do not worry, you can come back later'")
                    sleep(1)
                    print("You return to the field")
                    ship = False
                else:
                    print("'What? Answer yes or no.")
print("You set sail on the ship, with the Sailor")
sleep(2)
print(
    "You start to feel nervous, you are the only one who seems to be onboard, apart from the merchant of course."
)
sleep(2)
print("you hear some cluttering behind you")
sleep(1)
print("The merchant has his sword drawn towards you!")
sleep(1)
print("You will die here Dan, and noone will find your corpse!")
sleep(1)
print("You also draw your sword")
m = "Sailor"
mh = 100
fightNE()
print(
    "You defeat the sailor, it seems whoever kidnapped your mom, knows who you are and hates you"
)
sleep(3)
print(
    "You search around the ship and find some sort of target, with your name, your picture and alot of money"
)
sleep(1)
print(
    "'Well, I guess the sailor doesnt need this anymore', you take the bag of 200 gold"
)
sleep(2)
gold = int(gold) + 200
print("")
print("you now have", gold, "gold")
print("")
sleep(2)
print(
    "You suddenly realise you have no idea how to steer a ship, but the location is just ahead, so you hope and pray that its 'smooth sailing' from there."
)
sleep(2)
print("You eventually crash onto a beach, you get off the boat")
sleep(2)
print("On the beach you read a sign, which seems very out of place")
print(
    "Congratulations you have reached the end of this version, i'll update this whenever I get the time to, but I hope you had fun with this game!"
)
