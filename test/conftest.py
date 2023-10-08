import pytest

from figures import (
        Triangle,
        Circle,
        Rectangle,
        Square,
        )


@pytest.fixture(scope="session")
def not_right_triangle() -> Triangle:
    """angle between a & b != 90 degree."""
    return Triangle(2.0, 3.0, 4.2)


@pytest.fixture(scope="session")
def right_triangle() -> Triangle:
    return Triangle(2.0, 2.0, 2.8283)


@pytest.fixture(scope="session")
def simp_circle() -> Circle:
    return Circle(1.0)


@pytest.fixture(scope="session")
def simp_rectangle() -> Rectangle:
    return Rectangle(1.0, 2.0)


@pytest.fixture(scope="session")
def simp_square() -> Square:
    return Square(1.0)
