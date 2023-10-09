import pytest

from figures import Rectangle, ImpossibleDimention, _new_rectangle


def test_rectangle_area_calc_correct(simp_rectangle: Rectangle) -> None:
    """test that area 1.0 * 2.0 = 2.0"""
    assert simp_rectangle.area() == pytest.approx(2.0, 1e-1)


def test_rectangle_raises_impossible_dim() -> None:
    with pytest.raises(ImpossibleDimention):
        Rectangle(-0.5, 12.0)


@pytest.mark.parametrize(
        "sides,area,tol",
        [
            ((2.0, 3.5), 7.0, 1e-1),
            ]
        )
def test_new_rectangle_working_correct(sides: float, area: float, tol: float) -> None:
    nr = _new_rectangle(*sides)
    assert isinstance(nr, Rectangle) is True, "not rectangle"
    assert nr.area() == pytest.approx(area, tol)
