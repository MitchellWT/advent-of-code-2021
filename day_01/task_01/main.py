
if __name__ == '__main__':
    """Reads in a set of integer from a files and calculates how many
    are increased from the previous value read in."""
    input_data = open('./input_data')
    prev_line = None
    increased_counter = 0

    for data_line in input_data:
        if prev_line is not None and int(data_line) > int(prev_line):
            increased_counter += 1
        prev_line = data_line

    print(increased_counter)
