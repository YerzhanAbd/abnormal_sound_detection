import os
import librosa
import soundfile

dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(dir, 'Glass_Break')
out_dir = os.path.join(dir, 'Sliced_Glass')

FRAME_LENGTH = 2048
HOP_LENGTH = 512
NUM_SECONDS_OF_SLICE = 2.5

files = os.listdir(data_dir)
for file in files:
    filepath = os.path.join(data_dir,file)
    sound, sr = librosa.load(filepath, sr=None)

    clip_rms = librosa.feature.rms(y=sound,
                                frame_length=FRAME_LENGTH,
                                hop_length=HOP_LENGTH)
    clip_rms = clip_rms.squeeze()
    peak_rms_index = clip_rms.argmax()
    peak_index = peak_rms_index * HOP_LENGTH + int(FRAME_LENGTH/2)

    half_slice_width = int(NUM_SECONDS_OF_SLICE * sr / 2)
    left_index = max(0, peak_index - half_slice_width)
    right_index = peak_index + half_slice_width
    sound_slice = sound[left_index:right_index]

    soundfile.write(os.path.join(out_dir, file), sound_slice, sr)
