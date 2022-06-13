import pandas as pd
import numpy as np
from jarowinkler import jarowinkler_similarity

def get_dataframe():
    df = pd.read_csv("data/medicamentos.csv", sep=';', encoding='latin-1')
    return df

def get_prob_value(target,columna,thr,droga):

    med = get_dataframe()
    sims =[]
    method= jarowinkler_similarity
    if droga != "error":
        vocab= list(set(med[med['Principio activo']==droga][columna]))
    else:
        vocab= list(set(med[columna]))

    for word in vocab:
        sims.append(method(target, word))
    if np.max(sims) > thr:
        return vocab[np.argmax(sims)]
    else:
        return "error"

def predict(target):
    final_list = []
    for w in target:
        droga_pred= get_prob_value(w.lower() ,'Principio activo',0.8,"error")
        if droga_pred != "error":
            gramaje_pred= get_prob_value(w.lower(),'Potencia',0.7,droga_pred)
            if gramaje_pred != "error":
                unidad_pred= get_prob_value(w.lower(),'Unidad de potencia',0.7,droga_pred)
            else:
                unidad_pred = "error"
            if droga_pred != "error":
                final_list.append(droga_pred)
            if gramaje_pred != "error":
                final_list.append(gramaje_pred)
            if unidad_pred != "error":
                final_list.append(unidad_pred)

    if gramaje_pred == "error":
        final_list.append(" ")
    if unidad_pred == "error":
        final_list.append(" ")

    return final_list
