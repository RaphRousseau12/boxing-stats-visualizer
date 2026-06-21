import streamlit as st

st.set_page_config(
    page_title="Boxing Stats Visualizer",
    page_icon="🥊",
    layout="wide",
)


#Permanent header
container = st.container(border=True)
with container: 
    left, right = st.columns([7, 3], vertical_alignment="center")
    with left:
        container.title("Boxing Stats Visualizer")
    with right:
        ""