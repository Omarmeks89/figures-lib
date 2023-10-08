import pytest

from figures import Circle, ImpossibleDimention


def test_simp_circle_area_as_pi(simp_circle) -> None:
    """circle with r = 1.0 have area = 3.14..."""
    assert simp_circle.area() == pytest.approx(3.14, 1e-2), "simp failed"


def test_circle_raises_impossible_dim() -> None:
    with pytest.raises(ImpossibleDimention):
        Circle(0.0)


@pytest.mark.parametrize(
        "rad,area,tol",
        [
            (2.0, 12.56, 1e-2),
            (3.5, 38.48, 1e-2),
            (1.47, 6.78, 1e-2),
            ]
        )
def test_circle_area_calc_correct(rad: float, area: float, tol: float) -> None:
    c = Circle(rad)
    assert c.area() == pytest.approx(area, tol)
