# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:25:31 2021

@author: Jonat
"""

import streamlit as st
import pandas as pd

st.title("Understanding Kickstarter Campaigns")

@st.cache
def load_data(nrows = 1000):
    df = pd.read_csv('https://raw.githubusercontent.com/JonathanBechtel/dat-02-22/main/ClassMaterial/Unit3/data/ks2.csv',
                      nrows = nrows)
    return df
    
nrows = st.sidebar.number_input("Number of Rows to Load", min_value = 1000,
                        max_value = 10000, step = 1000)

df = load_data(nrows)

st.write(df)
