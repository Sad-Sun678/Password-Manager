import functions as fn
import FreeSimpleGUI as sg


label = sg.Text("Type in a Website")
input_box = sg.InputText(tooltip = "Enter Website")
add_button = sg.Button("Add")

window = sg.Window('My Password Manager', layout = [[[label], [input_box,add_button]]])
window.read()
window.close()
