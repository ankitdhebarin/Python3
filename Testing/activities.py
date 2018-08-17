def eat(food, is_healthy):
	ending = "because its healthy"
	
	if not is_healthy:
		ending = "because YOLO!"
	
	return f"I am eating {food} {ending}"

def nap(num_hours):
	pass