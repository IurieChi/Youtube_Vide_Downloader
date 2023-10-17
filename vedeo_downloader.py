#  pip install pytube

from pytube import YouTube
import PySimpleGUI as sg
import os


def chenge_dir():
    cwd = os.getcwd()
    cwd = value['path']
    return os.chdir(cwd)
    # print(os.getcwd())

# logic
def download(link):
    chenge_dir()
    youtubeOgject = YouTube(link)
    youtubeOgject = youtubeOgject.streams.get_highest_resolution()
    try:
        youtubeOgject.download()
    except:
        ex_error = 'An error acured '
        return ex_error
    succes = 'Download is complited successfuly'
    return succes


# GUI
form_rows = [ 
    [sg.Text('YouTube Video Downloader')],
    [sg.Text('Video URL:', size=(10,1)),sg.Input(key='link',do_not_clear=False)],
    [sg.Text('Select Folder to save', size=(10,1)),sg.Input(key='path'),sg.FolderBrowse()],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Save'), sg.Cancel(), sg.Button('Exit')]
]

window = sg.Window('Youtube Downloader', form_rows)
while True:
    event , value = window.read()
    if event == 'Save':
        link = value['link']
        window['-OUTPUT-'].update(download(link),text_color='yellow')
    if event == 'Cancel':
        window['-OUTPUT-'].update("")
        
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()