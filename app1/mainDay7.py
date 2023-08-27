prompt = "Type add, show, edit, complete or exit: "

file = open("todos.txt", "r")
todos = file.readlines()
file.close()
while True:
    user_action = input(prompt).strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo.title())
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for index, item in enumerate(todos):
                item = item.strip("\n")
                output = f"{index + 1}-{item}"
                print(output)
        case 'edit':
            number = int(input("Please enter the number of the Todo to edit (1-" + str(len(todos)) + "): "))
            new_todo = input("Enter new Todo: ")
            todos[number-1] = new_todo.capitalize()
        case 'complete':
            number = int(input("Please enter the number of the Todo to complete (1-" + str(len(todos)) + "): "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Unknown command entered.  Please try again")
print("Bye!")
