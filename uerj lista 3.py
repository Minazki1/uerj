# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AVH9yVzBy4wsExtDKfDAjPruB4TKAyDs
"""

pontuacoes_personagens = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def media_atributo(matriz):
    num = 1
    for i in range(len(matriz)):
        print(f'A média do {num}º atributo é {sum(matriz[i])/len(matriz[i])}')
        num += 1


media_atributo(pontuacoes_personagens)