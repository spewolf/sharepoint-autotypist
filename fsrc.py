from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
from sharepoint import *
from questions import *
import residents
import smartfill

entries = []
userKeyboard = Controller()

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

def recordEntry():
    found = False
    while not found:
        username = input('BGSU Username?\n>> ').split('@')[0]
        resident = residents.getResident(username)
        if not resident:
            print('Resident does not exist, check residents.csv')
        else:
            found = True

    successes = [askSuccess() for i in range(2)]
    challenges = [askChallenge() for i in range(2)]
    flagQ = askFlag()
    challengeQ = askChallengeQuestion() if flagQ == 0 else 0
    resource = askResource()
    advice = askAdvice() if resource == 17 else ''
    notes = askNotes()

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
        
def writeEntry(index = -1):
    if(len(entries) < 1):
        print('ERROR: No entries exist')
        return
    enterFSRC(entries[index])
    print("Entry Written")

def on_press(key):
    return
#     try:
#         print('{0} pressed'.format(key))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == Key.f2:
        writeEntry()
    elif key == keyboard.Key.esc:
        # Stop listener
        return False

#recordEntry()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    choice = input('')
    if choice == 'new':
        recordEntry()
    elif choice == 'exit':
        break;