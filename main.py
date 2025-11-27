from audioRecorder import audioRecorder

def main():
    """
    The main function of my program.
    """

    fs = 44100
    duration = 5.0
    
    recorder = audioRecorder(fs, duration)
    recorder.printDevices()
    recorded = recorder.record(1)
    recorder.play(recorded)

    


if __name__ == "__main__":
    main()
