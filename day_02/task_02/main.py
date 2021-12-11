
if __name__ == '__main__':
    """Reads in a set of command and values from a file and modifies
    horizontal_position, depth, and aim following some defined rules. 
    Depth and horizontal_position are multiplied in the final operation."""
    input_data = open('./input_data')
    input_data = open('./input_data')
    horizontal_position = 0
    depth = 0
    aim = 0

    for data_line in input_data:
        command, value = data_line.split()
        value = int(value)

        if command == 'forward':
            horizontal_position += value
            depth += aim * value
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value

    print(horizontal_position * depth)
