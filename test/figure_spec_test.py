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
