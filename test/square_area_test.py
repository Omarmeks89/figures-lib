import pytest

from figures import Square, ImpossibleDimention, new_square


def test_rectangle_area_calc_correct(simp_square: Square) -> None:
    """test that area 1.0 * 1.0 = 1.0"""
    assert simp_square.area() == pytest.approx(1.0, 1e-1)


def test_rectangle_raises_impossible_dim() -> None:
    with pytest.raises(ImpossibleDimention):
        Square(-0.5)


@pytest.mark.parametrize(
        "side,area,tol",
        [
            (2.0, 4.0, 1e-1),
            ]
        )
def test_new_square_working_correct(side: float, area: float, tol: float) -> None:
    ns = new_square(side)
    assert isinstance(ns, Square) is True, "not square"
    assert ns.area() == pytest.approx(area, tol)
