
if __name__ == '__main__':
    crab_subs = []
    with open('./input_data') as input_data:
        input_line = input_data.readline()
        crab_subs = [int(i) for i in input_line.split(',')]

    max_horizontal = max(crab_subs)
    min_fuel = -1

    for i in range(max_horizontal + 1):
        current_min = 0
        for crab_sub in crab_subs:
            n = abs(i - crab_sub)
            # Apply summation equation
            current_min += int((n * (n + 1)) / 2)
        if current_min < min_fuel or min_fuel == -1:
            min_fuel = current_min

    print(min_fuel)
