"""
Platformer Game
"""
import arcade

import menu
import constants

def main():
    """ Main method """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    menu_view = menu.MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
