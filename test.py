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
    
print('What is your favorite ice-cream flavor?')
choice = menu(['Chocolate', 'Vanilla', 'Strawberry'])
if choice == 1:
  print("🍫")
elif choice == 2:
  print("⬜")
elif choice == 3:
  print("🍓")