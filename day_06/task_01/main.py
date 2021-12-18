
days = 80

if __name__ == '__main__':
    input_line = open('./input_data').readline()
    lanternswarm = [int(val) for val in input_line.split(',')]

    for day in range(days):
        new_fish = []
        for index, lanternfish in enumerate(lanternswarm):
            if lanternfish == 0:
                lanternswarm[index] = 6
                new_fish.append(8)
                continue
            lanternswarm[index] = lanternfish - 1
        lanternswarm.extend(new_fish)

    print(len(lanternswarm))
