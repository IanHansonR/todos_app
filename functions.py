FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read text file and return list of items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write items to the text file for storage."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print('hello')
    print(get_todos())
