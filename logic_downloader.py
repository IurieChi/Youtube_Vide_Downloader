#  pip install pytube

from pytube import YouTube
import os


# link = g.value['link']

def chenge_directory(cwd_path):
    os.getcwd()
    return os.chdir(cwd_path)
    

def download_video(link,cwd_path):
    chenge_directory(cwd_path)
    videoObject = YouTube(link)
     # Short way to download higest resolution
    videoObject = videoObject.streams.get_highest_resolution()
    # videoObject = YouTube(link).streams.order_by('resolution').desc().first().download()

    try:
        videoObject.download()
    except:
        ex_error = 'Somthing went wrong, try again!'
        return ex_error
    else:
        succes = 'Download is complited successfuly'
        return succes
    
    
def download_audio(link,cwd_path):
    chenge_directory(cwd_path)
    audioObject = YouTube(link)
    audioObject = audioObject.streams.filter(only_audio = True, file_extension='mp3')
    # choose the audio feed with the bigger bitrate available
    # audioObject = YouTube(link).streams.filter(only_audio=True).order_by('abr').desc().first().download(filename_prefix="audio_")

    try:
        audioObject =  audioObject.get_audio_only()
        audioObject.download()
    except:
        ex_error = 'Somthing went wrong, try again!'
        return ex_error
    else:
        succes  = 'Audio file saved successfuly'
        return succes

    


