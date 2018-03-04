import pyaudio
import numpy as np
from AudioRecorder.readers import MicroPhoneReader


audio_recorder = MicroPhoneReader()

file_name = input('Please enter file name (do not add file extension): ')

data_size = int(input('please enter capture time (Seconds): '))
cap_params = {'file_name': file_name + '.txt',
              'data_type': 'time_domain',
              'data_size': None,
              'cap_time': float(data_size),
              'cap_type': 'time'}
data = audio_recorder.save_data(cap_params)


print('Captured %d samples and saved to %s.txt' % (len(data), file_name))

input("Press Enter to close")