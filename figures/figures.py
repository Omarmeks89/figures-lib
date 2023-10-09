import math
from enum import Enum
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import (
        TypeAlias,
        cast,
        Optional,
        Union,
        Final,
        Mapping,
        Callable,
        ClassVar,
        Any,
        )


__all__ = (
        "Base2DFigure",
        "AreaT",
        "FigureType",
        "ParamT",
        "ImpossibleDimention",
        "FigureSpecError",
        "FigureTypeError",
        "calculate_figure_area",
        "is_triangle_right",
        "calculate_circle_area",
        "calculate_square_area",
        "calculate_triangle_area",
        "build_figure_spec",
        "calculate_rectangle_area",
        )


AreaT: TypeAlias = float
ParamT: TypeAlias = Union[float, Any]

_DEF_TOLERANCE: Final[ParamT] = 1e-3
_POW2: Final[int] = 2


class ImpossibleDimention(Exception):
    """Raises if one of args <= 0."""
    pass


class FigureSpecError(Exception):
    """Raises if invalid spec parameter found."""
    pass


class FigureTypeError(Exception):
    """Raises if unknown figure type found."""
    pass


class FigureType(str, Enum):
    """It`s possible to use int here
    but str() is most humanreadable."""
    SQUARE: str = "square"
    TRIANGLE: str = "triangle"
    CIRCLE: str = "circle"
    RECTANGLE: str = "rectangle"


@dataclass
class FigureSpec:
    ftype: FigureType
    args: tuple[ParamT, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.args, tuple):
            raise FigureSpecError("Args have to be inside a tuple.")
        if not isinstance(self.ftype, FigureType):
            raise FigureSpecError(
                    f"Invalid type {type(self.ftype)} for <ftype> attr. "
                    f"Need <FigureType>, choose from them."
                    )


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
        if not _args_bigger_as_zero(self._radius):
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
        if not _args_bigger_as_zero(
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
        if not _args_bigger_as_zero(
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
        if not _args_bigger_as_zero(self._side):
            raise ImpossibleDimention(
                    "Dimentions shold be bigger as zero."
                    )

    def __repr__(self) -> str:
        return f"class {type(self).__name__}(side={self._side})"

    def area(self) -> AreaT:
        return cast(AreaT, math.pow(self._side, _POW2))


def _args_bigger_as_zero(*args) -> bool:
    """Check that args are bigger as zero."""
    for a in args:
        if a <= 0:
            return False
    return True


def _new_circle(radius: ParamT) -> Circle:
    """base factory func for circle creation.
    Prefer using that func creating object directly."""
    return Circle(radius)


def _new_triangle(
        leg_a: ParamT,
        leg_b: ParamT,
        hopotenuse: ParamT,
        *,
        rel_tolerance: Optional[ParamT] = None,
        ) -> Triangle:
    """base factory func for circle creation.
    Prefer using that func creating object directly."""
    return Triangle(leg_a, leg_b, hopotenuse, rel_tol=rel_tolerance)


def _new_square(side: ParamT) -> Square:
    """base factory func for square creation.
    Prefer using that func creating object directly."""
    return Square(side)


def _new_rectangle(side_a: ParamT, side_b: ParamT) -> Rectangle:
    """base factory func for rectangle creation.
    Prefer using that func creating object directly."""
    return Rectangle(side_a, side_b)


def calculate_circle_area(radius: ParamT) -> AreaT:
    """calculate circle area."""
    return _new_circle(radius).area()


def calculate_square_area(side: ParamT) -> AreaT:
    """calculate square area."""
    return _new_square(side).area()


def calculate_triangle_area(leg_a: ParamT, leg_b: ParamT, hopotenuse: ParamT) -> AreaT:
    """calculate triangle area."""
    return _new_triangle(leg_a, leg_b, hopotenuse).area()


def calculate_rectangle_area(side_a: ParamT, side_b: ParamT) -> AreaT:
    """calculate reactangle area."""
    return _new_rectangle(side_a, side_b).area()


def is_triangle_right(
        leg_a: ParamT,
        leg_b: ParamT,
        hopotenuse: ParamT,
        *,
        rel_tolerance: ParamT,
        ) -> bool:
    """check on 90 degree angle (in triangle)
    Can set wished tolerance, if not set, tolerance will be
    1e-3 by default (see _DEF_TOLERANCE)."""
    return (
            _new_triangle(leg_a, leg_b, hopotenuse, rel_tolerance=rel_tolerance)
            .is_right_triangle()
            )


class _TypeMapper(ABC):

    @classmethod
    @abstractmethod
    def fig_type_contains(cls, ftype: FigureType) -> bool: pass


class _TypeSwitch(_TypeMapper):
    """switch type for internal using."""

    _tmap: ClassVar[Mapping[FigureType, Callable[..., AreaT]]] = {
            FigureType.SQUARE: calculate_square_area,
            FigureType.TRIANGLE: calculate_triangle_area,
            FigureType.CIRCLE: calculate_circle_area,
            FigureType.RECTANGLE: calculate_rectangle_area,
            }

    @classmethod
    def choose_fig_type(cls, ftype: FigureType) -> Callable[..., AreaT]:
        """we needn`t call .get(), because we`re calling
        fig_type_contains() before."""
        return cls._tmap[ftype]

    @classmethod
    def fig_type_contains(cls, ftype: FigureType) -> bool:
        """check that type is specified."""
        return ftype in cls._tmap


class _ArgsCounter(_TypeMapper):
    """get args count for check by FigureType."""

    _args_cnt_map: ClassVar[Mapping[FigureType, int]] = {
            FigureType.CIRCLE: 1,
            FigureType.RECTANGLE: 2,
            FigureType.SQUARE: 1,
            FigureType.TRIANGLE: 3,
            }

    @classmethod
    def args_count_matched(cls, ftype: FigureType, args: tuple[ParamT, ...]) -> bool:
        return len(args) == cls._args_cnt_map[ftype]

    @classmethod
    def fig_type_contains(cls, ftype: FigureType) -> bool:
        """check that type is specified."""
        return ftype in cls._args_cnt_map

    @classmethod
    def get_args_count(cls, ftype: FigureType) -> int:
        """get args count from preset."""
        return cls._args_cnt_map[ftype]


def calculate_figure_area(spec: FigureSpec) -> AreaT:
    """calculate area without knowledge
    about exact figure type."""
    if _TypeSwitch.fig_type_contains(spec.ftype):
        areaf = _TypeSwitch.choose_fig_type(spec.ftype)
        return areaf(*spec.args)
    raise FigureTypeError(f"No type <{spec.ftype}> specified.")


def build_figure_spec(ftype: FigureType, /, *args) -> FigureSpec:
    msg = f"No type <{ftype}> specified."
    if _ArgsCounter.fig_type_contains(ftype):
        if _ArgsCounter.args_count_matched(ftype, args):
            return FigureSpec(ftype=ftype, args=args)
        cnt = _ArgsCounter.get_args_count(ftype)
        msg = f"Args count in {args} not mathed. Got: {len(args)}, need: {cnt}"
        raise FigureSpecError(msg)
    raise FigureTypeError(msg)
