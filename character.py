import arcade

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1


class Character(arcade.Sprite):
    def __init__(self, image_path):
        super().__init__(image_path, CHARACTER_SCALING)
        self.center_x = 64
        self.center_y = 96
