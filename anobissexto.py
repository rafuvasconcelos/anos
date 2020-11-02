# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:19:17 2020

@author: Rafael Vasconcelos
"""

def ano_bissexto(ano):
    if ano % 400 == 0 and ano % 100 != 0 or ano % 4 == 0:
        print("366 dias")
    else:
        print(" 365 dias ")


ano = int(input("quantos dias tem um ano: "))
ano_bissexto(ano)
