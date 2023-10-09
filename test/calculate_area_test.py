from enum import Enum

import pytest

from figures import (
        FigureSpec,
        FigureType,
        FigureTypeError,
        calculate_figure_area,
        )


class MockFigType(str, Enum):
    ANY: str = "any"


@pytest.fixture(scope="function")
def inv_spec(circ_spec: FigureSpec) -> FigureSpec:
    circ_spec.ftype = MockFigType.ANY
    return circ_spec


def test_area_calculated_by_spec(circ_spec: FigureSpec) -> None:
    assert calculate_figure_area(circ_spec) == pytest.approx(3.14, 1e-2)


def test_calculate_figure_area_raises_figuretypeerror(inv_spec: FigureSpec) -> None:
    with pytest.raises(FigureTypeError):
        calculate_figure_area(inv_spec)


def test_calculate_figure_area_calc_rectangle(rectangle_spec: FigureSpec) -> None:
    assert calculate_figure_area(rectangle_spec) == pytest.approx(12.0, 1e-1)


def test_calculate_figure_area_calc_square(square_spec: FigureSpec) -> None:
    sp = FigureSpec(FigureType.SQUARE, (3.0, ))
    assert calculate_figure_area(sp) == pytest.approx(9.0, 1e-1)


def test_calculate_figure_area_calc_triangle(triangle_spec: FigureSpec) -> None:
    assert calculate_figure_area(triangle_spec) == pytest.approx(2.0, 1e-1)
