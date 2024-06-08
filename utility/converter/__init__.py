from audio_extract import extract_audio
import pathlib
import librosa
import soundfile as sf
from config import FILEPATH


async def convert_to_audio(filename, new_filename):
    extract_audio(input_path=FILEPATH + filename, output_path=FILEPATH + new_filename)
    pathlib.Path(FILEPATH + filename).unlink()
    return new_filename


def downsample(filename):
    y, s = librosa.load(path=FILEPATH + filename,
                        sr=16000)
    sf.write(FILEPATH + filename, y, s, format="mp3")
