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
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        ex_error = 'Somthing went wrong, try again!'
        return ex_error
    else:
        succes = 'Download is complited successfuly'
        return succes
    
def download_audio(link):
    chenge_dir()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio = True, file_extension='mp4')

    try:
        youtubeObject =  youtubeObject.get_audio_only()
        youtubeObject.download()

    except:
        ex_error = 'Somthing went wrong, try again!'
        return ex_error
    else:
        succes  = 'Audio file saved successfuly'
        return succes

    


# GUI
form_rows = [ 
    [sg.Text('YouTube Video Downloader')],
    [sg.Text('Video URL:', size=(10,1)),sg.Input(key='link',do_not_clear=False)],
    [sg.Text('Select Folder to save', size=(10,1)),sg.Input(key='path'),sg.FolderBrowse()],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Save Video'), sg.Cancel(), sg.Button('Exit')],
    [sg.Button('Save Music')]
]

window = sg.Window('Youtube Downloader', form_rows)
while True:
    event , value = window.read()
    if event == 'Save Video':
        link = value['link']
        window['-OUTPUT-'].update(download(link),text_color='yellow')
    
    if event == 'Save Music':
        link = value['link']
        window['-OUTPUT-'].update(download_audio(link),text_color='white')

    if event == 'Cancel':
        window['-OUTPUT-'].update("")
    

        
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()