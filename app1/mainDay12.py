def write_todos(filename, todos_arg):
    with open(filename, 'w') as fi:
        fi.writelines(todos_arg)


prompt = "Type add, show, edit, complete or exit: "
with open("files/todos.txt", "r") as file:
    todos = file.readlines()

while True:
    user_action = input(prompt).strip()
    if user_action.startswith('add'):
        todos.append(user_action[4:].capitalize() + "\n")
        write_todos("files/todos.txt", todos)
    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            item = item.strip("\n")
            output = f"{index + 1}-{item}"
            print(output)
    elif user_action.startswith('edit'):
        try:
            new_todo = input("Enter new Todo: ")
            todos[int(user_action[5:])] = new_todo.capitalize() + "\n"
            write_todos("files/todos.txt", todos)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number")
            continue
    elif  user_action.startswith('complete'):
        try:
            index = int(user_action[9:]) - 1
            todo = todos[index].strip("\n")
            todos.pop(index)
            write_todos("files/todos.txt", todos)
            message = f"Todo {todo} was removed from the list successfully"
            print(message)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue
    elif  user_action.startswith('exit'):
        break
    else:
        print("Unknown command entered.  Please try again")
print("Bye!")
