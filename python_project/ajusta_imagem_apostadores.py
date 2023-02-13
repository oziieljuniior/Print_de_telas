import os
import cv2
from pytesseract import pytesseract
from matplotlib import pyplot as plt
from openpyxl import Workbook
import numpy as np
    
wb = Workbook()
ws = wb.active
wb.title = "Aposta"
indice_ex = 1

i = 0 
odd_original = []

#C:\Program Files\Tesseract-OCR\tesseract.exe
pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

while i <= 500:
    #print("Imagem: ", i)
    name = str(i)+"T_Apostadores.png"
    #/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data/qt_apostadores/
    name_path = "C:/Users/Riallen/Documents/Print_de_telas/data1/qt_apostadores/" + name
    image = cv2.imread(name_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1),np.float32)/25
    dst = cv2.filter2D(gray,-1,kernel)
    blur =cv2.GaussianBlur(dst, (1,1), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    #plt.imshow(thresh),plt.show()
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(thresh, config = custom_config)
    #print("Odd: ", text)
    
    odd_original.append(text)
    
    i += 1
   
print(odd_original)
print(len(odd_original))

# =============================================================================
# # =============================================================================
apostadores_editada = []
bad = ["\n", '.']
for name in odd_original:
    for i in bad:
        name = name.replace(i,"")
#      a = name.replace(",","")
#      b = a.replace("V71","1771")
    apostadores_editada.append(int(name))
# # 
print(apostadores_editada)
print(len(apostadores_editada))
# # 
i = 0
# # 
while i <= 500:
    ap = 'A' + str(indice_ex)
    ws[ap] = apostadores_editada[i]
# #     
    indice_ex += 1
    i += 1
#/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/
name = 'C:\\Users\\Riallen\\Documents\\Print_de_telas\\qt_apostadores1.xlsx'  
wb.save(name)
# #     
# =============================================================================
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    