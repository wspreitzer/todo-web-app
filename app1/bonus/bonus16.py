import PySimpleGUI as sg
import zipfile as zf

file_label = sg.Text("Select files to compress")
dest_label = sg.Text("Select destination folder")
file_input = sg.Input(tooltip="Files you want to compress")
dest_input = sg.Input(tooltip="Path to destination folder")
choose_button1 = sg.FilesBrowse("Choose")
choose_button2 = sg.FolderBrowse("Choose")
compress_button = sg.Button("Compress")
window = sg.Window("File Zipper", layout=[
    [file_label, file_input,choose_button1],
    [dest_label, dest_input, choose_button2],
    [compress_button]])
window.read()
window.close()