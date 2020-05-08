class Board:
    def __init__(self):
        self.board_size = 4
        self.constraints_keys = [[0,0], [1,2]]
        self.constraints_values = [[0,1], [2,2]]
        self.board = [[0 for col in range(self.board_size)] for row in range(self.board_size)]


def constraint_checks(board, solution):
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
    result = True

    if constraint_checks(board, solution):
        for row_list in solution:
            if  (list(set(row_list))) != sorted(row_list):
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
    solution = [
    [2,1,4,3],
    [1,4,3,2],
    [3,2,1,4],
    [4,3,2,1]

    ]
    board = Board()
    result = validate_solution(board, solution)
    print(result)


if __name__ == '__main__':
    run_validator()





