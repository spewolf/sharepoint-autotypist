from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
from sharepoint import *
from questions import *
import residents
import smartfill

entries = []
userKeyboard = Controller()

# describes form so that dictionary can be passed to type in data
enterFSRC = form_template(
    text_field('title'),
    multiplechoice_field('week'),
    multiplechoice_field('building'),
    text_field('room'),
    text_field('username'),
    text_field('firstname'),
    text_field('lastname'),
    multiplechoice_field('success_first'),
    multiplechoice_field('success_second'),
    multiplechoice_field('challenge_first'),
    multiplechoice_field('challenge_second'),
    multiplechoice_field('interaction_type'),
    text_field('number_participants'),
    text_field('group_participants'),
    multiplechoice_field('flagQ', 1),
    multiplechoice_field('challengeQ'),
    multiplechoice_field('resource'),
    text_field('advice'),
    text_field('notes')
)

# records entry of a new interaction
def recordEntry():
    #check that user exists
    found = False
    while not found:
        username = input('BGSU Username?\n>> ').split('@')[0]
        resident = residents.getResident(username)
        if not resident:
            print('Resident does not exist, check residents.csv')
        else:
            found = True

    # record basic questions
    successes = [askSuccess() for i in range(2)]
    challenges = [askChallenge() for i in range(2)]
    flagQ = askFlag()
    #ask only if interaction is flagged
    challengeQ = askChallengeQuestion() if flagQ == 0 else 0
    resource = askResource()
    # ask only if advice is flagged
    advice = askAdvice() if resource == 17 else ''
    notes = askNotes()

    # creates dictionary to be passed to enterFSRC() when entering data
    record = {
        "title"      : "Spencer Wolf - Intentional Interaction",
        "week"       : smartfill.getWeekNumber(),
        "building"   : 0,
        "room"       : resident['room'],
        "username"   : username,
        "firstname"  : resident['firstname'],
        "lastname"   : resident['lastname'],
        "success_first"    : successes[0],
        "success_second"   : successes[1],
        "challenge_first"  : challenges[0],
        "challenge_second" : challenges[1],
        "interaction_type" : 0,
        "number_participants": '1',
        "group_participants": '',
        "flagQ"      : flagQ,
        "challengeQ" : challengeQ,
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
    print("Entry Written")

def on_release(key):
    # listener writes data if F2 is pressed
    if key == Key.f2:
        writeEntry()
    elif key == keyboard.Key.esc:
        # Stop listener
        return False

# start listener
listener = keyboard.Listener(
    on_release=on_release)
listener.start()

# keep program running
# later on will implement menu system here with more options such as recovering data
while True:
    choice = input('')
    if choice == 'new':
        recordEntry()
    elif choice == 'exit':
        break;