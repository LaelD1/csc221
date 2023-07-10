from gasp import *

begin_graphics()

Circle((300, 200), 200)
Circle((200, 250), 25)
Circle((400, 250), 25)
Line((270, 170), (300, 230))
Line((270, 170), (325, 170))
Arc((300, 200), 150, 225, 315)


update_when('key_pressed') 
end_graphics()
