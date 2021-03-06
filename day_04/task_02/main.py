

def check_for_number(bingo_numbers, bingo_boards, boards_solved):
    for bingo_number in bingo_numbers:
        for board_index, bingo_board in enumerate(bingo_boards):
            for bingo_line in bingo_board:
                for bingo_board_number in bingo_line:
                    if int(bingo_board_number[0]) == int(bingo_number):
                        bingo_board_number[1] = True
                        if check_for_bingo(bingo_board):
                            boards_solved[board_index] = True
                            if all(board_solved for board_solved in boards_solved):
                                return board_index, int(bingo_board_number[0])


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


if __name__ == '__main__':
    input_data = open('./input_data')
    line_one = True
    first_board_line = True
    board_counter = -1
    bingo_numbers = []
    boards_solved = []
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
                boards_solved.append(False)
                bingo_boards.append([])
                first_board_line = False

            board_line = [[number, False] for number in board_line]
            bingo_boards[board_counter].append(board_line)
        else:
            board_counter += 1
            first_board_line = True
    bingo_boards.pop()

    winning_index, winning_number = check_for_number(bingo_numbers, bingo_boards, boards_solved)

    unmarked_total = 0
    for bingo_line in bingo_boards[winning_index]:
        for bingo_board_number in bingo_line:
            if not bingo_board_number[1]:
                unmarked_total += int(bingo_board_number[0])

    print(unmarked_total * winning_number)
