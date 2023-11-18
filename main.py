#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import streamlit as st
import pandas as pd
import pickle as pkl
from ml_predict import modelprediction
import matplotlib.pyplot as plt

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
    pred_haaa = pred['pred_haaa']
    pred_hhaa = pred['pred_hhaa']
    pred_hahh = pred['pred_hahh']
    #st.write(  pred_hhaa['pred_probs']['HH']) 
    species = ("HAAA", "HHAA", "HAHH")
    pred_dict = {
        'HH': (0, pred_hhaa['pred_probs']['HH'], pred_hahh['pred_probs']['HH']),
        'AA': (pred_haaa['pred_probs']['AA'], pred_hhaa['pred_probs']['AA'], 0),
        'HA': (pred_haaa['pred_probs']['HA'], 0, pred_hahh['pred_probs']['HA'])
    }

    x = np.arange(len(species))  # label locations
    width = 0.25  # width of the bars
    fig, ax = plt.subplots()

    for i, (key, values) in enumerate(pred_dict.items()):
        rects = ax.bar(x + i * width, values, width, label=key)
        ax.bar_label(rects, padding=3)

    # Customizing the plot
    ax.set_ylabel('Predicted Probability')
    ax.set_title('Source Prediction for ' + title)
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left')
    ax.set_ylim(0, 1)  # Assuming probabilities range from 0 to 1

    st.pyplot(fig)  # Display the plot in Streamlit

    # # Optional: Display the prediction results as text
    # st.write('--- Predictions ---')
    # st.write(f'Predictions for {title}')
    # # for pred_type, pred_values in pred.items():
    # #     st.write(f'-----{pred_type}-----')
    # #     st.write('Predicted class:', pred_values['pred_class'])
    # #     st.write('Probabilities for each class:')
    # #     for key, value in pred_values['pred_probs'].items():
    # #         st.write(f'{key}: {value}')
