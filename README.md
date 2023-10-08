## About


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
