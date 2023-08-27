from functions import get_todos, write_todos
import PySimpleGUI as sg

todos = get_todos()
enter = True
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=todos,
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button],
                       [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos.append(values["todo"] + "\n")
            write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            if new_todo.endswith("\n"):
                new_todo = new_todo
            else:
                new_todo = new_todo + "\n"
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit" | sg.WIN_CLOSED:
            break
window.close()
