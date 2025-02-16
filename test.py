from mplsoccer import *
import streamlit
import json
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data\euros_2024_shot_map.csv")
data = data[data['type'] == "Shot"].reset_index(drop=True)
data['location'] = data['location'].apply(json.loads)


pitch = Pitch()
fig, ax = pitch.draw(figsize=(8, 4))
plt.show()