import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import librosa.display
import soundfile
import os

from glob import glob

import librosa
import IPython.display as ipd

emotions_dict ={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}

audio_files = glob('Audio Data/*/*.wav')

if audio_files:
    ipd.Audio(audio_files[0])
else:
    print("No audio files found.")

def load_data():
    X, y = [], []
    count = 0
    
    for file in glob("Audio Data/Actor_*/*.wav"):
        file_name = os.path.basename(file)
        emotion = emotions_dict[file_name.split("-")[2]]
        # features = get_features(file)  # Uncomment when you have feature extraction function
        # X.append(features)
        y.append(emotion)
        count += 1
        print('\r' + f' Processed {count}/1440 audio samples', end=' ')
    
    return np.array(X), np.array(y)

features, emotions = load_data()

plt.figure(figsize=(35,4))
plt.subplot(1,3,1)
emotion_list, count = np.unique(emotions, return_counts=True)
plt.bar(x=range(8), height=count)
plt.xticks(ticks=range(8), labels = [emotion for emotion in emotion_list],fontsize=10)
plt.xlabel('Emotion')
plt.tick_params(labelsize=10)
plt.ylabel('Number of Samples')
plt.show()