from pynput import mouse

def on_click(x,y,button,pressed):
    if pressed:
        print(button,x,y)
        print(type(x))
        print(type(y))
        print(type(button))
with mouse.Listener(on_click=on_click) as listener:
    listener.join()