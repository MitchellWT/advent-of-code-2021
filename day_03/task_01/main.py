
if __name__ == '__main__':
    input_data = open('./input_data')
    binary_length = len(input_data.readline()) - 1
    binary_for_not = ''
    gamma_rate = ''
    on_bit = []
    off_bit = []

    for i in range(0, binary_length):
        on_bit.append(0)
        off_bit.append(0)
        binary_for_not += '1'

    for data_line in input_data:
        bit_counter = 0
        data_line = data_line.replace('\n', '')

        for bit in data_line:
            bit = int(bit)
            if bit == 1:
                on_bit[bit_counter] += 1
            elif bit == 0:
                off_bit[bit_counter] += 1
            bit_counter += 1

    for i in range(0, binary_length):
        if on_bit[i] > off_bit[i]:
            gamma_rate += '1'
        else:
            gamma_rate += '0'

    # Convert binary string to int
    binary_for_not = int(binary_for_not, 2)
    gamma_rate = int(gamma_rate, 2)
    # Performing NOT operation on binary
    epsilon_rate = binary_for_not - gamma_rate

    print(gamma_rate * epsilon_rate)
