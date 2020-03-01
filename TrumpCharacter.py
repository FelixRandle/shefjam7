import arcade
import character
import random
import os
import math
import constants


# Constants used to track if the player is facing left or right
import projectile

RIGHT_FACING = 1
LEFT_FACING = 0


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]


class PlayerCharacter(character.Character):
    def __init__(self, imagePath):

        # Set up parent class
        super().__init__(imagePath)

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Track out state
        self.jumping = False
        self.climbing = False
        self.is_on_ladder = False
        self.projectiles = arcade.SpriteList()
        self.scale = character.CHARACTER_SCALING
        self.aimPosition = [0, 0]

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-18, -30], [18, -30], [18, 25], [-18, 25]]

        # --- Load Textures ---

        main_path = "images/Trump/Pixelated/Running"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(6):
            texture = load_texture_pair(f"{main_path}_{i}.png")
            self.walk_textures.append(texture)

    def update(self, delta_time: float = 1/60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animationa
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > len(self.walk_textures) - 1:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]

    def shootProjectile(self):
        # Shooting Logic

        # Calculate speed for X and Y
        xDiff = self.aimPosition[0] - self.center_x
        yDiff = self.aimPosition[1] - self.center_y
        pointDiff = math.sqrt((xDiff ** 2) + (yDiff ** 2))

        multiplier = constants.PROJECTILE_SPEED / pointDiff
        self.projectiles.append(projectile.Projectile(self.center_x, self.center_y, xDiff * multiplier, yDiff * multiplier))



