# -*- coding: utf-8 -*-

altura = float(input('Entra com o valor da altura em metros '))
largura = float(input('Entra com o valor da largura em metros '))
area = altura * largura
print('Com base na altura {:.2f} metros e a largura {:.2f} metros corresponde \n a uma area de {:.2f} metros quadrados' .format(altura, largura, area))