from pynput.keyboard import Controller, KeyCode


class InputCommands():
    
    def __init__(self):
        self.keyboard = Controller()
    
    def press_release(self,virtual_key_id):
        
        key = KeyCode.from_vk(virtual_key_id)
        self.keyboard.press(key)
        self.keyboard.release(key)

    
    