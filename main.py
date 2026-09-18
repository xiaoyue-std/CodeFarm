import Position

def plantEn(farm):
	Position.backOrinPos()	
	flag = False
	while True:
		x = 0
		while True:
			if(flag == True):
				break
			if(farm == Entities.Grass):
				harvest()
			else:
				plant(farm)
			move(North)
			x = x + 1
			if(x % 22 == 0):
				move(West)
			if(x % (22 * 22) == 0):
				break
		while True:
			if(can_harvest()):
				harvest()
				if(farm != Entities.Grass):
					plant(farm)
				move(North)
				x = x + 1
			if(x % 22 == 0):
				move(West)
			if(x % (22 * 22) == 0):
				break
		flag = True

import Ground
clear()
Ground.tillAll(get_world_size())
plantEn(Entities.Sunflower)
