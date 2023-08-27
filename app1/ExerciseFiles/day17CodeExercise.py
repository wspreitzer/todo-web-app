import PySimpleGUI as sg
from converters import convert
feet_label = sg.Text("Enter length in feet")
inches_label = sg.Text("Enter length in inches")
meters_label = sg.Text(key="meters")
feet_input = sg.Input(tooltip="Length in feet", key="feet")
inches_input = sg.Input(tooltip="Length in inches", key="inches")
convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
window = sg.Window("Converter", layout=[
    [feet_label, feet_input],
    [inches_label, inches_input, convert_button],
    [meters_label],
    [exit_button]])
while True:
    event, values = window.read()
    match event:
        case "Convert":
            meters = convert(float(values["feet"]), float(values["inches"]))
            window["meters"].update(value=f"{values['feet']} feet {values['inches']} inches is {meters} meters")
        case "Exit" | sg.WIN_CLOSED:
            break
window.close()

