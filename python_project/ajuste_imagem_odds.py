import os
import cv2
import pytesseract
from matplotlib import pyplot as plt

#/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data/odds

path_odds = os.listdir('/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data/odds')
#print(path_odds)
path_imagem = '/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data/odds/38img.png'

image = cv2.imread(path_imagem)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur =cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations= 5)
invert = 255 - opening

plt.imshow(invert),plt.colorbar(),plt.show

        
text = pytesseract.image_to_string(invert, config = "--psm 6")
print(text)
    

