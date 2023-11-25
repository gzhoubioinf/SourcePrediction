#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
# import pandas as pd
# import pickle as pkl

from ml_predict import process
import matplotlib.pyplot as plt


# "class_label" : {
#     "HA": 1,
#     "HH": 2,
#     "AA": 0 },


uploaded_file = ''
text_input = ''


# read genome sequence
# uploaded_file = st.file_uploader("Pls enter your genome sequence")
# Create a file upload component
uploaded_file = st.file_uploader("Upload a file of genome sequence")
# Create a text input component
text_input = st.text_area("Copy and paste the genome sequence  here")
# Read the uploaded file or the text input

button_clicked = st.button("Start prediction.")
if button_clicked:
    st.pyplot(process(uploaded_file, text_input))


