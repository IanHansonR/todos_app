import PySimpleGUI as sg

layout = [
    [sg.Text('Column 1'), sg.Text('Column 2')],
    [sg.Column([
        [sg.Button('Button 1')],
        [sg.Button('Button 2')],
    ]), sg.Column([
        [sg.Button('Button 3')],
        [sg.Button('Button 4')],
    ])],
    [sg.Button('Submit')]
]

window = sg.Window('Split Window into Columns', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Submit':
        break

window.close()