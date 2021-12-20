
if __name__ == '__main__':
    digit_outputs = []
    with open('./input_data') as input_data:
        for input_line in input_data:
            input_parts = input_line.split('|')
            digit_outputs.append(input_parts[1].split())

    digit_counter = 0
    for digit_output in digit_outputs:
        for digit in digit_output:
            digit_len = len(digit)

            if digit_len in [2, 3, 4, 7]:
                digit_counter += 1

    print(digit_counter)
