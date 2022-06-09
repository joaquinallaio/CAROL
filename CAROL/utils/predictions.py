import pandas as pd
import numpy as np
from jarowinkler import jarowinkler_similarity

def get_dataframe():
    df = pd.read_csv("data/medicamentos.csv", sep=';', encoding='latin-1')
    return df

def get_prob_value(target,columna,thr):
    med = get_dataframe()
    sims =[]
    method= jarowinkler_similarity
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
        droga_pred= get_prob_value(w ,'Principio activo',0.8)
        gramaje_pred= get_prob_value(w,'Potencia',0.9)
        unidad_pred= get_prob_value(w,'Unidad de potencia',0.8)

        if droga_pred != "error":
            final_list.append(droga_pred)
        if gramaje_pred != "error":
            final_list.append(gramaje_pred)
        if unidad_pred != "error":
            final_list.append(unidad_pred)
    return final_list
