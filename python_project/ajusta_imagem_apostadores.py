import os
import cv2
import pytesseract
from matplotlib import pyplot as plt
from openpyxl import Workbook
    
wb = Workbook()
ws = wb.active
wb.title = "Aposta"
indice_ex = 1

i = 0 
odd_original = []

while i <= 250:
    print("Imagem: ", i)
    name = str(i)+"T_Apostadores.png"
    name_path = "/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data/qt_apostadores/" + name
    image = cv2.imread(name_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur =cv2.GaussianBlur(gray, (1,1), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    plt.imshow(thresh),plt.show()
    
    text = pytesseract.image_to_string(thresh, config = "--psm 6")
    #print("Odd: ", text)
    
    odd_original.append(text)
    
    i += 1
   
print(odd_original)
print(len(odd_original))

# =============================================================================
odd_editada = []
bad = ["\n\x0c"]
for name in odd_original:
     for i in bad:
         name = name.replace(i,"")
     a = name.replace(",","")
     b = a.replace("V71","1771")
     odd_editada.append(int(b))
# 
print(odd_editada)
print(len(odd_editada))
# 
i = 0
# 
while i <= 250:
    ap = 'A' + str(indice_ex)
    ws[ap] = odd_editada[i]
#     
    indice_ex += 1
    i += 1
name = '/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/qt_apostadores.xlsx'  
wb.save(name)
#     
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    