# sharepoint.py 
# provides abstraction layer between data collection and entry

from pynput.keyboard import Key, Controller
import time

#Delay insures that the browser processes all keypresses
DELAY = 0.06
controller = Controller()
# was at .015

def form_template(*args):
    # Returns function that takes data based on args and types it
    # works by chaining text_fields and multiplechoice_fields then looping them over given data
    def type_form_entries(data):
#        set_head()
        for name, typer in args:
            typer(data[name]) if name != "" else typer()
        #reset_form()
    return type_form_entries

def text_field(name):
    # Returns name of field and typer function of text field
    def type_text_entry(text):
        if not isinstance(text, str):
            print("ERROR: {0} is not a string".format(text))
            raise ValueError()
        # keypresses to type text into field
        hit_str(text)
        hit(Key.tab)
    # name is used to pull data from given dictionary which is then entered by type_text_entry
    return (name, type_text_entry)

def multiplechoice_field(name, initial_state = 0):
    # Returns name of field and typer function of text field
    def select_choice(choice_index):
        #Resets state each time it is printed
        nonlocal initial_state
        state = initial_state

        # Makes sure that user is entering data for multiple choice and not a text entry
        if not isinstance(choice_index, int):
            print("ERROR: {0} is not an int".format(choice_index))
            raise ValueError()

        hit(Key.enter)
        # Moves up and down multiple choice window state can be changed if form defaults to a certain one
        while state < choice_index:
            hit(Key.down)
            state += 1
        while state > choice_index:
            hit(Key.up)
            state -= 1
        hit(Key.enter)
        hit(Key.tab)
    # name is used to pull data from given dictionary which is then entered by select_choice
    return (name, select_choice)

def skip(jump = 0):
    def hit_tab():
        for i in range(jump):
            hit(Key.down)
        hit(Key.tab)
    return ("", hit_tab)

def set_head():
    for i in range(3):
        hit(Key.tab)

def reset_form():
    time.sleep(DELAY * 100);

    # add delay HERE
    controller.press(Key.enter)
    controller.release(Key.enter)
    time.sleep(DELAY * 150)

    controller.press(Key.enter)
    controller.release(Key.enter)
    time.sleep(DELAY * 150)
    
    for i in range(2):
        controller.press(Key.tab)
        controller.release(Key.tab)
        time.sleep(DELAY * 10)

def hit(key):
    controller.press(key)
    controller.release(key)
    time.sleep(DELAY)

def hit_str(text):
    controller.type(text)
    time.sleep(DELAY)

