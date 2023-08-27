from functions import get_todos, write_todos
import PySimpleGUI as sg
import time

todos = get_todos()
enter = True
sg.theme("Black":"odo = new_todo + "\n"
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
