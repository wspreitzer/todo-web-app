import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("this app is to increase your productivity")

st.checkbox("Buy groceries")
for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Add new todo...")