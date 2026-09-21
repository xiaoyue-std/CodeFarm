import Position
cur_dir = 0

def goDriction(cur_dir):
	way = [West,North,East,South]
	for i in [-1,0,1,2]:
		idx = (cur_dir + i + 4) % 4
		if (can_move(way[idx])):
			return idx 
	return 0			

def buildMaze(size):
	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,size)

Position.backOrinPos()	
cur_dir = 0
way = [West,North,East,South]
buildMaze(22)
while True:
	if(get_entity_type() == Entities.Treasure):
		harvest()
		Position.backOrinPos()
		buildMaze(22)
	cur_dir	 = goDriction(cur_dir)
	move(way[cur_dir])
	
	
	