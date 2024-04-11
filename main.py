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
  print(cursor.hide()+cursor.up()*(len(choices))+pointer, end='')
  stdout.flush()

  pos = 1
  while 1:
    key = getkey()
    text = f'  {pos}. {choices[pos-1]}'
    if (key == '\x1b[A' or key == 'w') and pos > 1:
      pos -= 1
      print(f'\r{text}\r' + cursor.up() + pointer + \
            fg.bold(f' {pos}. {choices[pos-1]}'), end = '')
    elif (key == '\x1b[B' or key == 's') and pos < len(choices):
      pos += 1
      print(f'\r{text}\r' + cursor.down() + pointer + \
            fg.bold(f' {pos}. {choices[pos-1]}'), end = '')
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
name = input("Enter a First Name")
time.sleep(1)
name_last = input("Enter a Last Name")
time.sleep(1)


print("\rokay",name ,"Your story Begins")
time.sleep(3)

print('In a town where jobs are never filled and the bar is never empty, The town of Li-core, with no family friends or future')
time.sleep(8)
print("\rhonestly you coudlve done better" + spaces, end = '')
time.sleep(3)
os.system('clear')
print('Hateful comments aside, looking around town you notice a job center,')
time.sleep(4)
print('you notice while looking at the barely visible sign and faded paint that no one really uses or probably works at the so called "job center"')
time.sleep(6)
print('after a couple of seconds of realization that you have hit rock bottom you prepare yourself and enter')
time.sleep(5)
os.system('clear')
print('"Welcome s... oh its just a drunk, hey the bar is that way"')
time.sleep(3)
print('she must think your a drunk, not suprised since this building is practically falling apart but still so rude')
print('what do you say to her ')
choice = menu(['Um hey im looking for a job', "Hi my name is "+ name + name_last +" and im looking for a job" , 'you think im a drunk?'])
if choice == 1:
  print("well you've come to the last place")
  time.sleep(2)
  print('"We have got only a couple available and let me tell you there not that good."')
  print("She points to the wall containing the 5 jobs no one has taken yet")
  print("she tells you (in a unemphatic way) to bring over a form once you have decided")
  choice = menu(['Sherf Assistant : wait sherf, did... did they mispell sheriff or is there a thing called a "Sherf" ', "Professional Gambler : Exactly what it sounds like, this town apparently is drowing in debt from bets made when drunk", 'Waste Managment : well its kinda in the name "Waste Management" you clean trash at least i think... ', 'Magician : This is a job offered??? Why... I mean if you really want to who am i to say what you can or cant be', 'Bounty ... : Half of this form has been ripped so one could only assume it means Bounty Hunter'])
elif choice == 2:
  print("⬜")
elif choice == 3:
  print("🍓")
