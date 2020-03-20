from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
from sharepoint import *
from questions import *
import residents
import smartfill

userKeyboard = Controller()

# describes form so that dictionary can be passed to type in data
enterFSRC = form_template(
    multiplechoice_field('week'),
    skip(),
    text_field('room'),
    text_field('username'),
    text_field('firstname'),
    text_field('lastname'),
    multiplechoice_field('success_first'),
    multiplechoice_field('success_second'),
    multiplechoice_field('challenge_first'),
    multiplechoice_field('challenge_second'),
    skip(),
    skip(),
    skip(),
    skip(),
    multiplechoice_field('resource'),
    text_field('advice'),
    text_field('notes')
)

def findResident():
    #check that user exists
    username = input('BGSU Username?\n>> ').split('@')[0]
    resident = residents.getResident(username)
    if not resident:
        residents.printAll()
        print('\nResident does not exist, see list above\n')
        return findResident()
    return resident

# records entry of a new interaction
def recordEntry(resident):
    if resident == None:
        return None
    # record basic questions
    successes = [askSuccess() for i in range(2)]
    challenges = [askChallenge() for i in range(2)]
    #ask only if interaction is flagged
    resource = askResource()
    # ask only if advice is flagged
    advice = askAdvice() if resource == 17 else ''
    notes = askNotes()

    # creates dictionary to be passed to enterFSRC() when entering data
    record = {
        "week"       : smartfill.getWeekNumber() - 1,
        "building"   : 1,
        "room"       : resident['room'],
        "username"   : residents.getUsername(resident),
        "firstname"  : resident['firstname'],
        "lastname"   : resident['lastname'],
        "success_first"    : successes[0],
        "success_second"   : successes[1],
        "challenge_first"  : challenges[0],
        "challenge_second" : challenges[1],
        "resource"   : resource,
        "advice"     : advice,
        "notes"      : notes
        }
    print(record)
    entries.append(record)

# Checks that a entry exists in memory when calls function to enter latest data
def writeEntry(index = -1):
    if(len(entries) < 1):
        print('ERROR: No entries exist')
        return
    enterFSRC(entries[index])

def on_release(key):
    # listener writes data if F2 is pressed
    if key == Key.f2:
        writeEntry()
    elif key == keyboard.Key.f3:
        # Stop listener
        return False

# start listener
listener = keyboard.Listener(
    on_release=on_release)
listener.start()

# keep program running
# later on will implement menu system here with more options such as recovering data
while True:
    choice = input('>> ')
    if len(choice) < 1:
        continue

    # Start new report
    if choice == 'new':
        recordEntry(findResident())
    # Print out all of the users
    if choice == 'users':
        residents.printAll()
    # Leave program
    elif choice == 'exit':
        break;
    # See if username of a resident was entered and 
    # start new report from that point if it was
    recordEntry(residents.getResident(choice))
