def backOrinPos():
	x = get_pos_x()
	y = get_pos_y()
	while True:
		for i in range(x):
			move(West)
		for i in range(y):
			move(South)
		break
		
def goTo(Pos):
	backOrinPos()
	for i in range(Pos // get_world_size()):
		move(East)
	for i in range(Pos % get_world_size()):
		move(North)
		
def RelPos(pos):
	x = get_pos_x()
	y = get_pos_y()
	Ax = pos // get_world_size()
	Ay = pos % get_world_size()
	return Ax - x,Ay - y

def goToRelPos(x,y):
	if(x > 0):
		for i in range(x):
			move(North)
	else:
		for i in range(abs(x)):
			move(South)
	if(y > 0):
		for i in range(y):
			move(East)
	else:
		for i in range(abs(y)):
			move(West)

def getPos(x,y):
	return x * get_world_size() + y