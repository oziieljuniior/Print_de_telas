from mouse_position_class import mouse_position

mouse_click_listener = mouse_position()
mouse_click_listener.run()
#c = mouse_click_listener.run()
#print(type(c))
#c = mouse_click_listener.start()

x1 = mouse_click_listener.x
print(x1)
print(type(x1))

y1 = mouse_click_listener.y
print(y1)
print(type(y1))
