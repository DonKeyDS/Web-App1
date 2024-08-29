import streamlit as st
import functions

todos = functions.get_todos()
def add_2do():
    todo = st.session_state["new_2do"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My 2Do-App")
st.subheader("This is my first Web App")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Write",
              placeholder="Add new 2do...",
              on_change=add_2do,
              key="new_2do")
