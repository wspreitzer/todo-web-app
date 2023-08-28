import streamlit as st
import os



def get_todos():
    """ Read a text file and return the list of
    to-do items.
    """
    filepath = os.path.join(os.getcwd(), "todos.txt")
    with open(filepath, 'r') as file:
        todos = [line.strip() for line in file.readlines()]
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
