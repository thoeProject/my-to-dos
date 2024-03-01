import streamlit as st
from modules.handle_file import read_file, write_file

#Read file to get existing to-dos
todos = read_file()

#Create method add-to-do
def add_to_do():
   todo = st.session_state["new_todo"] + "\n"
   todos.append(todo)
   write_file(todos)
   

st.title("My to-do app")
st.subheader("This is my to-do list")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    
st.text_input(label= "Input your to-do here", on_change= add_to_do, key = "new_todo")