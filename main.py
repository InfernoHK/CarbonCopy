import math
import random

direction = ("")
request = ("")
requestawn = ("")

play = input("Disclaimer you will be embarking on a journey which will contain acts of violence, amusment, bargaining (the worst sin of all) and overall other  roleplay game elements mashed together with a story adventure game, will you proceed? (y/n) ")

def MainGame(play):
    if play == "y":
        print("Great you will (not) regret this")
    elif play == "n":
        print("Well too bad you will paly anyway")
    print(end="\r") 

    print("Anway adventurer you will be embarking on this journey, Your story begins in a town called Li-core, not because its fancy or nothing but because the people here are always.... d-runk... yeah d-runk its a slang for not in the right state of mind, anyway your story begins here you have decided to start your own life away from home for reasons, im sure you dont want me to pry into your life and tell you so we'll leave it there, There are a couple of job posters you've seen going into this town, some of them are unintresting and harsh like Mud rucker,Gun oiler, Magician, and Waste managment, some though seem to be full of excitement like Sherrif, Professional Gambler or a Sorcerer(yes there is magic not some pretend or nothing like that)")
    print("as you make it into town you see a job center, you open the door and walk in to see it be as empty as your wallet, did i mention that you are flat broke, anyway you go to the front desk and see your options and select your occupation (Mud rucker,Gun oiler, Magician, and Waste managment, Sherrif, Professional Gambler, Sorcerer")

MainGame(play)
