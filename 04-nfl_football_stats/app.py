import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats (Rushing)')

st.markdown(
    """
        This app performs webscraping of NFL Football players data.
        * **Data Source:** [pro-football-reference.com](https://pro-football-reference.com)
    """
)

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, 2021))))

# scraping of NFL players
@st.cache
def load_data(year):
    url = f"https://www.pro-football-reference.com/years/{year}/rushing.htm"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df["Age"] == "Age"].index)
    raw = raw.fillna('0')
    playerstats = raw.drop(["Rk"], axis=1)
    return playerstats

playerstats = load_data(selected_year)
# playerstats

# sidebar - team selection
sorted_unique_team = sorted(playerstats["Tm"].unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# sidebar - pos selection
sorted_unique_pos = ["RB", "QB", "WR", "FB", "TE"]
selected_pos = st.sidebar.multiselect('Position', sorted_unique_pos, sorted_unique_pos)

# filter data

df_selecteds = playerstats[(playerstats["Tm"].isin(selected_team)) & (playerstats["Pos"].isin(selected_pos))]

rows, cols = df_selecteds.shape
st.header('Display Player Stats of Selected(s)')
st.write(f'Data dimension: {rows} rows and {cols} cols.')
st.dataframe(df_selecteds)


# Download NFL Player Stats data
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"<a href='data:file/csv;base64,{b64}' download='playerstats.csv'>Download CSV File </a>"
    return href

st.markdown(file_download(df_selecteds), unsafe_allow_html=True)


# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selecteds.to_csv('output.csv')
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
        st.pyplot(f, ax)


