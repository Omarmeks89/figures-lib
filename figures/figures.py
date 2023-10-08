import math
from abc import ABC, abstractmethod
from typing import (
        TypeVar,
        TypeAlias,
        cast,
        Optional,
        Union,
        Final,
        Any,
        )


__all__ = (
        "Base2DFigure",
        "AreaT",
        "ParamT",
        "TriangleT",
        "Circle",
        "Square",
        "Rectangle",
        "Triangle",
        "new_circle",
        "new_triangle",
        "new_rectangle",
        "new_square",
        "ImpossibleDimention",
        )


AreaT: TypeAlias = float
ParamT: TypeAlias = Union[float, Any]

_DEF_TOLERANCE: Final[ParamT] = 1e-3
_POW2: Final[int] = 2

# use for type-hinting purposes, where we need to use
# <is_right_triangle()> method. Other cases prefer to use
# <Base2DFigure> for hinting.
TriangleT = TypeVar("TriangleT", bound="TriangleMixin")

_CF = TypeVar("_CF", bound="AbcFigure", contravariant=True)
_F = TypeVar("_F", bound="AbcFigure", covariant=True)


class ImpossibleDimention(Exception):
    """Raises if one of args <= 0."""
    pass


class AbcFigure(ABC):

    @abstractmethod
    def area(self) -> AreaT: pass


class Base2DFigure(AbcFigure):
    """Base class for 2D figures."""

    def __repr__(self) -> str:
        return f"class {type(self).__name__}()"


class CircleMixin(ABC):
    """Mixin to create circles.
    Define object-attrs initializer."""

    @abstractmethod
    def __init__(self, radius: ParamT) -> None: pass


class TriangleMixin(ABC):
    """Mixin to create traingles.
    Define object-attrs initializer."""

    @abstractmethod
    def __init__(
            self,
            leg_a: ParamT,
            leg_b: ParamT,
            hopotenuse: ParamT,
            ) -> None: pass

    @abstractmethod
    def is_right_triangle(self, *, rel_tol: Optional[ParamT] = None) -> bool:
        pass


class RectangleMixin(ABC):
    """Mixin to create rectangles.
    Define object-attrs initializer."""

    @abstractmethod
    def __init__(self, side_a: ParamT, side_b: ParamT) -> None: pass


class SquareMixin(ABC):
    """Mixin to create squares.
    Define object-attrs initializer."""

    @abstractmethod
    def __init__(self, side: ParamT) -> None: pass


class Circle(CircleMixin, Base2DFigure):

    def __init__(self, radius: ParamT) -> None:
        self._radius = radius
        if not _args_bigger_or_eq_zero(self._radius):
            raise ImpossibleDimention(
                    "Dimentions shold be bigger as zero."
                    )

    def __repr__(self) -> str:
        return f"class {type(self).__name__}(r={self._radius})"

    def area(self) -> AreaT:
        """return area of circle."""
        return cast(AreaT, math.pi * math.pow(self._radius, _POW2))


class Triangle(TriangleMixin, Base2DFigure):

    def __init__(
            self,
            leg_a: ParamT,
            leg_b: ParamT,
            hopotenuse: ParamT,
            *,
            rel_tol: Optional[ParamT] = None,
            ) -> None:
        self._leg_a = leg_a
        self._leg_b = leg_b
        self._hpt = hopotenuse
        self._tol = rel_tol or _DEF_TOLERANCE
        if not _args_bigger_or_eq_zero(
                self._leg_a,
                self._leg_b,
                self._hpt,
                ):
            raise ImpossibleDimention(
                    "Dimentions shold be bigger as zero."
                    )

    def __repr__(self) -> str:
        return (
            f"class {type(self).__name__}(leg_a={self._leg_a}, "
            f"leg_b={self._leg_b}, hopotenuse={self._hpt})"
            )

    def is_right_triangle(self, *, rel_tol: Optional[ParamT] = None) -> bool:
        """Check do we have right triangle or not.
        Possible to set tolerance of comparison (safe)."""
        tol = rel_tol or self._tol
        return math.isclose(
            math.pow(self._hpt, _POW2),
            math.pow(self._leg_a, _POW2) + math.pow(self._leg_b, _POW2),
            rel_tol=tol,
            )

    def area(self) -> AreaT:
        """Heron`s method (we know all 3 sides)."""
        p = sum((self._leg_a, self._leg_b, self._hpt)) / 2
        return cast(
                AreaT,
                math.sqrt(
                    p * (p - self._leg_a) * (p - self._leg_b) * (p - self._hpt)
                    )
                )


class Rectangle(RectangleMixin, Base2DFigure):

    def __init__(self, side_a: ParamT, side_b: ParamT) -> None:
        self._side_a = side_a
        self._side_b = side_b
        if not _args_bigger_or_eq_zero(
                self._side_a,
                self._side_b,
                ):
            raise ImpossibleDimention(
                    "Dimentions shold be bigger as zero."
                    )

    def __repr__(self) -> str:
        return (
            f"class {type(self).__name__}(side_a={self._side_a}, "
            f"side_b={self._side_b})"
            )

    def area(self) -> AreaT:
        return cast(AreaT, self._side_a * self._side_b)


class Square(SquareMixin, Base2DFigure):

    def __init__(self, side: ParamT) -> None:
        self._side = side
        if not _args_bigger_or_eq_zero(self._side):
            raise ImpossibleDimention(
                    "Dimentions shold be bigger as zero."
                    )

    def __repr__(self) -> str:
        return f"class {type(self).__name__}(side={self._side})"

    def area(self) -> AreaT:
        return cast(AreaT, math.pow(self._side, _POW2))


def _args_bigger_or_eq_zero(*args) -> bool:
    """Check that args are bigger as zero."""
    for a in args:
        if a <= 0:
            return False
    return True


def new_circle(radius: ParamT) -> Circle:
    """base factory func for circle creation.
    Prefer using that func creating object directly."""
    return Circle(radius)


def new_triangle(
        leg_a: ParamT,
        leg_b: ParamT,
        hopotenuse: ParamT,
        *,
        rel_tolerance: Optional[ParamT] = None,
        ) -> Triangle:
    """base factory func for circle creation.
    Prefer using that func creating object directly."""
    return Triangle(leg_a, leg_b, hopotenuse, rel_tol=rel_tolerance)


def new_square(side: ParamT) -> Square:
    """base factory func for square creation.
    Prefer using that func creating object directly."""
    return Square(side)


def new_rectangle(side_a: ParamT, side_b: ParamT) -> Rectangle:
    """base factory func for rectangle creation.
    Prefer using that func creating object directly."""
    return Rectangle(side_a, side_b)
