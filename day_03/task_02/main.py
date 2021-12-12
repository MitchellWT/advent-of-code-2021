
if __name__ == '__main__':
    input_data = open('./input_data')
    binary_length = len(input_data.readline()) - 1
    on_binary = []
    off_binary = []

    for bit_position in range(0, binary_length):
        for data_line in input_data:
            bit = int(data_line[bit_position])

            if bit == 1:
                on_binary.append(data_line)
            elif bit == 0:
                off_binary.append(data_line)

        if len(on_binary) >= len(off_binary):
            input_data = on_binary.copy()
        else:
            input_data = off_binary.copy()

        on_binary = []
        off_binary = []

        if len(input_data) == 1:
            break

    oxygen_generator_rating = int(input_data[0].replace('\n', ''), 2)

    input_data = open('./input_data')
    on_binary = []
    off_binary = []
            
    for bit_position in range(0, binary_length):
        for data_line in input_data:
            bit = int(data_line[bit_position])

            if bit == 1:
                on_binary.append(data_line)
            elif bit == 0:
                off_binary.append(data_line)

        if len(on_binary) < len(off_binary):
            input_data = on_binary.copy()
        else:
            input_data = off_binary.copy()

        on_binary = []
        off_binary = []

        if len(input_data) == 1:
            break

    co2_scrubber_rating = int(input_data[0].replace('\n', ''), 2)

    print(oxygen_generator_rating * co2_scrubber_rating)
