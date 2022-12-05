import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np
import joblib
from prophet.plot import plot_plotly
from datetime import datetime

def show_footer():
    st.markdown("***")
    st.markdown("**Like this tool?** Follow me on "
                "[Twitter](https://twitter.com/).")

def main():
    st.button("Re-run")
    # set up layout
    st.title("Welcome to the burger section")
    st.markdown("Here below some information about burger's sales")
    show_footer()

    data=pd.read_excel('dati.xlsx', 
                     index_col = 'Calendario',
                     parse_dates = True
                     )
    df_burger = data[data['Tipologia'] == 'Burger']
    df_burger = df_burger.drop('Tipologia', axis = 1)
    df_burger = df_burger.reset_index()
    df_burger.columns = ['ds', 'y']

    model = joblib.load('model.pkl')


##mettere periods come slider
    future = model.make_future_dataframe(periods=30, freq='D')
    forecast = model.predict(future)

    fig = plot_plotly(model, forecast)
    fig.update_layout(yaxis_title = 'Quantità',
                  xaxis_title = 'Date',
                  title = 'Vendita Burger'
                  )
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()


