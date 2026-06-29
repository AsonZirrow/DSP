

class RouteConfig:
    def __init__(self):
        # Core settings
        self.speed_kmh = 60

        # Distance modifiers
        self.vertical_penalty = 1.3
        self.horizontal_penalty = 1.0

    def get_distance_multiplier(self, mode="horizontal"):
        if mode == "vertical":
            return self.vertical_penalty
        return self.horizontal_penalty