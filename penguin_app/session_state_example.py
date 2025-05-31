import streamlit as st

st.title('My To-Do List Creator')

if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = ['Buy groceries', 'Walk the dog', 'Read a book']
# st.write('My current To-Do List is:', my_todo_list)
new_todo = st.text_input('What do you need to do?')
if st.button('Add the new To-Do item'):
    st.write('Adding a new item to the list')
    st.session_state.my_todo_list.append(new_todo)
    # my_todo_list.append(new_todo)

st.write('My updated To-Do List is:', st.session_state.my_todo_list)