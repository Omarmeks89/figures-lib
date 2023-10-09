## About

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Small lib implements geometric figures like square, circle, rectangle and so on. No external libs used, pure python only. Lib contains factories for each figure type, i recommed to use them instead of creating figures directly. So, some example of usage below:

### Usage (sample):

```python
from figures.figures import (
        circle_area,
        triangle_area,
        is_triangle_right,
        )


c_area = circle_area(1.0)
print(c_area)

tr_area = triangle_area(2.0, 2.0, 2.8283)
print(tr_area)

# check that triangle have 90 degree angle
print(is_triangle_right(2.0, 2.0, 2.8283, rel_tolerance=1e-2))
```

Output:

```bash

>>> 3.141592653589793

>>> 2.00

>>> True
```
We can implement specification for each figure and
collect them all together

```python

from typing import Sequence
from figures.figures import (
        FigureType,
        FigureSpec,
        build_figure_spec,
        FigureTypeError,
        calculate_area,
        )


def calc_area_from(figures: Sequence[FigureSpec, ...]) -> None:
    """we don`t know about exact figure type at the moment."""
    for idx, spec in enumerate(figures):
        try:
            print(calculate_area(spec))
        except FigureTypeError as err:
            print(f"Failed calculate area from spec {spec}, pos {idx}, {err=}")


# but we should create specifications previously
specs = []
specs.append(build_figure_spec(FigureType.SQUARE, (1.5,)))
specs.append(build_figure_spec(FigureType.CIRCLE, (2.5,)))
specs.append(build_figure_spec(FigureType.RECTANGLE, (2.5, 3.8)))


# then using spec as a parameter
calc_area_from(specs)

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
collected 33 items                                                                                                                                                                                                                           

test/calculate_area_test.py::test_area_calculated_by_spec PASSED                                                                                                                                                                       [  3%]
test/calculate_area_test.py::test_calculate_area_raises_figuretypeerror PASSED                                                                                                                                                         [  6%]
test/calculate_area_test.py::test_calculate_area_calc_rectangle PASSED                                                                                                                                                                 [  9%]
test/calculate_area_test.py::test_calculate_area_calc_square PASSED                                                                                                                                                                    [ 12%]
test/calculate_area_test.py::test_calculate_area_calc_triangle PASSED                                                                                                                                                                  [ 15%]
test/circle_area_test.py::test_simp_circle_area_as_pi PASSED                                                                                                                                                                           [ 18%]
test/circle_area_test.py::test_circle_raises_impossible_dim PASSED                                                                                                                                                                     [ 21%]
test/circle_area_test.py::test_circle_area_calc_correct[2.0-12.56-0.01] PASSED                                                                                                                                                         [ 24%]
test/circle_area_test.py::test_circle_area_calc_correct[3.5-38.48-0.01] PASSED                                                                                                                                                         [ 27%]
test/circle_area_test.py::test_circle_area_calc_correct[1.47-6.78-0.01] PASSED                                                                                                                                                         [ 30%]
test/circle_area_test.py::test_new_circle_created_correct[1.5-7.06-0.01] PASSED                                                                                                                                                        [ 33%]
test/circle_area_test.py::test_new_circle_created_correct[2.3-16.61-0.01] PASSED                                                                                                                                                       [ 36%]
test/figure_spec_test.py::test_invalid_spec_raises_figurespecerror PASSED                                                                                                                                                              [ 39%]
test/figure_spec_test.py::test_invalid_spec_raises_figurespecerror_on_unkn_figtype PASSED                                                                                                                                              [ 42%]
test/figure_spec_test.py::test_build_figure_spec_raises_fse PASSED                                                                                                                                                                     [ 45%]
test/figure_spec_test.py::test_build_figure_spec_raises_fte PASSED                                                                                                                                                                     [ 48%]
test/rectangle_area_test.py::test_rectangle_area_calc_correct PASSED                                                                                                                                                                   [ 51%]
test/rectangle_area_test.py::test_rectangle_raises_impossible_dim PASSED                                                                                                                                                               [ 54%]
test/rectangle_area_test.py::test_new_rectangle_working_correct[sides0-7.0-0.1] PASSED                                                                                                                                                 [ 57%]
test/square_area_test.py::test_rectangle_area_calc_correct PASSED                                                                                                                                                                      [ 60%]
test/square_area_test.py::test_rectangle_raises_impossible_dim PASSED                                                                                                                                                                  [ 63%]
test/square_area_test.py::test_new_square_working_correct[2.0-4.0-0.1] PASSED                                                                                                                                                          [ 66%]
test/triangle_area_test.py::test_triangle_area_valid XFAIL                                                                                                                                                                             [ 69%]
test/triangle_area_test.py::test_area_calculated_correct[args0-2.0-0.01] PASSED                                                                                                                                                        [ 72%]
test/triangle_area_test.py::test_area_calculated_correct[args1-12.99-0.01] PASSED                                                                                                                                                      [ 75%]
test/triangle_area_test.py::test_area_calculated_correct[args2-3.89-0.01] PASSED                                                                                                                                                       [ 78%]
test/triangle_area_test.py::test_is_right_triangle PASSED                                                                                                                                                                              [ 81%]
test/triangle_area_test.py::test_is_right_triangles[args0-True] PASSED                                                                                                                                                                 [ 84%]
test/triangle_area_test.py::test_is_right_triangles[args1-False] PASSED                                                                                                                                                                [ 87%]
test/triangle_area_test.py::test_is_right_triangles[args2-False] PASSED                                                                                                                                                                [ 90%]
test/triangle_area_test.py::test_raises_impossible_dims PASSED                                                                                                                                                                         [ 93%]
test/triangle_area_test.py::test_new_triangle_created_correct[args0-3.49-0.01] PASSED                                                                                                                                                  [ 96%]
test/triangle_area_test.py::test_new_triangle_created_correct[args1-5.73-0.01] PASSED                                                                                                                                                  [100%]

======================================================================================================= 32 passed, 1 xfailed in 0.07s ========================================================================================================
```

### Mypy

Mypy results are below:

```bash
Success: no issues found in 2 source files
```
