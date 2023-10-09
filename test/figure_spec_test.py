import pytest

from figures import (
        FigureSpec,
        FigureType,
        FigureSpecError,
        FigureTypeError,
        build_figure_spec,
        )


def test_invalid_spec_raises_figurespecerror() -> None:
    with pytest.raises(FigureSpecError):
        FigureSpec(FigureType.CIRCLE, 1.0)


def test_invalid_spec_raises_figurespecerror_on_unkn_figtype() -> None:
    with pytest.raises(FigureSpecError):
        FigureSpec("circle", (1.0, ))


def test_build_figure_spec_raises_fse() -> None:
    with pytest.raises(FigureSpecError):
        build_figure_spec("circle", (1.2,))


def test_build_figure_spec_raises_fte() -> None:
    with pytest.raises(FigureTypeError):
        build_figure_spec("any", (1.2,))


def test_build_figure_spec_raises_fse_args_cnt() -> None:
    """Error raised if not enough args detected."""
    with pytest.raises(FigureSpecError):
        build_figure_spec(FigureType.TRIANGLE, 1.2, 2.3)


def test_build_circle_spec_succ() -> None:
    spec = build_figure_spec(FigureType.CIRCLE, 1.0)
    assert isinstance(spec, FigureSpec) is True, "inv type"


def test_build_square_spec_succ() -> None:
    spec = build_figure_spec(FigureType.SQUARE, 1.5)
    assert isinstance(spec, FigureSpec) is True, "inv type"


def test_build_rectangle_spec_succ() -> None:
    spec = build_figure_spec(FigureType.RECTANGLE, 1.0, 2.3)
    assert isinstance(spec, FigureSpec) is True, "inv type"


def test_build_triangle_spec_succ() -> None:
    spec = build_figure_spec(FigureType.TRIANGLE, 1.0, 2.0, 2.4)
    assert isinstance(spec, FigureSpec) is True, "inv type"
