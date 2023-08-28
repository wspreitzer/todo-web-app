from functions import get_todos, write_todos
import time

print("It is", time.strftime("%b %d, %Y %H:%M:%S"))
prompt = "Type add, show, edit, complete or exit: "
todos = get_todos()
while True:
    user_action = input(prompt).strip()
    if user_action.startswith('add'):
        todos.append(user_action[4:].capitalize() + "\n")
        write_todos(todos)
    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            item = item.strip("\n")
            output = f"{index + 1}-{item}"
            print(output)
    elif user_action.startswith('edit'):
        try:
            new_todo = input("Enter new Todo: ")
            todos[int(user_action[5:])] = new_todo.capitalize() + "\n"
            write_todos(todos)
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
            write_todos(todos)
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
