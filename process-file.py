from modules.handle_file import read_file, write_file,update_file

def loop_to_dos(todos):
    print("This is your list: ")
    for index, todo in enumerate(todos):
        todo = todo.strip()
        if todo == "":
            continue
        print(f"{index + 1}. {todo}")

while True:
    user_input = input("\nDo you want to add, show, edit, delete or exit? (add/show/edit/delete/exit) \n")
    if "add" in user_input:
        todo = input("\nEnter a to-do: ") + "\n"
        todos = read_file()
        todos.append(todo)
        write_file(todos)
    elif user_input in ["show", "display"]:
        content = read_file()
        loop_to_dos(content)
    elif "edit" in user_input:
        old_index = int(input("\nEnter the number you want to edit: "))
        new_value = input("\nEnter the new value: ")
        todos = read_file()
        todos[old_index - 1] = new_value + "\n"
        write_file(todos)
    elif "delete" in user_input:
        remove_index = int(input("\nEnter the number of item you want to delete: \n"))
        update_file(remove_index, "")
        content = read_file()
        loop_to_dos(content)
    elif "exit" in user_input:
        break
