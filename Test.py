import Ground
import Position
import Pum

set_world_size(6)
size = get_world_size()
print(size)



clear()
first = True
Position.backOrinPos()
while True:
	Pum.plantPum(size,first)
	harvest()
	first = False
