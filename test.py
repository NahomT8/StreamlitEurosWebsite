from mplsoccer import *
import json
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/match_26797_shots.csv")

pitch = Pitch()
fig, ax = pitch.draw(figsize=(8, 4))

ax.text(pitch.dim.length / 2, pitch.dim.width + 0.1, 'Liverpool shots against Manchester United', ha='center', va='top', fontsize=16, color='black')
ax.scatter(data['X'] * pitch.dim.length, data['Y'] * pitch.dim.width, s=100, c='#ea6969', alpha=0.7)
plt.show()
