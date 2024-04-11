import math
import random
import time
import os
from sys import stdout
from getkey import getkey, keys
from ansi.color import fg
from ansi import cursor

def menu(choices):
  global pos
  pointer = fg.boldblue('>')
  for choice in enumerate(choices):
    text = f'  {choice[0]+1}. {choice[1]}'
    if choice[0] == 0:
      text = fg.bold(text)
    print(text)
  print(cursor.hide()+cursor.up()*(len(choices))+pointer, end=" ")
  stdout.flush()

  pos = 1
  while 1:
    key = getkey()
    text = f'  {pos}. {choices[pos-1]}'
    if (key == '\x1b[A' or key == 'w') and pos > 1:
      pos -= 1
      print(f'\r{text}\r' + cursor.up() + pointer + \
            fg.bold(f' {pos}. {choices[pos-1]}'), end = " ")
    elif (key == '\x1b[B' or key == 's') and pos < len(choices):
      pos += 1
      print(f'\r{text}\r' + cursor.down() + pointer + \
            fg.bold(f' {pos}. {choices[pos-1]}'),end = " ")
    elif key == '\n':
      print(cursor.down()*(len(choices)-pos)+cursor.show())
      return pos
    elif key.isdecimal():
      number = int(key)
      if 0 < number <= len(choices):
        print(cursor.down()*(len(choices)-pos)+cursor.show())
        return number
    stdout.flush()
    





spaces = '  ' * 50
name = input("Enter a First Name ")
name_last = input("Enter a Last Name ")

print("Controls: Up and down / W and S, Enter(for continuing Dialouge)")
pause = input("")
print('"Warning this "Game" may cause addiction, the funnies, mild humor and reading (The Scariest)"')
pause = input("")
print("\rokay",name ,"Your story Begins")
pause = input("")
print('In a town where jobs are never filled and the bar is never empty, You arrive in the town of Li-core, with no family friends or future')
pause = input("")
print("\rhonestly you coudlve done better" + spaces, end = '')
pause = input("")
os.system('clear')
print('Hateful comments aside, looking around town you notice a job center,')
pause = input("")
print('you notice while looking at the barely visible sign and faded paint that no one really uses or probably works at the so called "job center"')
pause = input("")
print('after a couple of seconds of realization that you have hit rock bottom you prepare yourself and enter')
pause = input("")
os.system('clear')
print('"Welcome s... oh its just a drunk, hey the bar is that way, wait i aint never seen your face before, what do you need"')
pause = input("")
print("wow she must've thought your were a drunk, not suprised since this building is practically falling apart but still so rude")
choice = menu(['Um hey im looking for a job?', "Hi my name is "+ name +" "+ name_last +" and im looking for a job" , 'you think im a drunk?'])
if choice == 1:
  print('"is that a question or an Awnser"')
  choice = menu(['A Question?', 'An Awnser'])
  if choice == 1:
    print('"Your killing me"')
    pause = input("")
    print('"Just go over to that board and pick a job"')
    pause = input("")
    print("you go over to the board to see 5 pieces of paper, if you can call it that")
    choice = menu(['Sherf Assistant : wait sherf, did... did they mispell sheriff or is there a thing called a "Sherf" ', "Professional Gambler : Exactly what it sounds like, this town apparently is drowing in debt from bets made when drunk", 'Waste Managment : well its kinda in the name "Waste Management" you clean trash at least i think... ', 'Magician : This is a job offered??? Why... I mean if you really want to who am i to say what you can or cant be', '.... Hunter : the front half of this form has been ripped so one could only assume it means Bounty Hunter'])
    if choice == 1:
      os.system('clear')
      print("You bring the form back")
      
    elif choice == 2:
      os.system('clear')
      print("You bring the form back")
    elif choice == 3:
      os.system('clear')
      print("You bring the form back")
    elif choice == 4:
      os.system('clear')
      print("You bring the form back")
    elif choice == 5:
      os.system("clear")
      print("You bring the form back")
    
  elif choice == 2:
      print("she just tells you to bring over a form once you have decided")
      pause = input("")
      choice = menu(['Sherf Assistant : wait sherf, did... did they mispell sheriff or is there a thing called a "Sherf" ', "Professional Gambler : Exactly what it sounds like, this town apparently is drowing in debt from bets made when drunk", 'Waste Managment : well its kinda in the name "Waste Management" you clean trash at least i think... ', 'Magician : This is a job offered??? Why... I mean if you really want to who am i to say what you can or cant be', '.... Hunter : the front half of this form has been ripped so one could only assume it means Bounty Hunter'])
 
elif choice == 2: 
  print('"oh you dont need to be that formal with me, names Mandy"')
  pause = input("")
  print('"Go over to the wall to see all the current jobs and bring the form back when you have decided"')
  pause = input("")
  print("you go over to the board to see 5 pieces of paper, if you can call it that")
  choice = menu(['Sherf Assistant : wait sherf, did... did they mispell sheriff or is there a thing called a "Sherf" ', "Professional Gambler : Exactly what it sounds like, this town apparently is drowing in debt from bets made when drunk", 'Waste Managment : well its kinda in the name "Waste Management" you clean trash at least i think... ', 'Magician : This is a job offered??? Why... I mean if you really want to who am i to say what you can or cant be', '.... Hunter : the front half of this form has been ripped so one could only assume it means Bounty Hunter'])
  
elif choice == 3:
  print('"Well What are yuh"')
  pause = input("")
  print("Good question, What are you")
  choice = menu(['Im just traveling','Im not really anything', 'Im jobless', '*Stay Silent*'])

