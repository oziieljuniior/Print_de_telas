import pyscreenshot as ImageGrab
from PIL import Image
from tkinter import filedialog

class get_colors:
    def __init__(self):
        self.i = 0
    
    def capture_and_check(self, t, x1 = 1389, y1 = 442, x2 =1411 , y2 =441):
        while self.i <= t:
            
            imagem = ImageGrab.grab()
            #salvar imagem com um nome
            imagem.save('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/tela.jpeg','jpeg')
            #abrir imagem com a biblioteca Pil, para realizar corte
            img = Image.open('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/python_project/search/tela.jpeg')
            #area de corte pretendida
            area0 = (x1,y1,x1 + 1,y1 + 1) #area com numeros de tres digitos
            area1 = (x2,y2,x2 + 1,y2 + 1) #area com numeros de quatro digitos
            #area2 = (2929, 539, 2931, 541) #Area com 5 numeros
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
            
            #corte1 = img.crop(area2)
            #corte1.save('5d01.jpg','jpeg')
            #img_2 = Image.open('5d01.jpg')
            
            #gg1 = img_2.convert('RGB').getcolors()
            #print("5 dígitos:", gg1)       
                
            # se qualquer uma das imagens ficarem vermelha, entao havera um corte 
            if gg0 == [(1, (207, 9, 24))]:
                print("att")
                self.i += 1
            
acc = get_colors()

acc.capture_and_check(t = 5)