FILEPATH = "2do.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    2-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write 2-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("Hey man")
    print(get_todos())