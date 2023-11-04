# !/user/bin/env python3
# -*- coding: utf-8 -*-

from scipy.sparse import coo_matrix
import joblib


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
