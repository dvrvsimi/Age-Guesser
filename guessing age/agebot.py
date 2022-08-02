import time

print('hello there, i was built to read the age of humans')
time.sleep(1)
print('would you be delighted in a little mind reading? :) ')
time.sleep(2)
enter = input('if your answer is yes, enter any english alphabet here: ')
allowed_entry = 'abcdefghijklmnopqrstuvwxyz'.casefold()
# might be unnecessary, i was trying the "not in" function below
while len(enter) != 1 or enter not in allowed_entry:
    enter = input('i am pretty sure you didn\'t enter a single english alphabet, let\'s try something else: ')
    break
enter1 = float(input('alright, kindly enter  your shoe size (EU system): '))
while enter1 not in range(20, 55):  # average european shoe size
    enter1 = float(input('i\'m afraid that\'s not a valid entry, try that again: '))
    break
enter2 = int((input('enter the year you were born: ')))
while len(str(enter2)) != 4:
    enter2 = int((input('enter a valid year: ')))
    break
# remember to change to str()
print('now focus on the screen and think about your age')
time.sleep(5)
print('...')
# how to make the ellipsis dots have their own interval?
time.sleep(3)
enter3 = int(50 + (enter1*5))
enter4 = int((20*enter3) + 1021)
enter5 = abs(int(enter2 - enter4))
# arithmetics using variables
print('you are ' + str(enter5) + ' years old, how did i do? :)')
# line above this one should return a terrible joke(enter5 is a 4-digit number)
enter6 = int(input('enter 1 for good and 0 for bad: '))
if enter6 == 1:
    print('i honestly did not expect to pull that off :(\nyou\'re welcome?')
elif enter6 == 0:
    print('sorry i disappointed you human ToT\n or maybe it\'s the last two digits?')
    enter7 = int(input('are the last two digits your age? enter 1 for yes and 0 for no '))
    if enter7 == 1:
        print('great! maybe i am clairvoyant after all!\nthanks for your time ')
    elif enter7 == 0:
        print('oops, i guess my programmer messed up something\nthanks for your time? :)')
