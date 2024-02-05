import PySimpleGUI as sg
import logic_downloader as l

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
    new_path = value['path']
    link = value['link']

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if value['link'] != '':
        if value['path']  !='':
            if event == 'Save Video':
                window['-OUTPUT-'].update(l.download_video(link,new_path),text_color='yellow')
            
            if event == 'Save Music':
                window['-OUTPUT-'].update(l.download_audio(link,new_path),text_color='white')
        else:
            sg.popup('      Warning!     ','Please select folder',text_color='yellow',button_color = 'red')
    else:
        sg.popup(       'Warning!'       ,'Please add link',text_color='yellow',button_color = 'red')
    
window.close()