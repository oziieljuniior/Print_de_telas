import os
import cv2
import pytesseract
from matplotlib import pyplot as plt
import numpy as np
import time
import mysql.connector

mydb = mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "14072849",
            database = 'Aviator'
        )

mycursor = mydb.cursor()

sql = "INSERT INTO odds (id, odd, hora_criacao, apostadores) VALUES (%s,%s,%s,%s)"


i = 0
odd_original = []
apostadores_original = []
odds_hora = []

i_0 = int(input("Quantidade de conversões: "))

caminho_odds =  '/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data3/odds'
caminho_apostadores = '/home/oziel/Documentos/Personal_project/Aviator/Print_de_telas/data3/qt_apostadores'

while i <= i_0:
    lista_odds = os.listdir(caminho_odds)
    t1 = len(lista_odds)
    lista_apostadores = os.listdir(caminho_apostadores)
    t2 = len(lista_apostadores)
    
    print(t1,t2, i)
    if t1 == i + 1 and t2 == i + 1:
        time.sleep(2)
        name1 = caminho_odds + "/" + str(i) + 'img.png'
        image1 = cv2.imread(name1)
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        blur1 =cv2.GaussianBlur(gray1, (3,3), 0)
        thresh1 = cv2.threshold(blur1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        #       
        file_info = os.stat(name1)
        creation_time = time.ctime(file_info.st_ctime)
        #
        name2 = str(i)+"T_Apostadores.png"
        #C:/Users/Riallen/Documents/Print_de_telas/data1/qt_apostadores/
        name_path2 = caminho_apostadores + '/' + name2
        image2 = cv2.imread(name_path2)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        kernel2 = np.ones((1,1),np.float32)/3
        dst2 = cv2.filter2D(gray2,-1,kernel2)
        blur2 =cv2.GaussianBlur(dst2, (1,1), 0)
        thresh2 = cv2.threshold(blur2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        
        #plt.imshow(thresh),plt.show()
        #plt.imshow(thresh2),plt.show()
        
        custom_config = r'--oem 3 --psm 6 outputbase digits'
        text2 = pytesseract.image_to_string(thresh2, config = custom_config)
        text1 = pytesseract.image_to_string(thresh1, config = "--psm 6")
        
        bad1 = ['\n\x0c','x','X', ' ']
        bad2 = ['\n', '.', ' ']
        for j in bad1:
            text1 = text1.replace(j,'')
        for k in bad2:
            text2 = text2.replace(k,'')
#     
        apostadores_original.append(text2)
        odd_original.append(text1)
        odds_hora.append(creation_time)
        print("Odd: ", text1)
        print("Hora da criação: ", creation_time)
        print("Apostadores: ", text2)

        values = (i, text1,creation_time,text2)
        
        mycursor.execute(sql,values)
        
        mydb.commit()
         

        i += 1
        
        
    else:
        print("Esperando atualização")
    
mycursor.close()
mydb.close()