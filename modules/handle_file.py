FILEPATH = "data/data-test.txt"

def read_file(f_path = FILEPATH):
    with open(f_path, 'r') as file:
        return file.readlines()

def write_file(text, f_path = FILEPATH):
    with open(f_path, 'w') as file:
            file.writelines(text)

def loop_to_dos(todos):
    print("This is your list: ")
    for index, todo in enumerate(todos):
        todo = todo.strip()
        if todo == "":
            continue
        print(f"{index + 1}. {todo}")
