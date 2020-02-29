import arcade

TILE_SCALING = 0.5
COIN_SCALING = 0.5

class Map:
    def __init__(self, mapName):
        # Name of map file to load
        map_name = "./maps/map.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        damage_layer_name = 'Damage'
        tweets_layer_name = 'Tweets'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(my_map, platforms_layer_name, TILE_SCALING)

        # -- Coins
        self.damage_list = arcade.tilemap.process_layer(my_map, damage_layer_name, TILE_SCALING)

        # -- Tweets

        self.tweet_list = arcade.tilemap.process_layer(my_map, tweets_layer_name, TILE_SCALING)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)
