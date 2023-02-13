#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Fev 2023

@author: darkcover
"""

#author: darkcover
#Bibliotecas utilizadas
#Olhar requerimentos.txt
import pyscreenshot as ImageGrab
from PIL import Image
from datetime import datetime
#import mouse
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
wb.title = "Hora_Apostas"
indice_excel = 1

#import pyautogui
#Contadores
i_0 = int(input("Quantidade de amostras pretendida: "))
i = 0 #Quantidade de amostras pretendida
j = 0 #Contador
k = 0
l = 0
comeco = datetime.now().strftime('%H:%M:%S')
#identificador de odd vermelha
while i <= i_0:
    print("Amostra: ", i + 1)
    imagem = ImageGrab.grab()
    #salvar imagem com um nome
    imagem.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/tela.jpeg','jpeg')
    #abrir imagem com a biblioteca Pil, para realizar corte
    img = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/tela.jpeg')
    #area de corte pretendida
    area0 = (1389,442,1390,443) #area com numeros de tres digitos
    area1 = (1411,441,1412,442) #area com numeros de quatro digitos
    area2 = (1434,442,1435,443) #Area com 5 numeros
    #comando para cortar area da imagem 
    corte = img.crop(area0)
    #salvamento e carregamento da nova imagem de corte para imagem de 3 digitos
    corte.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/3d01.jpeg','jpeg')
    img_0 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/3d01.jpeg')
    #conversao da imagem de 3 digitos em rgb
    gg = img_0.convert('RGB').getcolors()
    print("3 digitos:", gg)
    #[(1, (219, 0, 20))]
    #corte de imagem, salvamentoe carregamento para imagem de 4 digitos
    corte0 = img.crop(area1)
    corte0.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/4d01.jpeg','jpeg')
    img_1 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/4d01.jpeg')
    #conversaõ de imagem de 4 digitos
    gg0 = img_1.convert('RGB').getcolors()
    print("4 digitos:", gg0)
    #[(1, (207, 9, 24))]
    
    corte1 = img.crop(area2)
    corte1.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/5d01.jpeg','jpeg')
    img_2 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/5d01.jpeg')
    
    gg1 = img_2.convert('RGB').getcolors()
    print("5 dígitos:", gg1)       
        
    # se qualquer uma das imagens ficarem vermelha, entao havera um corte 
    if gg == [(1, (219, 0, 20))] or gg0 == [(1, (207, 9, 24))] or gg1 == [(1, (212, 0, 27))]:
        print('Fase 1 - Captura de Odd e Apostas')
        #areas de cortes pretendidas
        area3 = (1295,380,1575,455)
        area4 = (1100,805,1145,823)
        #area5 = (975,6,1017,21)
        #comando para realizar corte
        fr = img.crop(area3)
        apos = img.crop(area4)
        #onl = img.crop(area5)
        #salvamento e contagem dos documento
        i = str(i)
        name_apos = i + "T_Apostadores.png" 
        name_fr = i + "img.png" 
        #name_onl = i + "T_Hora.png" 
        apos.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data2/qt_apostadores/' + name_apos)
        #onl.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data1/' + name_onl)
        fr.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data2/odds/' + name_fr)
        i = int(i)
        
        indice = "A" + str(indice_excel)
        ws[indice] = datetime.now().strftime('%H:%M:%S')
        
        j = 0
        i = i + 1
        indice_excel += 1
        #enquanto a odd estiver vermelha, não quebrar este comando de carregamento
        while gg == [(1, (219, 0, 20))] or gg0 == [(1, (207, 9, 24))] or gg1 == [(1, (212, 0, 27))]:
            #contagem de leituras ate mudança
            j = j +1
            print(j)
            #print da tela até haver mudança de cor
            imagem = ImageGrab.grab()
            #salvamento e abertura da imagem
            imagem.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/foto02.jpeg','jpeg')
            img = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/foto02.jpeg')
            #area de corte pretendida
            area0 = (1389,442,1390,443) #area com numeros de tres digitos
            area1 = (1411,441,1412,442) #area com numeros de quatro digitos
            area2 = (1434,442,1435,443) #Area com 5 numeros
            #comando para cortar area da imagem 
            corte = img.crop(area0)
            #salvamento e carregamento da nova imagem de corte para imagem de 3 digitos
            corte.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/3d01.jpeg','jpeg')
            img_0 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/3d01.jpeg')
            #conversao da imagem de 3 digitos em rgb
            gg = img_0.convert('RGB').getcolors()
            print("3 digitos:", gg)
            
            #corte de imagem, salvamentoe carregamento para imagem de 4 digitos
            corte0 = img.crop(area1)
            corte0.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/4d01.jpeg','jpeg')
            img_1 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/4d01.jpeg')
            #conversaõ de imagem de 4 digitos
            gg0 = img_1.convert('RGB').getcolors()
            print("4 digitos:", gg0)
            
            corte1 = img.crop(area2)
            corte1.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/5d01.jpeg','jpeg')
            img_2 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/5d01.jpeg')
    
            gg1 = img_2.convert('RGB').getcolors()
            print("5 dígitos:", gg1)       
        
    
            #resgistro de odds gerais
            #Registro do minuto atual, e retirar o resto da divisão por 12
            minu = datetime.now().strftime('%M')
            d = int(minu)
            d0 = d%12
            d0 = str(d0)
            print("Resto da divisão:", d0)
            d0 = int(d0)
            #Se o minuto tiver resto 0 ou 6, tire print da tela
            if d0 == 0 or d0 == 6:
                #comando para tirar print da tela 
                imagem2 = ImageGrab.grab()
                imagem2.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/tela0.jpeg', 'jpeg')
                img3 = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/tela0.jpeg')
                area2 = (970,262,1896,362)
                odds = img3.crop(area2)
                k = str(k)
                name_odds = k + "Odds.png" 
                odds.save("/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data2/odds_gerais/" + name_odds)
                k = int(k)
                k = k+1
                print("Tirou print das odds")
            #if d0 == 4 or d0 == 8:
             #   print("Clicou na tela")
              #  mouse.move(2025,75, absolute = True, duration = 0.01)
               # mouse.click('right')
            else:
                print("Não fez nada")

    else:
        print('Deu ruim')
print("Começou:", comeco)   
fim = datetime.now().strftime('%H:%M:%S')
print("Terminou em:",fim)
print("Quantidade de odds coletadas: ", i + 1)
wb.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/hora_apostas.xlsx')
