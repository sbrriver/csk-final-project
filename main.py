import random
import time


print("welcome to Astro Hype!!!")
print("here, you too will get to learn all about cool astronomy topics!")

a = input("first up: what topic do you wanna learn about (planets, supernovae, or double stars): ")


if a == "planets":
    ab= input("solar system or exoplanet? (s) or (e) ")
    if ab == "s":
        print("there are 8 planets in our solar system, can you name all of them?")
        abc = input("(put a commma between each entry (order matters) ")
        if abc == "mercury, venus, earth, mars, jupiter, saturn, uranus, neptune":
            print("hell yea mfs!!!")
            abcdef = input("do you want to learn more about the planets? (y) (n) ")
            if abcdef == "n":
                abcd= input("do you wanna learn about another thing? (y) (n): ")
                if abcd == "n":
                    print("ight see ya")
                if abcd == "y":
                    b = input("what topic do you wanna learn about (supernovae, double stars, random): ")
        else:
            def rps():
                print("oh no u have to win rock paper sissors to move on")
                ua = input("rock, paper, or sissors?: ")
                possible = ["rock", "paper", "sissors"]
                comp = random.choice(possible)
                
                if comp == ua:
                    print("its a tie, ill give it to u this time")
                    print("did you know that uranus orbits on its side?")
                elif (ua == "rock" and comp == "paper") or (ua == "paper" and comp == "sissors") or (ua == "sissors" and comp == "rock"):
                    print("wow, you lost to a computer?? damn.")
                elif (ua == "rock" and comp == "sissors") or ( ua == "paper" and comp == "rock" ) or (ua == "sissors" and comp == "paper"):
                    print("nice work!!")
                    print("did you know that the big red spot on jupiter is bigger in diameter than earth is? ")
            rps()
            print("now that u've survived rock paper sissors, lets learn about planets")
        time.sleep(3)
        print("mercury is the smallest planet with a very thin atmosphere and no moons")
        time.sleep(1)
        print("venus is earth's twin in size, the hottest planet in our solar system, rotates in the opposite direction of us, and has a very dense and thick atmosphere ")
        time.sleep(1)
        print("earth is next and thats us!!")
        time.sleep(1)
        print("mars is the 4th planet has gravity about 1/3 of earth's, has 2 moons, is red in color, and has no magnetic field")
        time.sleep(1)
        print("between mars and jupiter, is the asteroid belt and marks the seperation between the inner and outer planets")
        time.sleep(1)
        print("jupiter is a gas giant planet which means it is primarily hot gas. the big red spot thats on it is bigger in diameter than earth. it also features more than 75 moons and is the biggest planet")
        time.sleep(1)
        print("saturn is also a gas giant and has 82 moons. its mostly known for its rings which, contrary to pop culture, are not solid but rather complex rings of ice and rock ")
        time.sleep(1)
        print ("uranus is an ice giant which orbits on its side and has 27 moons, 13 rings, and is very very cold")
        time.sleep(1)
        print("last but certainly not least is neptune! an ice giant, it has 14 moons, 5 rings, and we have only gone by it once")
        b= input("well that was a lot, do you want to learn about another thing? (y) (n) ")
        if b == "y":
            bc = input ("supernovae or double stars? (s) or (d)")
            if bc == "s":
                print("supernovae are star explosions! when a star basically collapses and explodes! it can form black holes if the star is massive enough. if not, it can create white dwarf stars and planet forming regions. we use them to try and calculate expansion rate of the universe")
            else:
                print("double stars are the most common type of star in our universe, most being in pairs, we try and determine if they are gravitationally bound or not. if they are, we can find out all sorts of interesting information about the system. earth is actually irregular bc we have one sun.")
        else:
            print("ight bye")
    if ab == "e":
        print("exoplanets are any planet outside of our solar system and by understanding them we can understand our own planet better. most commmonly, we study hot jupiters which are the largest class of exoplanets and the brightest, making detection easier.")
