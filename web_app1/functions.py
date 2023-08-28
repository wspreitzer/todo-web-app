import streamlit as st

FILEPATH = "../files/todos.txt"


def get_todos(filename=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filename, 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(todos_arg, filename=FILEPATH):
    """ Write the to-do items list to the text file."""
    with open(filename, 'w') as fi:
        fi.writelines(todos_arg)


def add_todo():
    todos = get_todos()
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    write_todos(todos)

