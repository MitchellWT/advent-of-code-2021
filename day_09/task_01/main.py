
if __name__ == '__main__':
    heightmap = []
    with open('./input_data') as input_data:
        for input_line in input_data:
            height_line = [int(x) for x in input_line.replace('\n', '')]
            heightmap.append(height_line)

    max_x = len(heightmap[0]) - 1
    max_y = len(heightmap) - 1
    risk_level = 0
    for y, height_line in enumerate(heightmap):
        for x, height in enumerate(height_line):
            low_point = True
            if y != 0 and heightmap[y - 1][x] <= height:
                low_point = False
            if y != max_y and heightmap[y + 1][x] <= height:
                low_point = False
            if x != 0 and heightmap[y][x - 1] <= height:
                low_point = False
            if x != max_x and heightmap[y][x + 1] <= height:
                low_point = False
            if low_point:
                risk_level += (height + 1)

    print(risk_level)
