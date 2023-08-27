from functions import get_todos, write_todos
import PySimpleGUI as sg
import time

todos = get_todos()
enter = True
sg.theme("Black")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=todos,
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
window = sg.Window("My To-Do App",
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos.append(values["todo"] + "\n")
            write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
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
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit" | sg.WIN_CLOSED:
            break
window.close()
