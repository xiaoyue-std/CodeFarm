import Position

def tillAll(size):
	Position.backOrinPos()
	x = 0
	while True:
		till()
		move(North)
		x = x + 1
		if(x % size == 0):
			move(East)
		if(x == size * size):
			return 0

def harvestAll():
	x = 0
	size = get_world_size()
	Position.backOrinPos()
	while True:
		if can_harvest():
			harvest()
		move(North)
		x = x + 1
		if(x % size == 0):
			move(East)
		if(x == size * size):
			return 0
			