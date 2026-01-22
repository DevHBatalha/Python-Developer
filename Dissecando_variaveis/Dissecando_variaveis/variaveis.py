#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 10:37:54 2026

@author: heliobatalha
"""

a = input("Escreva Qualquer Coisa: ")
print("O tipo primitivo de valor ´é: ", type(a))
print("É um número: ", a.isnumeric())
print("Só tem espaço: ", a.isspace())
print("É alfabético: ", a.isalpha())
print("É alfanúmerico: ", a.isalnum())
print("Está em maiúsculas?", a.isupper())
print("Está em menúsculas??", a.islower())
print("Está capitalizada?", a.istitle())