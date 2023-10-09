import pytest

from figures import Triangle, ImpossibleDimention, _new_triangle
from figures import is_triangle_right


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
    assert right_triangle.is_right_triangle() is True


def test_is_right_triangle_func_is_correct() -> None:
    assert is_triangle_right(2.0, 2.0, 2.8283, rel_tolerance=1e-2) is True


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


@pytest.mark.parametrize(
        "args,area,tol",
        [
            ((2.0, 3.5, 4.1), 3.49, 1e-2),
            ((3.5, 3.6, 3.85), 5.73, 1e-2),
            ]
        )
def test_new_triangle_created_correct(args: tuple, area: float, tol: float) -> None:
    nt = _new_triangle(*args)
    assert isinstance(nt, Triangle) is True, "not circle"
    assert nt.area() == pytest.approx(area, tol)
