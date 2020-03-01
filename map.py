import arcade

TILE_SCALING = 0.5
COIN_SCALING = 0.5

class Map:
    def __init__(self, map_name):
        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(my_map, 'Platforms', TILE_SCALING)

        # -- Coins
        self.damage_list = arcade.tilemap.process_layer(my_map, 'Damage', TILE_SCALING)

        # -- Tweets
        self.tweet_list = arcade.tilemap.process_layer(my_map, 'Tweets', TILE_SCALING)

        # -- Tan
        self.tan_list = arcade.tilemap.process_layer(my_map, 'Tan', TILE_SCALING)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)
