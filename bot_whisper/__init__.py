from faster_whisper import WhisperModel
from config import MODEL_SIZE, DEVICE


class Whisper(WhisperModel):
    def __init__(self):
        super().__init__(MODEL_SIZE, device=DEVICE)

    def create_text(self, filepath):
        segments, info = self.transcribe(audio=filepath,
                                         beam_size=5,
                                         condition_on_previous_text=False)
        result = ''
        for segment in segments:
            result += segment.text
        return result.strip()
