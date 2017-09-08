class Settings():
    """Where we will change/update new settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 700
        self.color = (5, 20, 33)
        self.ship_speed_fac = 10
        self.version = "v1.0"
        self.author = "By. Pat"

        #Normal Bullet settings
        self.norm_bullet_speed = 7
        self.norm_bullet_width = 3
        self.norm_bullet_height = 15
        self.norm_bullet_color = 226, 0, 0

        #Missel settings
        self.missel_speed = 15
        self.missel_width = 6
        self.missel_height = 20
        self.missel_color = 50, 60, 70