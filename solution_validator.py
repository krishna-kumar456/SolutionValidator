# -*- coding: utf-8 -*-
"""Solution Validator

A program to validate a given solution of the puzzle.
Consists of data stuctures used to represent the board,
the constraints and the solution, as well as the
algorithm to validate it.

To make this a runnable program, we have a 4x4 board
with constraints, and valid/invalid solutions to validate.
The constraints are modeled as initial values in
the Board data structure.

"""

import json

class Board:
    """
    A class used to represent the Board

    Attributes
    ----------
    board_size : int
        to describe the size of the board
    constraint_keys : list
        stores a set of board locations whose
        value need to be greater than corresponding value at
        the same index within constraint_values.
    constraint_values : list
        stores a set of board locations whose
        value need to be smaller than corresponding value at
        the same index within constraint_keys.

    """
    def __init__(self):
        self.board_size = 4
        self.constraints_keys = [[0,0], [1,2]]
        self.constraints_values = [[0,1], [2,2]]

def constraint_checks(board, solution):
    """Applies constraint checks on the Board against the given
    solution.

    Parameters
    ----------
    board : Board
        instance of the Board class.
    solution : list(list)
        solution to validate.

    Returns
    -------
    bool
        True or False based on if constaint checks pass or fail.
    """
    for row_list in solution:
        for column_value in row_list:
            if [row_list, column_value] in board.constraints_keys:

                mapping_ind = board.constraints_keys.index([row_list, column_value])
                key_value = board.constraints_values[mapping_ind]

                if solution[row_list, column_value] > solution[key_value[0]][key_value[1]]:
                    continue
                else:
                    return False
            else:
                continue
    return True

def validate_solution(board, solution):
    """Validate the solution for the puzzle.

    Parameters
    ----------
    board : Board
        instance of the Board class.
    solution : list(list)
        solution to validate.

    Returns
    -------
    bool
        True or False based on if the solution is valid or not.
    """
    result = True

    if constraint_checks(board, solution):
        for row_list in solution:
            if sorted(list(set(row_list))) != sorted(row_list):
                result = False

        columns_list = []
        for column_index in range(len(solution)):
            for row_list in solution:
                columns_list += [row_list[column_index]]

            if sorted(list(set(columns_list))) != sorted(columns_list):
                result = False
            columns_list = []
    else:
        result = False

    return result


def run_validator():
    """Helper method to run the validation scenario.

    """
    solution_array = None
    with open('solution.json') as f:
        solution_array = json.loads(f.read())

    board = Board()
    result = validate_solution(board, solution_array["solution"])
    print(result)


if __name__ == '__main__':
    run_validator()





