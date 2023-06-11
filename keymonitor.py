from sshkeyboard import listen_keyboard, stop_listening

def keymonitor():
    km = listen_keyboard(
        on_press=press,
        on_release=release,
    )
    print("keymonitor done.")

def press(key):
    global pause, commandkey
    pause = True
    commandkey = key

def release(key):
    print(f"'{key}' released")

def stop_keymonitor():
    stop_listening()

def is_pause():
    global pause, commandkey
    return pause

def get_command():
    global pause, commandkey
    return commandkey

def reset_command():
    global pause, commandkey
    pause = False
    commandkey = ''

reset_command()

