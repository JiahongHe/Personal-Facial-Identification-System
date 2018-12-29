from getContent import getContent
import numpy as np
import pygame
import time
import os

API_url_setting = 'http://127.0.0.1:8000/request/getSettings'
API_url_songs = 'http://127.0.0.1:8000/request/getSongs'

def playSong(songPath):
    pygame.mixer.init()
    pygame.mixer.music.load(songPath)
    pygame.mixer.music.play()
    time.sleep(15)

def saySomething(line):
    os.system('say ' + "'" + line + "'") 

def playRandomSong(songs):
    count = len(songs.keys())
    songlist = []
    for _, path in songs.items():
        songlist.append(path)
    chosen = np.random.randint(low=0, high=count)
    song = songlist[chosen]
    if song == "None":
        playRandomSong(songs)
    else:
        playSong(song)
    return

def playVoice(name):
    line = 'welcome, {}'.format(name)
    saySomething(line)
    return


def face_detected(name, id, user_dic):
    settings = getContent(API_url_setting)
    songs = getContent(API_url_songs)
    if user_dic[id]["FavouriteSongPath"] == "NULL":
        if settings["defaultBehavior"] == "Null":
            saySomething("default behavior not specified")
        elif settings["defaultBehavior"] == "RandomSong":
            playRandomSong(songs)
        elif settings["defaultBehavior"] == "DefaultSong":
            if settings["defaultSong"] != "Null":
                playSong(songs[settings["defaultSong"]])
            else:
                saySomething("default song not specified")
        elif settings["defaultBehavior"] == "Voice":
            playVoice(name)
    else:
        playSong(user_dic[id]["FavouriteSongPath"])

    
    


    