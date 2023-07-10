from gasp import *

begin_graphics()

Circle((400, 300), 200)
Circle((300, 350), 25)
Circle((500, 350), 25)
Line((370, 270), (400, 330))
Line((370, 270), (425, 270))
Arc((400, 300), 150, 225, 315)


update_when('key_pressed') 
end_graphics()
