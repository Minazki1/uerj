# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AVH9yVzBy4wsExtDKfDAjPruB4TKAyDs
"""

cartas = []


def maior(vetor):
    valor = 1
    while valor >= 0:
        valor = int(input('Digite o valor da carta: '))
        cartas.append(valor)

    print(f'A carta mais valiosa desse vetor é {max(vetor)}')


maior(cartas)