if a == "supernovae":
    print("supernovae are star explosions! when a star basically collapses and explodes! it can form black holes if the star is massive enough. if not, it can create white dwarf stars and planet forming regions. we use them to try and calculate expansion rate of the universe")
    b= input("do you want to learn about another thing? (y) (n) ")
    if b == "y":
            bc = input ("planets or double stars? (p) or (d) ")
            if bc == "p":
                ab= input("solar system or exoplanet? (s) or (e) ")
                if ab == "s":
                    time.sleep(3)
                    print("mercury is the smallest planet with a very thin atmosphere and no moons")
                    time.sleep(1)
                    print("venus is earth's twin in size, the hottest planet in our solar system, rotates in the opposite direction of us, and has a very dense and thick atmosphere ")
                    time.sleep(1)
                    print("earth is next and thats us!!")
                    time.sleep(1)
                    print("mars is the 4th planet has gravity about 1/3 of earth's, has 2 moons, is red in color, and has no magnetic field")
                    time.sleep(1)
                    print("between mars and jupiter, is the asteroid belt and marks the seperation between the inner and outer planets")
                    time.sleep(1)
                    print("jupiter is a gas giant planet which means it is primarily hot gas. the big red spot thats on it is bigger in diameter than earth. it also features more than 75 moons and is the biggest planet")
                    time.sleep(1)
                    print("saturn is also a gas giant and has 82 moons. its mostly known for its rings which, contrary to pop culture, are not solid but rather complex rings of ice and rock ")
                    time.sleep(1)
                    print ("uranus is an ice giant which orbits on its side and has 27 moons, 13 rings, and is very very cold")
                    time.sleep(1)
                    print("last but certainly not least is neptune! an ice giant, it has 14 moons, 5 rings, and we have only gone by it once")
                else:
                    print("exoplanets are any planet outside of our solar system and by understanding them we can understand our own planet better. most commmonly, we study hot jupiters which are the largest class of exoplanets and the brightest, making detection easier.")
            else:
                print("double stars are the most common type of star in our universe, most being in pairs, we try and determine if they are gravitationally bound or not. if they are, we can find out all sorts of interesting information about the system. earth is actually irregular bc we have one sun.")
    else:
        print("ight bye")
if a == "double stars":
    print("double stars are the most common type of star in our universe, most being in pairs, we try and determine if they are gravitationally bound or not. if they are, we can find out all sorts of interesting information about the system. earth is actually irregular bc we have one sun.")
    b= input("do you want to learn about another thing? (y) (n) ")
    if b == "y":
        bc = input ("planets or supernovae? (p) or (s)")
        if bc == "p":
            ab= input("solar system or exoplanet? (s) or (e) ")
            if ab == "s":
                time.sleep(3)
                print("mercury is the smallest planet with a very thin atmosphere and no moons")
                time.sleep(1)
                print("venus is earth's twin in size, the hottest planet in our solar system, rotates in the opposite direction of us, and has a very dense and thick atmosphere ")
                time.sleep(1)
                print("earth is next and thats us!!")
                time.sleep(1)
                print("mars is the 4th planet has gravity about 1/3 of earth's, has 2 moons, is red in color, and has no magnetic field")
                time.sleep(1)
                print("between mars and jupiter, is the asteroid belt and marks the seperation between the inner and outer planets")
                time.sleep(1)
                print("jupiter is a gas giant planet which means it is primarily hot gas. the big red spot thats on it is bigger in diameter than earth. it also features more than 75 moons and is the biggest planet")
                time.sleep(1)
                print("saturn is also a gas giant and has 82 moons. its mostly known for its rings which, contrary to pop culture, are not solid but rather complex rings of ice and rock ")
                time.sleep(1)
                print ("uranus is an ice giant which orbits on its side and has 27 moons, 13 rings, and is very very cold")
                time.sleep(1)
                print("last but certainly not least is neptune! an ice giant, it has 14 moons, 5 rings, and we have only gone by it once")
            else:
                print("exoplanets are any planet outside of our solar system and by understanding them we can understand our own planet better. most commmonly, we study hot jupiters which are the largest class of exoplanets and the brightest, making detection easier.")
    else:
        print("supernovae are star explosions! when a star basically collapses and explodes! it can form black holes if the star is massive enough. if not, it can create white dwarf stars and planet forming regions. we use them to try and calculate expansion rate of the universe")
if a == "random":
    f = open("facts.txt", "r")
    x = random.randint(0,16)
    print(f.readlines(10)) #this doesnt work why tf
else:
    print("ight bye")
