import pyaudio
import time
from time import gmtime, strftime
import numpy as np
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 14100
CHUNK = 1024
 


class MicroPhoneReader(object):
    _data_rate = 0 
    _audio_device = None
    _audio_stream = None
    
    def __init__(self):
        print("got in init")
        # setup audio recording
        self._audio_device = pyaudio.PyAudio()

    def calibrate(self):
        self._audio_device = pyaudio.PyAudio()
        self._audio_stream = self._audio_device.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        start = time.time()
        
        raw_data = self._audio_stream.read(CHUNK)
        stop = time.time()
        self._data_rate = float(CHUNK / (stop - start))
        
        # stop Recording
        self._audio_stream.stop_stream()
        self._audio_stream .close()

    
    def __del__(self):
        self._audio_device.terminate()

    def read_data(self, data_size):
        self._audio_stream = self._audio_device.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=data_size)
        raw_data = self._audio_stream.read(data_size)
        data_samples = np.fromstring(raw_data, dtype=np.int16)
        self._audio_stream.stop_stream()
        self._audio_stream .close()

        return data_samples

    def save_data(self, params):

        self._audio_stream = self._audio_device.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=params['data_size'])
        cap_time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        raw_data = self._audio_stream.read(params['data_size'])
        data_samples = np.fromstring(raw_data, dtype=np.int16)
        self._audio_stream.stop_stream()
        self._audio_stream .close()

        save_file = open(params['file_name'], 'w')

        save_file.write('data_type, capture_time, sample_size \n')
        save_file.write(str(params['data_type'] + ',' + str(cap_time) + ',' + str(len(data_samples)) + '\n'))

        for d in data_samples:
            save_file.write(str(d) + '\n')

        return data_samples

