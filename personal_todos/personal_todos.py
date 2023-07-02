import PySimpleGUI as sg
import priorities_functions as pf
import time

sg.theme('DarkGreen5')

clock = sg.Text("", key="clock")
todo_input_label = sg.Text("Enter todo:")
todo_input = sg.InputText(key='input')
exit_button = sg.Button("Exit")

# Priorities:
p_add_button = sg.Button("Add Priority")
p_edit_button = sg.Button("Edit Priority")
p_complete_button = sg.Button("Complete Priority")
p_box = sg.Listbox(values=pf.get_items("priorities.txt"),
                   enable_events=True, key="priorities", size=[45, 10])

# Minorities:
m_add_button = sg.Button("Add Minority")
m_edit_button = sg.Button("Edit Minority")
m_complete_button = sg.Button("Complete Minority")
m_box = sg.Listbox(values=pf.get_items("minorities.txt"),
                   enable_events=True, key="minorities", size=[45, 10])

window = sg.Window("My Todos",
                   layout=[[clock],
                           [todo_input_label, todo_input],
                           [p_add_button, p_edit_button, m_add_button, m_edit_button],
                           [p_box, m_box],
                           [p_complete_button, m_complete_button],
                           [exit_button]
                           ],
                   font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%x, %I:%M %p"))
    match event:
        case "Add Priority":
            todos = pf.get_items("priorities.txt")
            new_todo = values['input']
            if new_todo == '':
                sg.popup("Enter a todo first.", font=('Helvetica', 15))
                continue
            new_todo = pf.get_format(new_todo) + '\n'
            todos.append(new_todo)
            pf.write_items(todos, "priorities.txt")
            window['priorities'].update(values=todos)
            window['input'].update(value='')
        case "Edit Priority":
            try:
                todos = pf.get_items("priorities.txt")
                new_todo = values['input']
                new_todo = pf.get_format(new_todo)
                todo_to_edit = values['priorities'][0]

                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                pf.write_items(todos, "priorities.txt")
                window['priorities'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first.", font=("helvetica", 15))
        case "Add Minority":
            todos = pf.get_items("minorities.txt")
            new_todo = values['input']
            if new_todo == '':
                sg.popup("Enter a todo first.", font=("Helvetica", 15))
                continue
            new_todo = pf.get_format(new_todo) + '\n'
            todos.append(new_todo)
            pf.write_items(todos, "minorities.txt")
            window['minorities'].update(values=todos)
            window['input'].update(value='')
        case "Edit Minority":
            try:
                todos = pf.get_items("minorities.txt")
                new_todo = values['input']
                new_todo = pf.get_format(new_todo)
                todo_to_edit = values['minorities'][0]

                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                pf.write_items(todos, "minorities.txt")
                window['minorities'].update(values=todos)
            except IndexError:
                sg.popup("Select a todo first.", font=("Helvetica", 15))
        case "Complete Priority":
            todo_completed = values['priorities'][0]
            todos = pf.get_items("priorities.txt")
            index = todos.index(todo_completed)
            del todos[index]
            pf.write_items(todos, "priorities.txt")
            window['priorities'].update(values=todos)
            window['input'].update('')
        case "Complete Minority":
            todo_completed = values['minorities'][0]
            todos = pf.get_items("minorities.txt")
            index = todos.index(todo_completed)
            del todos[index]
            pf.write_items(todos, "minorities.txt")
            window['minorities'].update(values=todos)
            window['input'].update('')
        case "priorities":
            window['input'].update(values['priorities'][0])
        case "minorities":
            window['input'].update(values['minorities'][0])
        case "Exit":
            break

window.close()
