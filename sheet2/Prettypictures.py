from gasp import *

begin_graphics()

Circle((300, 200), 200)
Circle((200, 250), 25)
Circle((400, 250), 25)
Line((270, 170), (300, 230))
Line((270, 170), (325, 170))
Arc((300, 200), 150, 225, 315)
Arc((120, 230), 35, 105, 235)
Arc((478, 230), 35, -50, 70)



update_when('key_pressed') 
end_graphics()
