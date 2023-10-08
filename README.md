## About

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Small lib implements geometric figures like square, circle, rectangle and so on. No external libs used, pure python only. Lib contains factories for each figure type, i recommed to use them instead of creating figures directly. So, some example of usage below:

### Usage (sample):

```python
from figures.figures import (
        TriangleT,
        new_triangle,
        ParamT,
        )


def get_triangle_dims() -> tuple[ParamT, ...]:
    return (2.0, 2.0, 2.8283)


def is_right_triangle(t: TriangleT) -> bool:
    """we use TriangleT for correct type-hint
    because Base2DFigure haven`t <is_right_triangle()>."""

    if t.is_right_triangle():
        print(f"Triangle {t} have angle 90 degrees.")
        return True
    print(f"Triangle {t} haven`t angle 90 degrees.")
    return False


def main() -> None:
    triangle = new_triangle(*get_triangle_dims())
    if is_right_triangle(triangle):
        print(f"Area is {triangle.area():.3f}")
        return
    print("Area not needed")
```

Output:

```bash
Triangle class Triangle(leg_a=2.0, leg_b=2.0, hopotenuse=2.8283) have angle 90 degrees.
Area is 2.000
```

We can calculate area in runtime, it`s not depended on a figure type:

```python

from typing import Sequence
from figures.figures import Base2DFigure


def runtime_area_calculation(figures: Sequence[Base2DFigure, ...]) -> None:
    """example of runtime usage."""
    for idx, fig in enumerate(figures):
        print(f"POS [{idx}] | FIGURE: {fig:<16} | AREA: {fig.area():<8}")

```

You can create `wheel` because of pure python:

```bash
python3 -m build --wheel
```

### Tests

Tests results are below:

```bash
============================================================================================================ test session starts =============================================================================================================
platform linux -- Python 3.11.4, pytest-7.4.2, pluggy-1.3.0 -- /home/egor_usual/figures-lib/fig-env/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/egor_usual/figures-lib
collected 24 items                                                                                                                                                                                                                           

test/circle_area_test.py::test_simp_circle_area_as_pi PASSED                                                                                                                                                                           [  4%]
test/circle_area_test.py::test_circle_raises_impossible_dim PASSED                                                                                                                                                                     [  8%]
test/circle_area_test.py::test_circle_area_calc_correct[2.0-12.56-0.01] PASSED                                                                                                                                                         [ 12%]
test/circle_area_test.py::test_circle_area_calc_correct[3.5-38.48-0.01] PASSED                                                                                                                                                         [ 16%]
test/circle_area_test.py::test_circle_area_calc_correct[1.47-6.78-0.01] PASSED                                                                                                                                                         [ 20%]
test/circle_area_test.py::test_new_circle_created_correct[1.5-7.06-0.01] PASSED                                                                                                                                                        [ 25%]
test/circle_area_test.py::test_new_circle_created_correct[2.3-16.61-0.01] PASSED                                                                                                                                                       [ 29%]
test/rectangle_area_test.py::test_rectangle_area_calc_correct PASSED                                                                                                                                                                   [ 33%]
test/rectangle_area_test.py::test_rectangle_raises_impossible_dim PASSED                                                                                                                                                               [ 37%]
test/rectangle_area_test.py::test_new_rectangle_working_correct[sides0-7.0-0.1] PASSED                                                                                                                                                 [ 41%]
test/square_area_test.py::test_rectangle_area_calc_correct PASSED                                                                                                                                                                      [ 45%]
test/square_area_test.py::test_rectangle_raises_impossible_dim PASSED                                                                                                                                                                  [ 50%]
test/square_area_test.py::test_new_square_working_correct[2.0-4.0-0.1] PASSED                                                                                                                                                          [ 54%]
test/triangle_area_test.py::test_triangle_area_valid XFAIL                                                                                                                                                                             [ 58%]
test/triangle_area_test.py::test_area_calculated_correct[args0-2.0-0.01] PASSED                                                                                                                                                        [ 62%]
test/triangle_area_test.py::test_area_calculated_correct[args1-12.99-0.01] PASSED                                                                                                                                                      [ 66%]
test/triangle_area_test.py::test_area_calculated_correct[args2-3.89-0.01] PASSED                                                                                                                                                       [ 70%]
test/triangle_area_test.py::test_is_right_triangle PASSED                                                                                                                                                                              [ 75%]
test/triangle_area_test.py::test_is_right_triangles[args0-True] PASSED                                                                                                                                                                 [ 79%]
test/triangle_area_test.py::test_is_right_triangles[args1-False] PASSED                                                                                                                                                                [ 83%]
test/triangle_area_test.py::test_is_right_triangles[args2-False] PASSED                                                                                                                                                                [ 87%]
test/triangle_area_test.py::test_raises_impossible_dims PASSED                                                                                                                                                                         [ 91%]
test/triangle_area_test.py::test_new_triangle_created_correct[args0-3.49-0.01] PASSED                                                                                                                                                  [ 95%]
test/triangle_area_test.py::test_new_triangle_created_correct[args1-5.73-0.01] PASSED                                                                                                                                                  [100%]

======================================================================================================= 23 passed, 1 xfailed in 0.05s ========================================================================================================
```

### Mypy

Mypy results are below:

```bash
Success: no issues found in 2 source files
```
