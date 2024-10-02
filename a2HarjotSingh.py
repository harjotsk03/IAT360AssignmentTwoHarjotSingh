import matplotlib.pyplot as plt
import numpy as np
import os
from glob import glob

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
    print(f"Playing first audio: {audio_files[0]}")
else:
    print("No audio files found.")

def load_data():
    y = []
    gender_data = []
    count = 0
    
    for file in glob("Audio Data/Actor_*/*.wav"):
        file_name = os.path.basename(file)
        emotion = emotions_dict[file_name.split("-")[2]]
        actor_id = int(file_name.split("-")[-1].split(".")[0])
        
        gender = 'male' if actor_id % 2 != 0 else 'female'
        gender_data.append(gender)
        
        y.append(emotion)
        count += 1
        print('\r' + f'Processed {count}/1440 audio samples', end=' ')
    
    return np.array(y), np.array(gender_data)

emotions, genders = load_data()

fig1, ax1 = plt.subplots(figsize=(10, 6), dpi=100)

emotion_list, emotion_count = np.unique(emotions, return_counts=True)

ax1.bar(x=range(len(emotion_list)), height=emotion_count, width=0.4, color='skyblue')
ax1.set_xticks(range(len(emotion_list)))
ax1.set_xticklabels(emotion_list, fontsize=12)
ax1.set_xlabel('Emotion', fontsize=14)
ax1.set_ylabel('Number of Samples', fontsize=14)
ax1.set_title('Distribution of Emotional Categories', fontsize=16)

plt.tight_layout()
plt.show()

fig2, ax2 = plt.subplots(figsize=(8, 5), dpi=100)

unique_genders, gender_counts = np.unique(genders, return_counts=True)

ax2.bar(x=unique_genders, height=gender_counts, width=0.4, color=['blue', 'pink'])
ax2.set_xlabel('Gender', fontsize=14)
ax2.set_ylabel('Number of Samples', fontsize=14)
ax2.set_title('Gender Balance of Audio Samples', fontsize=16)

plt.tight_layout()
plt.show()
