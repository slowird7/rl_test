# sample3.py

from pynput import mouse, keyboard
import time

def move(x, y):
    print('マウスポインターは {0} へ移動しました'.format((x, y)))

def click(x, y, button, pressed):
    print('{2} が {0} された座標： {1}'.format(
        'Pressed' if pressed else 'Released',(x, y), button))

def scroll(x, y, dx, dy):
    print('{0} スクロールされた座標： {1}'.format(
        'down' if dy < 0 else 'up',(x, y)))

def press(key):
    try:
        print('アルファベット {0} が押されました'.format(key.char))
    except AttributeError:
        print('スペシャルキー {0} が押されました'.format(key))

def release(key):
    print('{0} が離されました'.format(key))
    if key == keyboard.Key.esc:     # escが押された場合
        mouse_listener.stop()       # mouseのListenerを止める
        keyboard_listener.stop()    # keyboardのlistenerを止める

# mouseのリスナー
mouse_listener = mouse.Listener(
    on_move=move,
    on_click=click,
    on_scroll=scroll)
mouse_listener.start()

# keyboardのリスナー
keyboard_listener = keyboard.Listener(
    on_press=press,
    on_release=release)
keyboard_listener.start()

while True:
    print("ok")
    time.sleep(1)
