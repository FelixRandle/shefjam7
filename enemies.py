import character
import constants

class Enemy(Character):
    def __init__(self, image_path, x,y):
        super().__init__(image_path, CHARACTER_SCALING)
        self.movement = False
        self.center_x = x
        self.center_y = y
