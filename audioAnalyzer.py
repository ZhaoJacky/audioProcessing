from audioRecorder import audioRecorder
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy as sp


def audioAnalyzer(soundArray, fs):
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

    
    
    