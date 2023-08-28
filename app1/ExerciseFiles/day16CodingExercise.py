import PySimpleGUI as sg

feet_label = sg.Text("Enter feet")
inches_label = sg.Text("Enter inches")
feet_input = sg.InputText(tooltip="Feet amount")
inches_input = sg.InputText(tooltip="Inches amount")
button = sg.Button("Convert")
window = sg.Window("Converter", layout=[
    [feet_label, feet_input],
    [inches_label, inches_input],
    [button]])
window.read()
window.close()