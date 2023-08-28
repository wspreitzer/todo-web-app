import PySimpleGUI as sg
from zip_functions import extract_archive
sg.theme("Black")
file_label = sg.Text("Select archive to extract")
dest_label = sg.Text("Select destination folder")
file_input = sg.Input(tooltip="Archive you want to extract")
dest_input = sg.Input(tooltip="Path to destination folder")
archive_button = sg.FilesBrowse("Choose", key="archive")
dest_button = sg.FolderBrowse("Choose", key="folder")
extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")
window = sg.Window("Archive Extractor", layout=[
    [file_label, file_input,archive_button],
    [dest_label, dest_input, dest_button],
    [extract_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    folder = values["folder"]
    match event:
        case "Extract":
            extract_archive(archivepath, folder)
            window["output"].update(value="Archive extracted successfully")
        case sg.WIN_CLOSED:
            break
window.close()