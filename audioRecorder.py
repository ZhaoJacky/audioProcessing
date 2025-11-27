import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy as sp

class audioRecorder:

    # Constructor
    def __init__(self, fs, duration):
        self.fs = fs
        self.duration = duration

    # Prints the input and output devices available.
    def printDevices(self):
        print(sd.query_devices())

    def printParams(self):
        print(f"Sample Rate: {self.fs} Hz")
        print(f"Duration: {self.duration} seconds")

    # Change the duration of the recording.
    def changeDuration(self, newDuration):
        self.duration = newDuration

    # Change the sample rate of the recording.
    def changeSampleRate(self, newSampleRate):
        self.fs = newSampleRate

    def changeDevices(self, inputDevice, outputDevice):
        sd.default.device = (inputDevice, outputDevice)

    def record(self, channels):
        print("Recording audio...")
        recordedSound = sd.rec(int(self.duration * self.fs), 
                               samplerate=self.fs, channels=channels)
        sd.wait()
        return recordedSound.flatten()
    
    def play(self, soundArray):
        print("Playing audio...")
        sd.play(soundArray, samplerate=self.fs)
        sd.wait()

    # Plots the sound wave recorded.
    def plotSound(self, soundArray):
        
        timeVector = np.linspace(0, len(soundArray) / self.fs, num=len(soundArray))
        plt.plot(timeVector, soundArray)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title('Sound Waveform')
        plt.show()

    # Saves the recorded sound to a file to the directory you run the program.
    def saveSound(self, soundArray, filename):
        sp.io.wavfile.write(filename, self.fs, soundArray)
    

    
    


