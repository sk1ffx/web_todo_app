FILEPATH = "test.txt"


def get_todos(filepath=FILEPATH):
    with open(FILEPATH, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    with open(FILEPATH, "w") as file:
        file.writelines(todos)