from project import velocity_breakdown
from project import float_range
from project import displacement
import pytest
import math

def test_velocity_breakdown_45_degrees():
    velocity = 10
    angle = math.radians(45)
    u_x, u_y = velocity_breakdown(velocity, angle)

    #At 45 degrees, both are equal
    assert pytest.approx(u_x, 0.01) == pytest.approx(u_y, 0.01)

    angle = math.radians(90)
    u_x, u_y = velocity_breakdown(velocity, angle)

    #At 90 degrees, horizontal velocity is 0, vertical should be equal to velocity
    assert u_x == pytest.approx(0, 0.01)
    assert u_y == pytest.approx(velocity, 0.01)

    angle = math.radians(0)
    u_x, u_y = velocity_breakdown(velocity, angle)

    #At 0 degrees, vertical velocity is 0, horizontal should be equal to velocity
    assert u_x == pytest.approx(velocity, 0.01)
    assert u_y == pytest.approx(0, 0.01)

def test_float_range():
    result = list(float_range(0, 1, 0.2))
    expected = [0, 0.2, 0.4, 0.6, 0.8]
    assert round(result[4], 1) == expected[4]

    result = list(float_range(1, 0, 0.2))
    expected = []
    assert result == expected

def test_displacement():
    assert displacement(1, 2, 3) == 8
    assert displacement(2, 2, 2) == 8
