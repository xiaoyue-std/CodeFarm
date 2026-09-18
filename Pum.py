import Ground
import Position

def confirmPum(size,begin):
	p = begin
	Position.goTo(p)
	while True:
		if (not can_harvest()):
			return False,p
		move(North)
		p = p + 1
		if (p % size == 0):
			move(East)
		if (p % (size * size) == 0):
			break
	return True,0

def plantPum(size,needTill):
	first = False
	if(needTill):
		Ground.tillAll(size)
	x = 0
	while True:
		p = x
		while True:
			if (first and (not can_harvest())):
				plant(Entities.Pumpkin)
			else:
				plant(Entities.Pumpkin)
			p = p + 1
			move(North)
			if (p % size == 0):
				move(East)
			if (p % (size * size) == 0):
				first = True
				break
		flag,x = confirmPum(size,x)
		if flag:
			Position.backOrinPos()
			break
		Position.goTo(x)
		