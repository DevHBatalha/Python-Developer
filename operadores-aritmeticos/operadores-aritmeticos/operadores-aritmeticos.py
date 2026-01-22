#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 11:07:58 2026

@author: heliobatalha
"""

n1 = int( input("Escreva o primeiro número: "))
n2 = int(input("Escreva segundo número: "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
dint = n1 // n2
exp = n1 ** n2

print('A soma é {}, a subtração é {}, produto  é {}, o resto da divisão é {: .2f}' .format(soma, sub, mult, div), end=' ')
print('Divisão interira {} e a Potência {}' . format(dint, exp))




