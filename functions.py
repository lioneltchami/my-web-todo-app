# now we have a lot of repetitive code and that is not good ... so we will create a custom function .. get_todos() function that reads the file
#a function that has no return object at the end always returns None. So always make sure to return at the end of fxn .. not print!
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Reads a text file and returns a list of todo items

    Args:
        filepath (str, optional): _description_. Defaults to 'todos.txt'.

    Returns:
        _type_: _description_
    """
    with open(filepath, 'r') as file_local: 
        todos_local = file_local.readlines()
    return todos_local
    
def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the todo items list into the text file.

    Args:
        todos_arg (_type_): _description_
        filepath (str, optional): _description_. Defaults to 'todos.txt'.
    """
    with open(filepath, 'w') as file: 
            file.writelines(todos_arg)

if __name__ == "__main__":
    print("It is this file we are running")
    print("So calling the function elsewehre does not call this")