from audioTools.audioRecorder import audioRecorder
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import scipy as sp
import requests
import zipfile
import io

class audioAnalyzer:
    """
    Analyzes the audio data in sound file recorded at sample rate fs.
    """

    def __init__(self, soundfile):
        data, fs = sf.read(soundfile)
        self.data = data
        self.fs = fs

    def changeSoundfile(self, newsoundfile):
        data, fs = sf.read(newsoundfile)
        self.data = data
        self.fs = fs

    def changeSampleRate(self, newSampleRate):
        self.fs = newSampleRate

    # Plots the sound wave recorded in time.
    def plotSound(self):
        timeVector = np.linspace(0, len(self.data) / self.fs, num=len(self.data))
        plt.plot(timeVector, self.data)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title('Sound Waveform')
        plt.show()



    

    

    
    
    