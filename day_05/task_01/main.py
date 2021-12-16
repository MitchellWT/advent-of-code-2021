

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def is_vertical_line(point_one: Point, point_two: Point) -> bool:
    if point_one.x == point_two.x:
        return True
    return False


def is_horizontal_line(point_one: Point, point_two: Point) -> bool:
    if point_one.y == point_two.y:
        return True
    return False


if __name__ == "__main__":
    input_data = open('./input_data')
    points = []
    max_x = 0
    max_y = 0

    for input_line in input_data:
        input_points = input_line.split('->')
        point_list = []
        for input_point in input_points:
            point_data = input_point.split(',')
            new_point = Point(
                int(point_data[0]),
                int(point_data[1])
            )
            point_list.append(new_point)
            if new_point.x > max_x:
                max_x = new_point.x
            if new_point.y > max_y:
                max_y = new_point.y
        if is_horizontal_line(point_list[0], point_list[1]) or is_vertical_line(point_list[0], point_list[1]):
            points.append(point_list)

    vent_diagram = []
    # Fill vent diagram with default value (0)
    for y in range(max_y + 1):
        new_line = []
        for x in range(max_x + 1):
            new_line.append(0)
        vent_diagram.append(new_line)

    for point_list in points:
        if is_vertical_line(point_list[0], point_list[1]):
            # X won't change
            point_one = point_list[0]
            point_two = point_list[1]
            if point_list[1].y < point_list[0].y:
                point_one = point_list[1]
                point_two = point_list[0]

            for y_moving in range(point_one.y, point_two.y + 1):
                vent_diagram[y_moving][point_one.x] += 1
        elif is_horizontal_line(point_list[0], point_list[1]):
            # Y won't change
            point_one = point_list[0]
            point_two = point_list[1]
            if point_list[1].x < point_list[0].x:
                point_one = point_list[1]
                point_two = point_list[0]

            for x_moving in range(point_one.x, point_two.x + 1):
                vent_diagram[point_one.y][x_moving] += 1


    danger_zone = 0
    # Calculate danger zone value
    for vent_line in vent_diagram:
        for vent_value in vent_line:
            if vent_value > 1:
                danger_zone += 1

    print(danger_zone)
