import arcade
import character


class AnimatedItem(arcade.Sprite):
    def __init__(self, mainPath, frameCount, x, y):
        # Set up parent class
        super().__init__(f"{mainPath}_0.png", center_x=x, center_y=y)

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Load textures for walking
        self.textures = []
        for i in range(frameCount):
            texture = arcade.load_texture(f"{mainPath}_{i}.png")
            self.textures.append(texture)

    def update_animation(self, delta_time: float = 5/60):
        self.texture = self.textures[self.cur_texture]

        self.cur_texture += 1
        if self.cur_texture > len(self.textures) - 1:
            self.cur_texture = 0
