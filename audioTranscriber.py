from faster_whisper import WhisperModel

class audioTranscriber:

    # Constructor to initialize the Whisper model with specified parameters.
    def __init__(self, model_size="small", device="auto", compute_type="int8"):
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type

        self.model = WhisperModel(self.model_size, 
                                  device=self.device, 
                                  compute_type=self.compute_type)

    # Returns a segment of the transcribed words related information
    # such as language and duration.
    def transcribe(self, soundArray):
        segments, info = self.model.transcribe(soundArray)
        return segments, info
    
    def printModelParams(self):
        print(f"Model Size: {self.model_size}")
        print(f"Device: {self.device}")
        print(f"Compute Type: {self.compute_type}")

    def changeModelParams(self, model_size=None, device=None, compute_type=None):
        if model_size:
            self.model_size = model_size
        if device:
            self.device = device
        if compute_type:
            self.compute_type = compute_type

        self.model = WhisperModel(self.model_size, 
                                  device=self.device, 
                                  compute_type=self.compute_type)
