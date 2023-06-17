import functions
import PySimpleGUI as sg

label = sg.Text("Type a Todo")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")


window = sg.Window("My Todos",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            new_todo = functions.get_format(new_todo) + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            new_todo = functions.get_format(new_todo)

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos']. update(values=todos)
        case "Complete":
            todo_completed = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(todo_completed)
            del todos[index]
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            print(todo_completed)
            print(index)
            print('hello')

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
