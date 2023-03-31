#author: darkcover
#Bibliotecas utilizadas
import pyscreenshot as ImageGrab
from PIL import Image
from datetime import datetime
#import mouse

#import pyautogui
#Contadores
i = 0 #Quantidade de amostras pretendida
j = 0 #Contador
k = 0
l = 0
comeco = datetime.now().strftime('%H:%M:%S')
#identificador de odd vermelha
while i <= 10:
    
    #print da tela
    imagem = ImageGrab.grab()
    #salvar imagem com um nome
    imagem.save('tela','jpeg')
    #abrir imagem com a biblioteca Pil, para realizar corte
    img = Image.open('tela')
    #area de corte pretendida
    area0 = (3068,531,3070,533) #area com numeros de tres digitos
    area1 = (2898,538,2902,542) #area com numeros de quatro digitos
    area2 = (2929, 539, 2931, 541) #Area com 5 numeros
    #comando para cortar area da imagem 
    corte = img.crop(area0)
    #salvamento e carregamento da nova imagem de corte para imagem de 3 digitos
    corte.save('3d01.jpg','jpeg')
    img_0 = Image.open('3d01.jpg')
    #conversao da imagem de 3 digitos em rgb
    gg = img_0.convert('RGB').getcolors()
    print("3 digitos:", gg)
    #corte de imagem, salvamentoe carregamento para imagem de 4 digitos
    corte0 = img.crop(area1)
    corte0.save('4d01.jpg','jpeg')
    img_1 = Image.open('4d01.jpg')
    #conversaõ de imagem de 4 digitos
    gg0 = img_1.convert('RGB').getcolors()
    print("4 digitos:", gg0)
    
    corte1 = img.crop(area2)
    corte1.save('5d01.jpg','jpeg')
    img_2 = Image.open('5d01.jpg')
    
    gg1 = img_2.convert('RGB').getcolors()
    print("5 dígitos:", gg1)       
        
    # se qualquer uma das imagens ficarem vermelha, entao havera um corte 
    if gg == [(4, (199, 6, 23))]:
        print('olá nois')
        #areas de cortes pretendidas
        area3 = (2950,450,3330,560)
        area4 = (2062, 140, 2115, 160)
        area5 = (3588,60,3630,80)
        #comando para realizar corte
        fr = img.crop(area3)
        apos = img.crop(area4)
        onl = img.crop(area5)
        #salvamento e contagem dos documento
        i = str(i)
        apos.save(i + "T_Apostadores.png")
        onl.save(i + "T_Online.png")
        fr.save(i + "img.png")
        i = int(i)
        
        j = 0
        i = i + 1
        #enquanto a odd estiver vermelha, não quebrar este comando de carregamento
        while gg == [(4, (199, 6, 23))]:
            #contagem de leituras ate mudança
            j = j +1
            print(j)
            #print da tela até haver mudança de cor
            imagem0 = ImageGrab.grab()
            #salvamento e abertura da imagem
            imagem0.save('foto02','jpeg')
            img_0 = Image.open('foto02')
            #area de corte pretendida
            area0 = (2868, 538, 2872, 542) #area com numeros de tres digitos
            area1 = (2899,539,2900,540) #area com numeros de quatro digitos
            #comando para cortar area da imagem 
            corte = img_0.crop(area0)
            #salvamento e carregamento da nova imagem de corte para imagem de 3 digitos
            corte.save('3d01.jpg','jpeg')
            img_0 = Image.open('3d01.jpg')
            #conversao da imagem de 3 digitos em rgb
            gg = img_0.convert('RGB').getcolors()
            print("3 digitos:", gg)
            #corte de imagem, salvamentoe carregamento para imagem de 4 digitos
            corte0 = img_0.crop(area1)
            corte0.save('4d01.jpg','jpeg')
            img_1 = Image.open('4d01.jpg')
            #conversaõ de imagem de 4 digitos
            gg0 = img_1.convert('RGB').getcolors()
            print("4 digitos:", gg0)
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
                imagem2.save('tela0.jpg', 'jpeg')
                img3 = Image.open('tela0.jpg')
                area2 = (2345,135,3500,220)
                odds = img3.crop(area2)
                k = str(k)
                odds.save(k + "Odds.png")
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