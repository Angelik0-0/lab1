import math


def area(r):
"""
    Возвращает плоащадь круга
            Параметры:
                    r (float): радиус круга
            Возвращаемое значение:
                    math.pi * r * r (float): площадь круга
    """
    return math.pi * r * r


def perimeter(r):
"""
    Возвращает длину окружности
            Параметры:
                    r (float): радиус окружности
            Возвращаемое значение:
                    2 * math.pi * r (float): длину окружности
    """
    return 2 * math.pi * r

