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


