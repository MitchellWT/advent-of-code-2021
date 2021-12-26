
import re
from termcolor import colored


def read_data(input_file: str) -> ([[int, int]], {str: int}):
    points = []
    folds = []
    with open(input_file) as input_file:
        for input_line in input_file:
            if input_line == '\n':
                continue
            if 'fold along' in input_line:
                current_fold = re.findall(r'([yx])=(\d*)', input_line)
                folds.append((current_fold[0][0], int(current_fold[0][1])))
                continue
            current_points = input_line.split(',')
            current_points[1] = current_points[1].replace('\n', '')
            points.append([int(current_points[0]), int(current_points[1])])
    return points, folds


def fold_x(points: [int, int], fold_line: int) -> [int, int]:
    """Folds the points on the fold_line to the right"""
    remove_points = []
    new_points = []
    for point in points:
        if point[0] > fold_line:
            distance_to_fold = point[0] - fold_line
            new_point = [point[0] - (distance_to_fold * 2), point[1]]
            new_points.append(new_point)
            remove_points.append(point)
    points = [point for point in points if point not in remove_points]
    points += [point for point in new_points if point not in points]

    return points


def fold_y(points: [int, int], fold_line: int) -> [int, int]:
    """Folds the points on the fold_line upwards"""
    remove_points = []
    new_points = []
    for point in points:
        if point[1] > fold_line:
            distance_to_fold = point[1] - fold_line
            new_point = [point[0], point[1] - (distance_to_fold * 2)]
            new_points.append(new_point)
            remove_points.append(point)
    points = [point for point in points if point not in remove_points]
    points += [point for point in new_points if point not in points]

    return points


def print_paper(points: [int, int]):
    """Prints the transparent paper (with its points) to the screen"""
    max_x = 0
    max_y = 0
    transparent_paper = []
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    for y in range(max_y + 1):
        paper_line = ['.' for x in range(max_x + 1)]
        transparent_paper.append(paper_line)
    for point in points:
        transparent_paper[point[1]][point[0]] = '#'
    for paper_line in transparent_paper:
        for paper_point in paper_line:
            if paper_point == '#':
                print(colored('\u2588', 'white'), end='')
                continue
            print(' ', end='')
        print()


if __name__ == '__main__':
    points, folds = read_data('./input_data')

    for fold in folds:
        if fold[0] == 'y':
            points = fold_y(points, fold[1])
        if fold[0] == 'x':
            points = fold_x(points, fold[1])

    print_paper(points)
