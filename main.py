# !/user/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import pickle as pkl
from ml_predict import modelprediction
#
# "class_label" : {
#     "HA": 1,
#     "HH": 2,
#     "AA": 0 },

# read genome sequence
# uploaded_file = st.file_uploader("Pls enter your genome sequence")
# Create a file upload component
uploaded_file = st.file_uploader("Upload a file of genome sequence")
# Create a text input component
text_input = st.text_area("Copy and paste the genome sequence  here")
# Read the uploaded file or the text input
if uploaded_file is not None:
    # User uploaded a file
    file_contents = uploaded_file.read()
    # Decode the binary content into a text format
    decoded_content = file_contents.decode('utf-8')
    # Split the content into lines
    lines = decoded_content.splitlines()
    if lines[0].startswith('>'):
        title = lines[0]
        print(title)

else:
    # User copied and pasted the content

    if text_input.startswith('>'):
        text = text_input.split('\n')
        title = text[0]
        file_contents = ''.join(text[1:])
    else:
        title = 'Your gene sequence'
        file_contents = text_input

if uploaded_file or text_input:
    pred = modelprediction(file_contents)
    st.write(title)
    pred_haaa = pred['pred_haaa']
    pred_hhaa = pred['pred_hhaa']
    pred_hahh = pred['pred_hahh']
    # pred = {
    #     'pred_haaa': pred_haaa,
    #     'pred_hhaa': pred_hhaa,
    #     'pred_hahh': pred_hahh
    # }
    # pred = {
    #     'pred_class': pred_class,
    #     'pred_probs': pred_probs
    # }
    st.write('-----HA vs AA-----')
    st.write('predicted class: ', pred_haaa['pred_class'])
    st.write('probabilities for each class')
    for key, value in pred_haaa['pred_probs'].items():
        st.write(key,':',value)

    # st.write('HH vs AA')
    # st.write(pred['pred_hhaa'])

    st.write('-----HH vs AA-----')
    st.write('predicted class: ', pred_hhaa['pred_class'])
    st.write('probabilities for each class')
    for key, value in pred_hhaa['pred_probs'].items():
        st.write(key, ':', value)

    # st.write('HA vs HH')
    # st.write(pred['pred_hahh'])

    st.write('-----HA vs HH-----')
    st.write('predicted class: ', pred_hahh['pred_class'])
    st.write('probabilities for each class')
    for key, value in pred_hahh['pred_probs'].items():
        st.write(key, ':', value)


