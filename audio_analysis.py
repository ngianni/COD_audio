# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:34:54 2021

@author: 20340495072
"""

# Importo librerias
import numpy as np
import pandas as pd
import os

from pydub import AudioSegment
import speech_recognition as sr


# --- SET WORKING DIRECTORY -------------------------------------------------------------

# seteo directorio de trabajo
# os.chdir(os.path.dirname(os.path.abspath('__file__')))

os.chdir("C:/Users/20340495072/Desktop/GCBA/COD - Ciudad On Demand/COD_clasificador")

audiofiles = 'C:/Users/20340495072/Desktop/GCBA/COD - Ciudad On Demand/COD_audio/audiofiles/'

# AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
# AudioSegment.ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
# AudioSegment.ffprobe ="C:/ffmpeg/bin/ffprobe.exe"


# --- LOAD DATA -------------------------------------------------------------------------

# transform ogg en wav
def ogg2wav ( file ):
        
        sound = AudioSegment.from_ogg( file )
        
        outfile = os.path.splitext(file)[0] + '.wav'
        
        sound.export( outfile , format="wav")
        
        return os.path.basename(outfile)

def speech2text ( file ):
    
    with sr.AudioFile( file ) as source:
        
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language="es-ES")
        
        print('\n----------------------------------------------------')
        print(os.path.basename(filename))
        print(text)



# initialize the recognizer
r = sr.Recognizer()

# transform all files in directory to wav
for filename in os.listdir( audiofiles ):
    
    if filename.endswith( '.ogg' ): 
        filename = ogg2wav( audiofiles + filename )

    speech2text( audiofiles + filename )
