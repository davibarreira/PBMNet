#Break Captcha
"""
Essa função recebe uma imagem e o dataframe com os símbolos 
do captcha que iremos quebrar.

O algoritmo realiza as seguintes tarefas em ordem:
1) Ao receber a imagem, ele realiza um tratamento de remoção do fundo;:
3) Extrai o "spectro" da imagem, que é a soma por coluna;
2) Passa a função de prever os captchas e retorna a previsão.
"""


import pandas as pd
from PIL import Image
import numpy as np


def BreakCaptcha(image_path,sinais_path='sinais.pkl'):
	image  = np.array(Image.open(image_path).convert('L')) #Converte gray
	image[np.where(image<200)] = 0
	spec   = image.sum(axis=0)
	sinais = pd.read_pickle(sinais_path)
	guess  = Predict_Captcha(spec, sinais)

	return guess

def Predict_Captcha(spec,sinais):
    prev = [] #Lista com simbolos previstos
    shift= 0
    for i in range(4):
        if i ==0:
            begin = 30
            p, shift = Predict_Simbol(spec,sinais,begin)
            prev.append(p)
        else:
            begin = int(begin + sinais['size'][sinais['simbolo']==prev[-1]].values[0]+shift)
            p, shift = Predict_Simbol(spec,sinais,begin)
            prev.append(p)
    return prev

def Predict_Simbol(spec,sinais,begin=30):
    lw    = 4 # Aumenta o tamanho do sinal que se vai testar
    shifts= []
    erros = []
    for k in range(len(sinais)):
        size     = int(sinais['size'].iloc[k])
        shift    = int(lw - np.correlate(sinais.iloc[k]['signal'],spec[begin:begin+size+lw]).argmax())
        adj_begin    = begin + shift
        erro_abs = np.abs(sinais['signal'].iloc[k] - spec[adj_begin:adj_begin+size]).sum()
        erro_per = erro_abs/(spec[adj_begin:adj_begin+size].sum()+0.01)
        if erro_per <= 0.1:
            return sinais['simbolo'][k],shift
        else:
            shifts.append(shift)
            erros.append(erro_per)
    return sinais['simbolo'][np.array(erros).argmin()],shifts[np.array(erros).argmin()]