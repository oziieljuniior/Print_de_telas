from pynput import mouse

class mouse_position:
    def __init__(self):
        self.listener = mouse.Listener(on_click=self.on_click)
        self.contador = 0

    def on_click(self,x,y,button,pressed):
        #print(pressed)
        #print(type(pressed))
        if pressed:
            if self.contador == 0:
                print(button,x,y)
                self.x = x
                self.y = y
                self.listener.stop()
            self.contador += 1
    
        
    def run(self):
        with self.listener:
            self.listener.join()
            
