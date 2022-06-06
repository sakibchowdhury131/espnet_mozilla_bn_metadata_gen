import pandas as pd
import os

source = 'train.txt'
destination = 'wav.scp'
destination_dir = 'data/train'
audio_dir = '/content/espnet/egs/ljspeech/tts1/downloads/LJSpeech-1.1/wavs'

df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']

df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")



for i in range (len(df)):
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i].replace('-','').replace(df['spk_id'][i], '') +'.wav' +'\n')

f.close()





source = 'val.txt'
destination = 'wav.scp'
destination_dir = 'data/val'
audio_dir = '/content/espnet/egs/ljspeech/tts1/downloads/LJSpeech-1.1/wavs'

df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']
df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')



if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")



for i in range (len(df)):
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i].replace('-','').replace(df['spk_id'][i], '') +'.wav' +'\n')

f.close()





source = 'test.txt'
destination = 'wav.scp'
destination_dir = 'data/test'
audio_dir = '/content/espnet/egs/ljspeech/tts1/downloads/LJSpeech-1.1/wavs'

df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']

df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")



for i in range (len(df)):
    #new_file_name = df['file_name'][i].replace('-','')
    #new_file_name = new_file_name.replace(df['spk_id'][i], '')
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i].replace('-','').replace(df['spk_id'][i], '') +'.wav' +'\n')

f.close()
