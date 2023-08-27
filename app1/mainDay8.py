prompt = "Type add, show, edit, complete or exit: "
with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    user_action = input(prompt).strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo.capitalize())
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            for index, item in enumerate(todos):
                item = item.strip("\n")
                output = f"{index + 1}-{item}"
                print(output)
        case 'edit':
            number = int(input("Please enter the number of the Todo to edit (1-" + str(len(todos)) + "): "))
            new_todo = input("Enter new Todo: ")
            todos[number-1] = new_todo.capitalize() + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Please enter the number of the Todo to complete (1-" + str(len(todos)) + "): "))
            index = number - 1
            todo = todos[index].strip("\n")
            todos.pop(index)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo {todo} was removed from the list successfully"
            print(message)
        case 'exit':
            break
        case _:
            print("Unknown command entered.  Please try again")
print("Bye!")
