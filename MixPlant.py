import Ground
import Position

clear()
def plantEn(En,pos):
	Rx,Ry = Position.RelPos(pos) 
	Position.goToRelPos(Rx,Ry)
	if (can_harvest()):
		harvest()
	plant(En)
	farm,(x,y) = get_companion()
	print(x)
	print(y)
	nextPos = Position.getPos(x,y)
	plantEn(farm,nextPos)

plantEn(Entities.Bush,24)