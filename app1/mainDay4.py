prompt = "Type add, show, edit or exit: "
todos = []
while True:
    user_action = input(prompt).strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            length = str(todos.__len__())
            number = int(input("Please enter the number of the Todo to edit (1-" + length + "): "))
            new_todo = input("Enter new Todo: ")
            todos[number-1] = new_todo.capitalize()
        case 'exit':
            break
        case _:
            print("Unknown command entered.  Please try again")
print("Bye!")
