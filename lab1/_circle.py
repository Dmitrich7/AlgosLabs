import math

def calculate_circle_area(radius):
    return round(math.pi * radius ** 2, 4)

def calculate_distance_from_origin(point):
    return math.sqrt(point[0] ** 2 + point[1] ** 2)

def is_point_inside_circle(point, radius):
    return calculate_distance_from_origin(point) <= radius

def get_circle_radius():
    return float(input("Введите радиус круга: "))

def get_point_coordinates():
    x = float(input("Введите координату X точки: "))
    y = float(input("Введите координату Y точки: "))
    return (x, y)

def show_circle_area(radius):
    area = calculate_circle_area(radius)
    print(f"Площадь круга с радиусом {radius}: {area}")

def show_point_position(point, radius):
    inside = is_point_inside_circle(point, radius)
    print(f"Точка с координатами {point} внутри круга: {inside}")

def main():
    radius = get_circle_radius()

    point_1 = get_point_coordinates()
    point_2 = get_point_coordinates()

    show_circle_area(radius)

    show_point_position(point_1, radius)
    show_point_position(point_2, radius)

if __name__ == "__main__":
    main()
