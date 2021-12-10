
if __name__ == '__main__':
    input_data = open('./input_data')
    line_counter = 0
    increased_counter = 0
    line_list = [0, 0, 0, 0]

    for input_line in input_data:
        line_list[line_counter] = int(input_line)

        if line_list[3] != 0:
            prev_sum = line_list[0] + line_list[1] + line_list[2]
            curr_sum = line_list[1] + line_list[2] + line_list[3]

            if curr_sum > prev_sum:
                increased_counter += 1
            
            line_list[0] = line_list[1]
            line_list[1] = line_list[2]
            line_list[2] = line_list[3]
        else:
            line_counter += 1

    print(increased_counter)
