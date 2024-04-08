import os
import numpy as np
import librosa

def getDuration(file_path):
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    duration = librosa.get_duration(y=audio_data, sr=sample_rate)
    return duration

dir = os.path.dirname(os.path.realpath(__file__))
ground_truth_csv = os.path.join(dir, "FSD50K.ground_truth/eval.csv")

import pandas as pd

df = pd.read_csv(ground_truth_csv)

data=set()
df['fname'].apply(str)
for index, row in df.iterrows():
    if ('bark' in row['labels'].lower()):
        data.add(row['fname'])
print(len(data))
data_dir = os.path.join(dir, "FSD50K.eval_audio")
count = 0
for file in os.listdir(data_dir):
    if int(file.split('.')[0]) in data:
        duration = getDuration(f'{data_dir}/{file}')
        if (duration <= 2.5):
            count = count+1
            os.popen(f'cp {data_dir}/{file} {dir}/test_bark/{file}') 
print(count)