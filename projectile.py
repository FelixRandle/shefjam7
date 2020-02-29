import arcade
import constants

class Projectile(arcade.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__("images/items/tweet.png", constants.ITEM_SCALING)
        self.center_x = x
        self.center_y = y

        self.change_x = dx
        self.change_y = dy

