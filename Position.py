def backOrinPos():
	x = get_pos_x()
	y = get_pos_y()
	while True:
		for i in range(x):
			move(West)
		for i in range(y):
			move(South)
		break
		
def RelPos(pos):
	x = get_pos_x()
	y = get_pos_y()
	Ax = pos // get_world_size()
	Ay = pos % get_world_size()
	return Ax - x,Ay - y

def goTo(x,y):
	if(y > 0):
		for i in range(x):
			move(East)
	else:
		for i in range(abs(x)):
			move(West)
	if(x > 0):
		for i in range(y):
			move(North)
	else:
		for i in range(abs(y)):
			move(South)
			
def getPos(x,y):
	return x * get_world_size() + y
	
def getCor(Pos):
	size = get_world_size()
	return (Pos // size),(Pos % size)