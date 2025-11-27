from audioRecorder import audioRecorder
from audioTranscriber import audioTranscriber
from audioAnalyzer import audioAnalyzer

def main():
    """
    The main function of my program.
    """

    fs = 16000 # Sample rate that works with faster whisper models.
    duration = 5.0
    
    recorder = audioRecorder(fs, duration)
    recorder.printDevices()
    recorded = recorder.record(1)
    recorder.play(recorded)

    transcriber = audioTranscriber(model_size="tiny", device="cpu")
    segments, info = transcriber.transcribe(recorded)

    # Test case: prints out the transcribed segments
    for segment in segments:
        print(f"[{segment.start:.2f} --> {segment.end:.2f}] {segment.text}")

    
if __name__ == "__main__":
    main()
