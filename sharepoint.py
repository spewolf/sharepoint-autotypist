from pynput.keyboard import Key, Controller
import time

#Delay insures that the browser processes all keypresses
DELAY = 0.01

def form_template(*args):
    # Returns function that takes data based on args and types it
    def type_form_entries(data):
        for name, typer in args:
            typer(data[name])
    return type_form_entries

def text_field(name):
    # Returns name of field and typer function of text field
    def type_text_entry(text):
        if not isinstance(text, str):
            print("ERROR: {0} is not a string".format(text))
            raise ValueError()
        controller = Controller()
        time.sleep(DELAY)
        controller.type(text)
        time.sleep(DELAY)
        controller.press(Key.tab)
        controller.release(Key.tab)
    return (name, type_text_entry)

def multiplechoice_field(name, initial_state = 0):
    # Returns name of field and typer function of text field
    def select_choice(choice_index):
        #Resets state each time it is printed
        nonlocal initial_state
        state = initial_state

        if not isinstance(choice_index, int):
            print("ERROR: {0} is not an int".format(choice_index))
            raise ValueError()
        controller = Controller()
        # Moves up and down multiple choice window state can be changed if form defaults to a certain one
        while state < choice_index:
            time.sleep(DELAY)
            controller.press(Key.down)
            controller.release(Key.down)
            state += 1
        while state > choice_index:
            time.sleep(DELAY)
            controller.press(Key.up)
            controller.release(Key.up)
            state -= 1
        time.sleep(DELAY)
        controller.press(Key.tab)
        controller.release(Key.tab)
    return (name, select_choice)