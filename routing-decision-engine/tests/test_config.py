

from src.config import RouteConfig


def test_default_speed():
    config = RouteConfig()

    assert config.speed_kmh == 60


def test_vertical_multiplier():
    config = RouteConfig()

    result = config.get_distance_multiplier("vertical")

    assert result == 1.3


def test_horizontal_multiplier():
    config = RouteConfig()

    result = config.get_distance_multiplier("horizontal")

    assert result == 1.0


def test_unknown_mode_defaults_to_horizontal():
    config = RouteConfig()

    result = config.get_distance_multiplier("unknown")

    assert result == 1.0