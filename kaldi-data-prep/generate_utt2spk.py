import pandas as pd
import os

source = 'train.txt'
destination = 'utt2spk'
destination_dir = 'data/train'

df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']

df.sort_values(['file_name'], axis=0, ascending=True, inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/utt2spk","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+df['spk_id'][i]+'\n')

f.close()



source = 'val.txt'
destination = 'utt2spk'
destination_dir = 'data/val'

df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']
df.sort_values(['file_name'], axis=0, ascending=True, inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/utt2spk","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+df['spk_id'][i]+'\n')

f.close()



source = 'test.txt'
destination = 'utt2spk'
destination_dir = 'data/test'

df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']


df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/utt2spk","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+df['spk_id'][i]+'\n')

f.close()