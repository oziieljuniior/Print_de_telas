import os
import cv2 
import pytesseract

path_data = os.listdir("/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data")
path_data.sort() 
#print(path_data)
for name in path_data:
    #print(name)
    name_pasta = "/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data/" + name
    path_data_esp = os.listdir(name_pasta)
    path_data_esp.sort()
    for name1 in path_data_esp:
        #print(name1)
        path_arquivo_imagem = name_pasta +"/"+ name1
        #print(path_arquivo_imagem)
        image = cv2.imread(path_arquivo_imagem)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur =cv2.GaussianBlur(gray, (3,3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations= 5)
        invert = 255 - opening
        
        text = pytesseract.image_to_string(invert, config = "--psm 6")
        print(text)
    