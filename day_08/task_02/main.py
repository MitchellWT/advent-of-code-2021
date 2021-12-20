
if __name__ == '__main__':
    digit_inputs = []
    digit_outputs = []
    # with open('./input_data') as input_data:
    with open('./input_data') as input_data:
        for input_line in input_data:
            input_parts = input_line.split('|')
            # Sorts strings in the input section of the input_data
            append_list = []
            for input_part_0 in input_parts[0].split():
                input_list = list(input_part_0)
                input_list.sort()
                append_list.append(''.join(input_list))
            digit_inputs.append(append_list)
            # Sorts strings in the output section of the input_data
            append_list = []
            for input_part_1 in input_parts[1].split():
                input_list = list(input_part_1)
                input_list.sort()
                append_list.append(''.join(input_list))
            digit_outputs.append(append_list)

    output_value = 0
    for i in range(len(digit_inputs)):
        digit_strings = [''] * 10
        digit_strings[1] = [one for one in digit_inputs[i] if len(one) == 2][0]
        digit_inputs[i].remove(digit_strings[1])
        digit_strings[4] = [four for four in digit_inputs[i] if len(four) == 4][0]
        digit_inputs[i].remove(digit_strings[4])
        digit_strings[7] = [seven for seven in digit_inputs[i] if len(seven) == 3][0]
        digit_inputs[i].remove(digit_strings[7])
        digit_strings[8] = [eight for eight in digit_inputs[i] if len(eight) == 7][0]
        digit_inputs[i].remove(digit_strings[8])

        theta_segment = digit_strings[4]
        for one_segment in digit_strings[1]:
            theta_segment = theta_segment.replace(one_segment, '')

        for digit_input in digit_inputs[i]:
            if theta_segment[0] in digit_input and theta_segment[1] in digit_input and len(digit_input) == 5:
                digit_strings[5] = digit_input
                break
        digit_inputs[i].remove(digit_strings[5])

        five_set = set(digit_strings[5])

        for digit_input in digit_inputs[i]:
            if len(five_set.difference(set(digit_input))) == 2 and len(digit_input) == 5:
                digit_strings[2] = digit_input
            if len(five_set.difference(set(digit_input))) == 1 and len(digit_input) == 5:
                digit_strings[3] = digit_input
            if len(five_set.difference(set(digit_input))) == 1 and len(digit_input) == 6:
                digit_strings[0] = digit_input
        digit_inputs[i].remove(digit_strings[2])
        digit_inputs[i].remove(digit_strings[3])
        digit_inputs[i].remove(digit_strings[0])

        for digit_input in digit_inputs[i]:
            if digit_strings[7][0] in digit_input and digit_strings[7][1] in digit_input and digit_strings[7][2] in digit_input:
                digit_strings[9] = digit_input
                break
        digit_inputs[i].remove(digit_strings[9])
        digit_strings[6] = digit_inputs[i][0]

        output_string = ''
        for digit_output in digit_outputs[i]:
            for index, digit_string in enumerate(digit_strings):
                if digit_output == digit_string:
                    output_string += str(index)

        output_value += int(output_string)
    print(output_value)
