import os
import random

dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(dir, 'Glass_Break')
output_dir = os.path.join(dir, 'Clean_Glass')
files = os.listdir(data_dir)

selected = []
for file in files:
    name = file.split('.')[0]
    quality = name.split('_')[-1]
    if quality == '0':
        selected.append(file)

selected = random.sample(selected, 70)
for file in selected:
    os.popen(f'cp {data_dir}/{file} {output_dir}/{file}') 
