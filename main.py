from mplsoccer import Pitch
import json
import streamlit as st
import pandas as pd


st.title("Euros 2024 Shot Map")
st.subheader("Filter to any team/player to see all their shots taken.")

df = pd.read_csv("C:\\Users\lilim\\OneDrive\\Desktop\\Streamlit\\data\\euros_2024_shot_map.csv")
df = df[df['type'] == 'Shot'].reset_index(drop=True)
df['location'] = df['location'].apply(json.loads)

team = st.selectbox('Select a Team', df['team'].sort_values().unique(), index=None)
player = st.selectbox('Select a Player', df[df['team'] == team]['player'].sort_values().unique(), index=None)

def filterData(df, team, player):
    if team:
        df = df[df['team'] == team]
    if player:
        df = df[df['player'] == player]

    return df

filtered_df = filterData(df, team, player)

pitch = Pitch(pitch_type="statsbomb", half=True)
fig, ax = pitch.draw(figsize=(10,10))

def plotShots(df, ax, pitch):
    for x in df.to_dict(orient='records'):
        pitch.scatter(
            x=float(x['location'][0]),  # X location (horizontal)
            y=float(x['location'][1]),  # Y location (vertical)
            ax=ax,
            s=1000 * x["shot_statsbomb_xg"],  # Bubble size based on expected goal value
            color='green' if x['shot_outcome'] == 'Goal' else 'white',
            edgecolors='black',
            alpha=1 if x['shot_outcome'] == 'Goal' else 0.5,
            zorder=2 if x['shot_outcome'] == 'Goal' else 1
        )
plotShots(filtered_df, ax, pitch)

st.pyplot(fig)