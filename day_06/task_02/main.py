
days = 256

if __name__ == '__main__':
    input_line = open('./input_data').readline()
    lanternfishes = [int(val) for val in input_line.split(',')]
    lanternswarm = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for lanternfish in lanternfishes:
        lanternswarm[lanternfish] += 1

    for day in range(days):
        fish_at_zero = lanternswarm[0]

        for i in range(8):
            lanternswarm[i] = lanternswarm[i + 1]

        lanternswarm[6] += fish_at_zero
        lanternswarm[8] = fish_at_zero

    total = 0
    for lanternfish in lanternswarm:
        total += lanternfish

    print(total)
