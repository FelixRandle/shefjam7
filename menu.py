import arcade
import game
import constants

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()

class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

class StartTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Start", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()


class QuitTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Quit", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        quit()

class MenuView(arcade.View):
    def on_show(self):
        # self.background =  arcade.load_texture("images/")
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Trump Run", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 200,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Escaping climate change", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 150,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

        self.buttons = []
        self.quit_text_button = QuitTextButton(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 100,
                         QuitTextButton.on_release)
        self.buttons.append(self.quit_text_button)

        self.start_text_button = StartTextButton(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 50,
                         QuitTextButton.on_release)

        self.buttons.append(self.start_text_button)

        for i in self.buttons:
            i.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        print(_x, _y, _button, _modifiers)
        game_view = game.GameView()
        game_view.setup()
        instructions_view = InstructionView()

        runSomething = False
        check_mouse_press_for_buttons(_x,_y,self.buttons)

        for i in self.buttons:
            if i.pressed:
                print(i.__class__.__name__)
                if i.__class__.__name__ == "StartTextButton":
                    print("Running game")
                    self.window.show_view(game_view)
                    runSomething = True
                    break
                else:
                    print("Quitting!")
                    i.on_release()
                    runSomething = True
                    break

        if not runSomething:
            self.window.show_view(instructions_view)
            runSomething = False


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
        arcade.set_viewport(0, constants.SCREEN_WIDTH,
                            0, constants.SCREEN_HEIGHT)
        arcade.start_render()
        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to try again", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        game_view = game.GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = game.GameView()
        game_view.setup()
        self.window.show_view(game_view)
