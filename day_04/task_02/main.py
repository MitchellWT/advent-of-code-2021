

def check_for_number(bingo_numbers, bingo_boards):
    for bingo_number in bingo_numbers:
        for board_index, bingo_board in enumerate(bingo_boards):
            for bingo_line in bingo_board:
                for bingo_board_number in bingo_line:
                    if int(bingo_board_number[0]) == int(bingo_number):
                        bingo_board_number[1] = True
                        if check_for_bingo(bingo_board):
                            bingo_boards.pop(board_index)
                            print(bingo_board_number[0])
                            if len(bingo_boards) == 1:
                                return board_index, int(bingo_board_number[0])

                            for bingo_board in bingo_boards:
                                for bingo_line in bingo_board:
                                    print(bingo_line)
                                print()

def check_for_bingo(bingo_board):
    column_bingo = [True] * len(bingo_board)

    for bingo_line in bingo_board:
        row_bingo = True
        column_counter = 0
        for bingo_board_number in bingo_line:
            if not bingo_board_number[1]:
                column_bingo[column_counter] = False
                row_bingo = False
            column_counter += 1

        if row_bingo:
            return row_bingo

    for column_bool in column_bingo:
        if column_bool:
            return column_bingo

    return False


if __name__ == '__main__':
    input_data = open('../test')
    line_one = True
    first_board_line = True
    board_counter = -1
    bingo_numbers = []
    bingo_boards = [[]]

    # Collect data from file
    for input_line in input_data:
        if line_one:
            bingo_numbers = input_line.split(',')
            line_one = False
            continue

        board_line = input_line.split()
        if len(board_line) > 0:
            if first_board_line:
                bingo_boards.append([])
                first_board_line = False

            board_line = [[number, False] for number in board_line]
            bingo_boards[board_counter].append(board_line)
        else:
            board_counter += 1
            first_board_line = True
    bingo_boards.pop()

    winning_index, winning_number = check_for_number(bingo_numbers, bingo_boards)

    unmarked_total = 0
    for bingo_line in bingo_boards[winning_index]:
        for bingo_board_number in bingo_line:
            if not bingo_board_number[1]:
                unmarked_total += int(bingo_board_number[0])

    print(winning_index)
    for bingo_board in bingo_boards:
        for bingo_line in bingo_board:
            print(bingo_line)
        print()
    print(unmarked_total)
    print(winning_number)
    print(unmarked_total * winning_number)
