def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        print(*list(map(lambda j: operation(i, j), range(1, num_columns+1))), sep="\t")


print_operation_table(lambda x, y: x * y)