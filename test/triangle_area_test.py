import pytest

from figures import Triangle, ImpossibleDimention


@pytest.mark.xfail
def test_triangle_area_valid(not_right_triangle: Triangle) -> None:
    assert not_right_triangle.is_right_triangle() is True


@pytest.mark.parametrize(
        "args,area,tol",
        [
            ((2.0, 2.0, 2.8283), 2.00, 1e-2),
            ((4.0, 6.5, 7.6321), 12.99, 1e-2),
            ((3.0, 3.0, 3.0), 3.89, 1e-2),
            ]
        )
def test_area_calculated_correct(args: tuple, area: float, tol: float) -> None:
    t = Triangle(*args)
    assert t.area() == pytest.approx(area, tol)


def test_is_right_triangle(right_triangle: Triangle) -> None:
    """default tol in <figures> pack is 1e-3."""
    assert right_triangle.is_right_triangle() is True


@pytest.mark.parametrize(
        "args,res",
        [
            ((2.0, 4.0, 4.4721), True),
            ((2.0, 4.0, 6.0), False),
            ((2.0, 2.0, 2.0), False),
            ]
        )
def test_is_right_triangles(args: tuple, res: bool) -> None:
    t = Triangle(*args)
    assert t.is_right_triangle() == res, "Fail"


def test_raises_impossible_dims() -> None:
    """area will have no sence if args <= 0."""
    with pytest.raises(ImpossibleDimention):
        Triangle(-1.0, 6.0, 1.0)
