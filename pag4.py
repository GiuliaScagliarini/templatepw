import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px 

def show_footer():
    st.markdown("***")
    st.markdown("**Like this tool?** Follow me on "
                "[Twitter](https://twitter.com/).")

def main():
    st.button("Re-run")
    # set up layout
    st.title("Welcome to the pag4")
    st.markdown("Coming soon ... Sign up [here]() to get notified.")
    show_footer()

if __name__ == "__main__":
    main()

