
def flash(y: int, x: int, max_y: int, max_x: int, flashed: [[int, int]]) -> [[int, int]]:
    need_to_flash = []
    # Top
    if y != 0:
        octopi[y - 1][x] += 1
        if octopi[y - 1][x] > 9 and [y - 1, x] not in flashed:
            need_to_flash.append([y - 1, x])
    # Top-Right
    if y != 0 and x != max_x:
        octopi[y - 1][x + 1] += 1
        if octopi[y - 1][x + 1] > 9 and [y - 1, x + 1] not in flashed:
            need_to_flash.append([y - 1, x + 1])
    # Right
    if x != max_x:
        octopi[y][x + 1] += 1
        if octopi[y][x + 1] > 9 and [y, x + 1] not in flashed:
            need_to_flash.append([y, x + 1])
    # Bottom-Right
    if y != max_y and x != max_x:
        octopi[y + 1][x + 1] += 1
        if octopi[y + 1][x + 1] > 9 and [y + 1, x + 1] not in flashed:
            need_to_flash.append([y + 1, x + 1])
    # Bottom
    if y != max_y:
        octopi[y + 1][x] += 1
        if octopi[y + 1][x] > 9 and [y + 1, x] not in flashed:
            need_to_flash.append([y + 1, x])
    # Bottom-Left
    if y != max_y and x != 0:
        octopi[y + 1][x - 1] += 1
        if octopi[y + 1][x - 1] > 9 and [y + 1, x - 1] not in flashed:
            need_to_flash.append([y + 1, x - 1])
    # Left
    if x != 0:
        octopi[y][x - 1] += 1
        if octopi[y][x - 1] > 9 and [y, x - 1] not in flashed:
            need_to_flash.append([y, x - 1])
    # Top-Left
    if y != 0 and x != 0:
        octopi[y - 1][x - 1] += 1
        if octopi[y - 1][x - 1] > 9 and [y - 1, x - 1] not in flashed:
            need_to_flash.append([y - 1, x - 1])
    return need_to_flash


if __name__ == '__main__':
    octopi = []
    with open('./input_data') as input_data:
        for input_line in input_data:
            octopi_line = []
            for dumbo_octopuses in input_line:
                if dumbo_octopuses == '\n':
                    continue
                octopi_line.append(int(dumbo_octopuses))
            octopi.append(octopi_line)

    max_y = len(octopi) - 1
    max_x = len(octopi[0]) - 1
    step_counter = 0
    synchronised = False
    while not synchronised:
        step_counter += 1
        flashed = []
        need_to_flash = []
        for y, octopi_line in enumerate(octopi):
            for x, dumbo_octopuses in enumerate(octopi_line):
                octopi[y][x] += 1
                if octopi[y][x] > 9:
                    need_to_flash.append([y, x])

        while len(need_to_flash) != 0:
            new_need_to_flash = []
            for dumbo_octopuses in need_to_flash:
                if [dumbo_octopuses[0], dumbo_octopuses[1]] in flashed:
                    continue
                flashed.append([dumbo_octopuses[0], dumbo_octopuses[1]])
                new_need_to_flash.extend(flash(dumbo_octopuses[0], dumbo_octopuses[1], max_y, max_x, flashed))
            need_to_flash = new_need_to_flash
       
        for y, octopi_line in enumerate(octopi):
            for x, dumbo_octopuses in enumerate(octopi_line):
                if octopi[y][x] > 9:
                    octopi[y][x] = 0
        if len(flashed) == ((max_x + 1) * (max_y + 1)):
            synchronised = True
    print(step_counter)
