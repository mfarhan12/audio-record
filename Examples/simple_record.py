import pyaudio
import numpy as np
from AudioRecorder.readers import MicroPhoneReader


audio_recorder = MicroPhoneReader()

audio_recorder.calibrate()

data = audio_recorder.read_data(1024)

print(len(data))