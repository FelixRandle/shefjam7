import arcade

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
PLAYER_MOVEMENT_SPEED = 5


class Character(arcade.Sprite):
    def __init__(self, image_path):
        super().__init__(image_path, CHARACTER_SCALING)
        self.center_x = 64
        self.center_y = 96

        self.movingLeft = False
        self.movingRight = False

    def setSpeed(self):
        self.change_x = 0
        if self.movingLeft:
            self.change_x -= PLAYER_MOVEMENT_SPEED
        if self.movingRight:
            self.change_x += PLAYER_MOVEMENT_SPEED
