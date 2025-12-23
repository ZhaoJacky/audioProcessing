from audioRecorder import audioRecorder
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy as sp
import requests
import zipfile
import io


class audioAnalyzer:
    """
    Analyzes the audio data in soundArray recorded at sample rate fs.
    """

    def __init__(self, soundArray, fs):
        self.soundArray = soundArray
        self.fs = fs

    def changeSoundArray(self, newSoundArray):
        self.soundArray = newSoundArray

    def changeSampleRate(self, newSampleRate):
        self.fs = newSampleRate

    # Plots the sound wave recorded in time.
    def plotSound(self, soundArray):
        timeVector = np.linspace(0, len(soundArray) / self.fs, num=len(soundArray))
        plt.plot(timeVector, soundArray)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title('Sound Waveform')
        plt.show()

    

    
    
    