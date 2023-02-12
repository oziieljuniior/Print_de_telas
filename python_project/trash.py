import pyautogui
i = 0
while i <= 5:
    x = pyautogui.locateOnScreen('C:\\Users\\Riallen\\Documents\\Print_de_telas\\python_project\\search\\vpl.png')
    print(x)
    if x != None:
        print("Locazido com sucesso")
        i += 1
print(i)

