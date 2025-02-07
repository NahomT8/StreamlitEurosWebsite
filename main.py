import json
import streamlit as st
import pandas as pd
import mplsoccer as mp
from mplsoccer import VerticalPitchPitch

st.title("Soccer Stats")
st.header("Free Soccer data for Euros 2024")

df = pd.read_csv("data\euros_2024_shot_map.csv")
df = df[df['type'] == 'Shot'].reset_index(drop=True)
df['location'] = df['location'].apply(json.loads)

team = st.selectbox("Select a Team", df['team'].sort_values().unique(), index=None)
player = st.selectbox("Select a Player", df['player'].sort_values().unique(), index=None)

def filteredData():
    if team:
        df = df[df['team'] == team]
    if player:
        df = df[df['player'] == team]
    
filtered_df = filteredData(df, team, player)

pitch = VerticalPitchPitch(pitch_type='statsbomb', half = True)
fix, ax = pitch.draw(figsize=(10,10))

def PlotShos(df, ax, pitch):
    for x in df.to_dict(orient='records'):
        pitch.scatter(x=float['location'][0]), y=float['location'[1]],ax=ax, s=1000 * x['shots_statsbomb_xg'], color = 'green'

        if x['shot_outcome']