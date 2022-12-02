import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np


def show_footer():
    st.markdown("***")
    st.markdown("**Like this infomanager tool?** Follow me on "
                "[Twitter](https://twitter.com/xxxxxx).")
def main():
    st.button("Re-run")
    st.title("Welcome page1")
    st.markdown("***")
    show_footer()

if __name__ == "__main__":
    main()


