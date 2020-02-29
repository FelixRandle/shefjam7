import arcade
import game
import constants


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Welcome to Trump Run, you're objective is to progress through the levels whilst trying", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 25,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text(" to collect enough tweets so that people are distracted from climate change.", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 50,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text(" There are 3 different levels, a city level a polar level and an outback level. As you will see,", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text(" the levels will get harder as you progress as the effects of climate change create more and more ", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("problems. You will have 100 health which can be replenished by the fake tan sprays dotted about.", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 125,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text(" You will lose your health to angered animals, scientists and protesters as well as natural hazards", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text(" like bush fires and freezing water. Click to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 175,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = game.GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to try again", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = game.GameView()
        game_view.setup()
        self.window.show_view(game_view)