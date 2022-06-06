import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tqdm import tqdm

source = 'meta380okSolved.txt'


df = pd.read_csv(source, delimiter='\t', header=None)
df.columns = ['file_name', 'spk_id', 'transcription', 'duration']
df = shuffle(df)


for i in tqdm(range(len(df))):
    df['file_name'][i] = df['spk_id'][i]+'-'+df['file_name'][i]

train, middle = train_test_split(df, test_size=0.1)
val, test = train_test_split(middle, test_size=0.5)
print(train)
print(val)
print(test)



train.to_csv('train.txt', sep = '\t', index = False, header = False)
val.to_csv('val.txt', sep = '\t', index = False, header = False)
test.to_csv('test.txt', sep = '\t', index = False, header = False)