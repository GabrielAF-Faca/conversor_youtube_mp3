import PySimpleGUI as sg
from converter import YoutubeConverter


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Link do vídeo ou da playlist: '), sg.InputText(do_not_clear=False)],
            [sg.Text('Salvar em: '), sg.FolderBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Conversor YouTube - MP3', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if event == 'Ok':
        YoutubeConverter(values[0], values['Browse']+'/')



window.close()