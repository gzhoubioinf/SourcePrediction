# !/user/bin/env python3
# -*- coding: utf-8 -*-
from scipy.sparse import coo_matrix
import joblib
from matplotlib import pyplot as plt
import numpy as np

#
# import sys
# from sklearn.model_selection import cross_val_score, KFold
# from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, cross_validate
# from sklearn.metrics import confusion_matrix, classification_report, balanced_accuracy_score, roc_auc_score
# from sklearn.model_selection import train_test_split, StratifiedKFold
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from datetime import datetime
# from math import sqrt
# import warnings
# testflag = False

def convert_gene_seq(gene_seq: str, voc_col: dict):
    data = []
    row = []
    col = []
    first_key = next(iter(voc_col))
    kmer_list = generate_kmers(gene_seq, len(first_key))
    for k in kmer_list:
        if voc_col.get(k) is None:
            continue
        col.append(voc_col.get(k))
        row.append(voc_col.get(0))
        data.append(1)
    shape = (1, len(voc_col))
    return coo_matrix((data, (row, col)), shape=shape)


def generate_kmers(seq, k):
    kmers = []
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i + k]
        kmers.append(kmer)
    return kmers


def get_model_pred(filename: str, gene_seq: str):
    model_info = joblib.load(filename)
    model = model_info['xgb_model']
    voc_col = model_info['voc_col']
    class_label = model_info['class_label']
    x_test = convert_gene_seq(gene_seq, voc_col)
    pred_class = model.predict(x_test)
    pred_prb = model.predict_proba(x_test)
    cl = [''] * 2
    for k, v in class_label.items():
        if v <= 1:
            cl[v] = k
    pred_probs = {}
    pred_prb = pred_prb.flatten()
    pred_probs= {
        cl[0]: pred_prb[0],
        cl[1]: pred_prb[1],
    }

    # pred_probs = {cl[0]: pred_prb[0], cl[1]: pred_prb[1]}
    pred = {
        'pred_class': cl[int(pred_class)],
        'pred_probs': pred_probs
    }
    return pred


def modelprediction(gene_seq: str):
    pred_haaa = get_model_pred('./data/HAAAxgb_model_ct0.05fn10.pkl', gene_seq)
    pred_hhaa = get_model_pred('./data/HHAAxgb_model_ct0.05fn10.pkl', gene_seq)
    pred_hahh = get_model_pred('./data/HAHHxgb_model_ct0.05fn10.pkl', gene_seq)
    pred = {
        'pred_haaa': pred_haaa,
        'pred_hhaa': pred_hhaa,
        'pred_hahh': pred_hahh
    }

    return pred



def process(uploaded_file, text_input):

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

    return plot_probability(file_contents,title)




def process_cmd(input_file, output):

    # User uploaded a file
    with open(input_file,'rb') as f:
        file_contents = f.read()
    # Decode the binary content into a text format
    decoded_content = file_contents.decode('utf-8')
    # Split the content into lines

    lines = decoded_content.splitlines()
    # print(file_contents)
    if lines[0].startswith('>'):
        title = lines[0]
    else:
        title = 'Gene sequence'


    fig = plot_probability(file_contents,title)
    fig.savefig(output, format='pdf')

    

def plot_probability(file_contents,title):
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

    return fig 
