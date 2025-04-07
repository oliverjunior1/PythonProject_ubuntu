import PySimpleGUI as sg

sg.theme('SandyBeach')

layout = [
    [sg.Text('Please enter your name, age, Phone')],
    [sg.Text('Name', size=(15,1)),sg.InputText()],
    [sg.Text('Age', size=(15,1)), sg.InputText()],
    [sg.Text('Phone', size=(15,1)),sg.InputText()],
    [sg.Sudmit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
