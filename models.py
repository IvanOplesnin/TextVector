def valid_float(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False


class Point:
    def __init__(self, x, y):
        # Проверяем является ли аргумент числом, аналогично в других классах.
        for arg in [x, y]:
            if not valid_float(arg):
                raise ValueError(f"Аргумент {arg} не является числом.")

        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False


class Square(Point):
    def __init__(self, x, y, side):
        for arg in [x, y, side]:
            if not valid_float(arg):
                raise ValueError(f"Аргумент {arg} не является числом.")

        super().__init__(x, y)
        self.side = float(side)

    def __repr__(self):
        return f"Square({self.x}, {self.y}, {self.side})"


class Circle(Point):
    def __init__(self, x, y, radius):
        for arg in [x, y, radius]:
            if not valid_float(arg):
                raise ValueError(f"Аргумент {arg} не является числом.")

        super().__init__(x, y)
        self.radius = float(radius)

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.radius})"


class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.point_start = Point(x1, y1)
        self.point_end = Point(x2, y2)
        if self.point_start == self.point_end:
            raise ValueError(
                "Начальная и конечная точки вектора совпадают. Невозможно создать вектор."
            )

    def __repr__(self):
        return f"Vector(({self.point_start.x}, {self.point_start.y}) -> ({self.point_end.x}, {self.point_end.y}))"
