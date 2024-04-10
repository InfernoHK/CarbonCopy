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
print('\rYour story Begins'+ spaces, end = '' )
time.sleep(3)
os.system('clear')

print('\rIn a town where jobs are never filled and the bar is never empty, The town of Li-core, with no family friends or future' + spaces, end = '')
time.sleep(8)
os.system('clear')
print("\rhonestly you coudlve done better" + spaces, end = '')
time.sleep(3)
os.system('clear')
print('\rHateful comments aside, looking around town you notice a job center,' + spaces, end = '')
time.sleep(4)
os.system('clear')
print('\ryou notice while looking at the barely visible sign and faded paint that no one really uses or probably works at the so called "job center"' + spaces, end = '')
time.sleep(6)
os.system('clear')
print('\rafter a couple of seconds of realization that you have hit rock bottom you prepare yourself and enter')
time.sleep(4)
os.system('clear')
print('"Welcome s... oh its just a drunk hey the bar is that way"')
time.sleep(2)
print('she must think your a drunk, not suprised since this building is practically falling apart but still so rude')
print('what do you say to her ')
choice = menu(['Um hey im looking for a job', 'Im not a drunk im a responsible person', 'you think im a drunk?'])
if choice == 1:
  print("🍫")
elif choice == 2:
  print("⬜")
elif choice == 3:
  print("🍓")
