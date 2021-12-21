from termcolor import colored

if __name__ == '__main__':
    heightmap = []
    with open('./input_data') as input_data:
        for input_line in input_data:
            height_line = [int(x) for x in input_line.replace('\n', '')]
            heightmap.append(height_line)

    max_x = len(heightmap[0]) - 1
    max_y = len(heightmap) - 1
    low_points = []
    # Finds low points
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
                low_points.append([y, x, height])

    basin_data = []
    for low_point in low_points:
        current_basin = [low_point]
        adjacent_points = []
        y = low_point[0]
        x = low_point[1]
        height = low_point[2]

        if y != 0 and heightmap[y - 1][x] != 9:
            adjacent_points.append([y - 1, x, heightmap[y - 1][x]])
        if y != max_y and heightmap[y + 1][x] != 9:
            adjacent_points.append([y + 1, x, heightmap[y + 1][x]])
        if x != 0 and heightmap[y][x - 1] != 9:
            adjacent_points.append([y, x - 1, heightmap[y][x - 1]])
        if x != max_x and heightmap[y][x + 1] != 9:
            adjacent_points.append([y, x + 1, heightmap[y][x + 1]])

        basin_stop = False
        while not basin_stop:
            new_adjacent_points = []
            for adjacent_point in adjacent_points:
                y = adjacent_point[0]
                x = adjacent_point[1]
                height = adjacent_point[2]

                if y != 0 and [y - 1, x, heightmap[y - 1][x]] not in current_basin \
                        and [y - 1, x, heightmap[y - 1][x]] not in new_adjacent_points and heightmap[y - 1][x] != 9:
                    new_adjacent_points.append([y - 1, x, heightmap[y - 1][x]])
                if y != max_y and [y + 1, x, heightmap[y + 1][x]] not in current_basin \
                        and [y + 1, x, heightmap[y + 1][x]] not in new_adjacent_points and heightmap[y + 1][x] != 9:
                    new_adjacent_points.append([y + 1, x, heightmap[y + 1][x]])
                if x != 0 and [y, x - 1, heightmap[y][x - 1]] not in current_basin \
                        and [y, x - 1, heightmap[y][x - 1]] not in new_adjacent_points and heightmap[y][x - 1] != 9:
                    new_adjacent_points.append([y, x - 1, heightmap[y][x - 1]])
                if x != max_x and [y, x + 1, heightmap[y][x + 1]] not in current_basin \
                        and [y, x + 1, heightmap[y][x + 1]] not in new_adjacent_points and heightmap[y][x + 1] != 9:
                    new_adjacent_points.append([y, x + 1, heightmap[y][x + 1]])
            current_basin.extend(adjacent_points)
            adjacent_points = new_adjacent_points
            if len(adjacent_points) == 0:
                basin_stop = True
        basin_data.append(current_basin)

    basin_size = []
    for basin in basin_data:
        basin_size.append(len(basin))

    output_value = max(basin_size)
    basin_size.remove(output_value)

    multiply_temp = max(basin_size)
    basin_size.remove(multiply_temp)

    output_value *= multiply_temp
    output_value *= max(basin_size)

    print(output_value)

    # Prints out the 'lava map'
    for y, height_line in enumerate(heightmap):
        for x, height in enumerate(height_line):
            if heightmap[y][x] == 9:
                print(colored('\u2588', 'white', attrs=['dark']), end='')
            else:
                print(colored('\u2588', 'red', attrs=['dark']), end='')
        print()
