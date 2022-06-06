import os
from tqdm import tqdm
from pydub import AudioSegment

m4a_files = os.listdir('wavs')
totalFiles = len(m4a_files)


for i in tqdm(range(totalFiles)):
    wav_file_name = 'wavs_out/'+m4a_files[i][0:-4] + '.wav'
    track = AudioSegment.from_file('wavs/'+m4a_files[i],  format= 'mp3')
    file_handle = track.export(wav_file_name, format='wav')
