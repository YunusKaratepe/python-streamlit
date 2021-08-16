import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open('dnalogo.png')

st.image(image, use_column_width=True)

st.write(
    """
        # DNA Nucleotide Count

        Showing the counts of nucleotide composition of query DNA.

        ***
    """
)

st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nACGTACGATCGAAGGCTCTTTCAATCGACGTCCCTAAACTGGCTATC"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""
    ***
""")

# print dna sequence
st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (Nucleotide Count)')

# 1. way
st.subheader('1. way to go')


def dna_nuc_count(seq):
    d = {
        "A": seq.count('A'),
        "T": seq.count('T'),
        "G": seq.count('G'),
        "C": seq.count('C')
    }
    return d

st.write("Total Nucleotide Count:", len(sequence))

x = dna_nuc_count(sequence)

xlabel = list(x)
xvalues = list(x.values())

x

# 2. way
st.subheader('2. way to go')
st.write('There are', x["A"], 'Adenine (A)')
st.write('There are', x["T"], 'Thymine (T)')
st.write('There are', x["G"], 'Guanine (G)')
st.write('There are', x["C"], 'Cytosine (C)')

# 3. way
st.subheader('3. way to go')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({ 0: "count" }, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = { 'index': 'nucleotide' })
st.write(df)

# 4. way
st.subheader('4. way to go')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80) # width of the bar
)
st.write(p)




