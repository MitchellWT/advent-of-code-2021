
if __name__ == '__main__':
    """Reads in a set of command and values from a file and modifies
    horizontal_position and depth following some defined rules. 
    These values are multiplies in the final operation."""
    input_data = open('./input_data')
    horizontal_position = 0
    depth = 0

    for data_line in input_data:
        command, value = data_line.split()
        value = int(value)

        if command == 'forward':
            horizontal_position += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value

    print(horizontal_position * depth)
