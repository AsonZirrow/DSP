

from src.calculator import RouteCalculator


def test_compute_time_valid():
    calc = RouteCalculator()

    result = calc.compute_time(100, 50)

    assert result == 2.0


def test_compute_time_invalid_speed():
    calc = RouteCalculator()

    result = calc.compute_time(100, 0)

    assert result is None


def test_distance_multiplier():
    calc = RouteCalculator()

    result = calc.compute_distance_with_penalty(10, 1.3)

    assert result == 13.0