from mplsoccer import *
import json
import pandas as pd
import matplotlib.pyplot as plt
from scrape import scrapeData

matchid = scrapeData()

if matchid:
    data_path = (f'data/match_{matchid}_shots.csv')
    data = pd.read_csv(data_path)


pitch = Pitch()
fig, ax = pitch.draw(figsize=(8, 4))

ax.text(pitch.dim.length / 2, pitch.dim.width + 0.1, 'Shot Map', ha='center', va='top', fontsize=16, color='black')
ax.scatter(data['X'] * pitch.dim.length, data['Y'] * pitch.dim.width, s=100, c='#ea6969', alpha=0.7)
plt.show()
