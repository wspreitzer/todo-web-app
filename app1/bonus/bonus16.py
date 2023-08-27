import PySimpleGUI as sg
import zipfile as zf
from zip_creator import make_archive

file_label = sg.Text("Select files to compress")
dest_label = sg.Text("Select destination folder")
file_input = sg.Input(tooltip="Files you want to compress")
dest_input = sg.Input(tooltip="Path to destination folder")
choose_button1 = sg.FilesBrowse("Choose", key="files")
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")
window = sg.Window("File Zipper", layout=[
    [file_label, file_input,choose_button1],
    [dest_label, dest_input, choose_button2],
    [compress_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    match event:
        case "Compress":
            make_archive(filepaths, folder)
            window["output"].update(value="Files compressed successfully")
        case sg.WIN_CLOSED:
            break
window.close()