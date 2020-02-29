import arcade

import map
import character
import TrumpCharacter
import menu
import constants
import animatedItem as item

# Movement speed of player, in pixels per frame
GRAVITY = 1.1
PLAYER_JUMP_SPEED = 20

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 300
RIGHT_VIEWPORT_MARGIN = 300
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 150


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.damage_list = None
        self.wall_list = None
        self.tweet_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player = None

        # Our physics engine
        self.physics_engine = None
        self.map = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        #Keep track of health
        self.health = 100

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        self.maps = [
            {
                "map": map.Map("./maps/level_one.tmx"),
                "scoreTarget": 10
            },
            {
                "map": map.Map("./maps/level_two.tmx"),
                "scoreTarget": 6
            },
            {
                "map": map.Map("./maps/level_three.tmx"),
                "scoreTarget": 3
            }
        ]

        self.currentLevel = 0
        self.frame_number = 0

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        #Keep track of health
        #TODO Do we want to have different health on different levels.
        #TODO switch health to be stored in character.
        self.health = 30

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.damage_list = arcade.SpriteList()
        self.tweet_list = arcade.SpriteList()
        self.tan_list = arcade.SpriteList()

        # Set up the player
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player = TrumpCharacter.PlayerCharacter(image_source)
        self.player_list.append(self.player)

        # --- Load in a map from the tiled editor ---
        self.map = self.maps[self.currentLevel]["map"]

        self.wall_list = self.map.wall_list
        self.damage_list = self.map.damage_list
        self.tweet_list = self.map.tweet_list

        for thing in self.map.tan_list:
            self.tan_list.append(item.AnimatedItem("images/items/Tan/tan", 14, thing.center_x, thing.center_y))

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.wall_list,
                                                             GRAVITY)

        self.base_viewport = arcade.get_viewport()

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.tweet_list.draw()
        self.damage_list.draw()
        self.player_list.draw()
        self.tan_list.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

        # Draw our health on the screen, scrolling it with the viewport
        health_text = f"Health: {self.health}"
        arcade.draw_text(health_text, 10 + self.view_left, 30 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.movingLeft = True
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.movingRight = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.movingLeft = False
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.movingRight = False

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.frame_number += 1
        self.player.setSpeed()

        self.player.update_animation()
        # Slow down animation by 3x
        if self.frame_number % 3 == 0:
            for tan in self.tan_list:
                tan.update_animation(delta_time*3)
        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any damage
        damage_hit_list = arcade.check_for_collision_with_list(self.player,
                                                               self.damage_list)

        # Loop through each coin we hit (if any) and remove it
        for item in damage_hit_list:
            # Remove the coin
            item.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.health -= 10

        # See if we hit any damage
        tan_hit_list = arcade.check_for_collision_with_list(self.player,
                                                            self.tan_list)

        # Loop through each coin we hit (if any) and remove it
        for item in tan_hit_list:
            # Remove the coin
            tan.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.player.health += 10

        # See if we hit any damage
        tweet_hit_list = arcade.check_for_collision_with_list(self.player,
                                                              self.tweet_list)

        # Loop through each coin we hit (if any) and remove it
        for item in tweet_hit_list:
            # Remove the coin
            item.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.score += 1

        if self.player.center_y < 0:
            self.health = 0

        # Checking for low health.
        if self.health <= 0:
            game_over_view = menu.GameOverView()
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)

        # Checking for winning score, assuming constant for now.
        if self.score == self.maps[self.currentLevel]["scoreTarget"]:
            if self.currentLevel == len(self.maps) - 1:
                print("WINNER WINNER CHICKEN DINNER")
            else:
                self.currentLevel += 1
                self.setup()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)

