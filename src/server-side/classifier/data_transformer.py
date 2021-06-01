import math

# Euclidean distance
def dist(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def findDegrees(point_9):
	dotproduct = sum((a*b) for a, b in zip((0,10), point_9))
	degrees = math.acos(dotproduct / 100)
	return degrees 


# Translate all coordinates so that point 0 is on the origin
def translate(hand_gesture):
	x_dif = hand_gesture[1]
	y_dif = hand_gesture[2]
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]

	hand_gesture = [hand_gesture[0]]
	i = 0
	while i < len(x):
		new_x = round(x[i] - x_dif, 3)	
		hand_gesture.append(new_x)

		new_y = round(y[i] - y_dif, 3)		
		hand_gesture.append(new_y)
		i += 1
	return hand_gesture


# Normalise the distances between point 0 and point 9 to 10 units
def enlarge(hand_gesture): 
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]

	# Find the scale factor 	
	p_0 = (x[0], y[0])
	p_9 = (x[9], y[9])
	scale_factor = 10/dist(p_0, p_9)

	i = 1
	while i < len(hand_gesture):
		hand_gesture[i] = hand_gesture[i]*scale_factor
		hand_gesture[i] = round(hand_gesture[i], 3)
		i +=1
	return hand_gesture 


# Rotate around origin so that point 0 and point 9 are both on y axis for each gesture 
def rotate(hand_gesture):
	x = hand_gesture[1::2] 
	y = hand_gesture[2::2]
	hand_gesture = [hand_gesture[0]]

	# Find how much to rotate by 
	point_9 = (x[9], y[9])
	degrees = findDegrees(point_9)
	
	# Rotate points by degrees and add them to list
	i = 0
	while i < len(x):
		tmp = x[i]
		x[i] = round((math.cos(degrees) * x[i] - math.sin(degrees) * y[i]),3)
		y[i] = round((math.sin(degrees) * tmp + math.cos(degrees) * y[i]),3)
		hand_gesture.extend([x[i], y[i]])
		i+=1
	return hand_gesture


