class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = float("inf")

        self.fleet_drop_speed = 10

        self.speed_up_scale = 1.1
        self.score_scale = 1.5

        self.initializate_dynamic_settings()

    def initializate_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.0
        # 1 - движение вправо, -1 - влево
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)
