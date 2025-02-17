from mplsoccer import *
import json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from scrape import scrapeData

matchid = scrapeData()

if matchid:
    data_path = (f'data/match_{matchid}_shots.csv')
    data = pd.read_csv(data_path)


pitch = Pitch()
pitch_length = pitch.dim.length
pitch_width = pitch.dim.width
fig, ax = pitch.draw(figsize=(8, 4))


ax.text(pitch_length / 2, pitch_width + 15, 'Shot Map', ha='center', va='top', fontsize=16, color='black')
ax.scatter(data['X'] * pitch_length, data['Y'] * pitch_width, s=100, c='#ea6969', alpha=0.7)
plt.show()
