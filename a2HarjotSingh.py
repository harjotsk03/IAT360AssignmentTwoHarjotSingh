import matplotlib.pyplot as plt
import numpy as np
import os
from glob import glob

# Emotion dictionary
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

# Load audio files
audio_files = glob('Audio Data/*/*.wav')

if audio_files:
    print(f"Playing first audio: {audio_files[0]}")
else:
    print("No audio files found.")

def load_data():
    y = []
    count = 0
    
    # Extract emotion from file name
    for file in glob("Audio Data/Actor_*/*.wav"):
        file_name = os.path.basename(file)
        emotion = emotions_dict[file_name.split("-")[2]]
        y.append(emotion)
        count += 1
        print('\r' + f' Processed {count}/1440 audio samples', end=' ')
    
    return np.array(y)

emotions = load_data()

fig, ax = plt.subplots(figsize=(15, 8), dpi=100)

emotion_list, count = np.unique(emotions, return_counts=True)

ax.bar(x=range(len(emotion_list)), height=count, width=0.4)

ax.set_xticks(range(len(emotion_list)))
ax.set_xticklabels(emotion_list, fontsize=12)
ax.set_xlabel('Emotion', fontsize=14)
ax.set_ylabel('Number of Samples', fontsize=14)

plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)  # Adjust margins

plt.tight_layout()

plt.show()