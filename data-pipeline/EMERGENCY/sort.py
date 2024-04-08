import os

dir = os.path.dirname(os.path.realpath(__file__))

data_dir = os.path.join(dir, 'firetruck')
out_dir = os.path.join(dir, 'firetruck_sound')
files = os.listdir(data_dir)

for file in files:
    if 'wav' in file and 'Zone' not in file:
        filePath = os.path.join(data_dir, file)
        os.popen(f'cp {filePath} {out_dir}/{file}') 