import random
attempt_num = 0
score = 0

#Initialize Game
game_frame = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] #intial 4x4 setup
startlist = [0,1,2,3]
startrow = random.choice(startlist)
startcolumn = random.choice(startlist)
game_frame[startrow][startcolumn] = 2

#Define functions
def up(game_frame): #move up
	i = 0
	for h in range(0, 4): #iterate through all columns
		if game_frame[i][h]!= 0 or game_frame[i+1][h]!= 0 or game_frame[i+2][h]!= 0 or game_frame[i+3]!= 0: #loop through, find non-zeros
			if game_frame[i][h]==0:
				while game_frame[i][h]==0: #loop till item 1 becomes non-zero
					game_frame[i][h] = game_frame[i+1][h]
					game_frame[i+1][h] = game_frame[i+2][h]
					game_frame[i+2][h] = game_frame[i+3][h]
					game_frame[i+3][h] = 0

			if game_frame[i+1][h]==0 and (game_frame[i+2][h]!= 0 or game_frame[i+3][h]!=0): #check if 2nd item is zero followed by non-zeros
				while game_frame[i+1][h]==0: #loop till item 2 becomes non-zero
					game_frame[i+1][h] = game_frame[i+2][h]
					game_frame[i+2][h] = game_frame[i+3][h]
					game_frame[i+3][h] = 0

			if game_frame[i+2][h]==0 and game_frame[i+3][h]!= 0: #check if 3rd member is zero followed by non-zeros
				while game_frame[i+2]==0: #loop till item 3 becomes non-zero
					game_frame[i+2] = game_frame[i+3]
					game_frame[i+3][h] =0 

				#------------------------------------------#

def up_sum(game_frame):
	i = 0
	global score
	for h in range(0,4): #iterate through all columns
		if game_frame[i][h] == game_frame[i+1][h]: #check if item 1 & 2 are the equal
			game_frame[i][h] == game_frame[i][h] + game_frame[i+1][h] #add item 1 & 2
			score += game_frame[i][h] **2 #add points for same tiles
			game_frame[i+1][h] = game_frame[i+2][h] #move item 3 up
			game_frame[i+2][h] = game_frame[i+3][h] #move item 4 up
			game_frame[i+3][h] = 0	#set item 4 to zero/empty
	
		if game_frame[i+1][h] == game_frame[i+2][h]: #check if item 2 & 3 are the equal
			game_frame[i+1][h] == game_frame[i+1][h] + game_frame[i+1][h] #add item 2 & 3
			score += game_frame[i+1][h] **2 #add points for same tiles
			game_frame[i+2][h] = game_frame[i+3][h] #move item 4 up
			game_frame[i+3][h] = 0	#set item 4 to zero/empty

		if game_frame[i+2][h] == game_frame[i+3][h]: #check if item 3 & 4 are the equal
			game_frame[i+2][h] == game_frame[i+2][h] + game_frame[i+1][h] #add item 3 & 4
			score += game_frame[i+2][h] **2 #add points for same tiles
			game_frame[i+3][h] = 0	#set item 4 to zero/empty

			#----------------------------------------------#

def down(game_frame):
	i = 0
	for h in range(0, 4): #iterate through all columns
		if game_frame[i][h]!= 0 or game_frame[i+1][h]!= 0 or game_frame[i+2][h]!= 0 or game_frame[i+3]!= 0: #loop trhough, find non-zeros
			if game_frame[i+3][h]==0: #check if item 4 is zero
				while game_frame[i+3][h]==0: #loop till item 4 becomes non-zero
					game_frame[i+3][h] = game_frame[i+1][h]
					game_frame[i+2][h] = game_frame[i+2][h]
					game_frame[i+1][h] = game_frame[i+3][h]
					game_frame[i][h] = 0

			if game_frame[i+2][h]==0 and (game_frame[i+1][h]!= 0 or game_frame[i][h]!=0): #check if item 3 is zero followed by non-zeros
				while game_frame[i+1][h]==0: #loop till item 3 becomes non-zero
					game_frame[i+2][h] = game_frame[i+1][h]
					game_frame[i+1][h] = game_frame[i][h]
					game_frame[i][h] = 0
			
			if game_frame[i+1][h]==0 and game_frame[i][h]!= 0: #check if item 2 is zero followed by non-zeros
				while game_frame[i+2]==0: #loop till item 3 becomes non-zero
					game_frame[i+2] = game_frame[i][h]
					game_frame[i][h] =0 

			#-----------------------------------------------#

def down_sum(game_frame):
	global score
	for h in range(0,4): #iterate through all columns
		if game_frame[i+3][h] == game_frame[i+2][h]: #check if item 3 & 4 are the same
			game_frame[i+3][h] = game_frame[i+3][h] + game_frame[i+2][h]
			score += game_frame[i+3][h] **2 #add points
			game_frame[i+2][h] = game_frame[i+1][h] #move item 2 down
			game_frame[i+1][h] = game_frame[i][h] #move item 1 down
			game_frame[i][h] = 0 #set item 1 to zero/empty

		if game_frame[i+2][h] == game_frame[i+1][h]: #check if item 3 & 4 are the same
			game_frame[i+2][h] = game_frame[i+2][h] + game_frame[i+1][h]
			score += game_frame[i+2][h] **2 #add points
			game_frame[i+1][h] = game_frame[i][h] #move item 1 down
			game_frame[i][h] = 0 #set item 1 to zero/empty

		if game_frame[i+1][h] == game_frame[i+1][h]: #check if item 1 & 2 are the same
			game_frame[i+2][h] = game_frame[i+2][h] + game_frame[i+1][h]
			score += game_frame[i+2][h] **2 #add points
			game_frame[i][h] = 0 #set item 1 to zero/empty

			#----------------------------------------------#

def left(game_frame):
	h = 0
	for i in range(0,4): #iterate through all rows
		if game_frame[i][h]!= 0 or game_frame[i][h+1]!= 0 or game_frame[i][h+2]!= 0 or game_frame[i][h+3]!= 0:
			if game_frame[i][h] ==0: #check if item 1 is zero
				while game_frame[i][h] ==0:
					game_frame[i][h] = game_frame[i][h+1]
					game_frame[i][h+1] = game_frame[i][h+2]
					game_frame[i][h+2] = game_frame[i][h+3]
					game_frame[i][h+3] = 0
					
			if game_frame[i][h+1]== 0 or game_frame[i][h+2]!= 0 or game_frame[i][h+3]!= 0: #check if item 2 is zero followed by non-zero
				while game_frame[i][h] ==0:
					game_frame[i][h+1] = game_frame[i][h+2]
					game_frame[i][h+2] = game_frame[i][h+3]
					game_frame[i][h+3] = 0

			if game_frame[i][h+2]== 0 or game_frame[i][h+3]!= 0: #check if item 2 is zero followed by non-zero
				while game_frame[i][h] ==0:
					game_frame[i][h+1] = game_frame[i][h+2]
					game_frame[i][h+2] = game_frame[i][h+3]
					game_frame[i][h+3] = 0

			#----------------------------------------------#

def left_sum(game_frame):
	h = 0
	global score
	for i in range(0,4): #iterate through all rows
		if game_frame[i][h] == game_frame[i][h+1]: #check if item 1 & 2 are the same
			game_frame[i][h] = game_frame[i][h]+game_frame[i][h+1] #add item 1 & 2
			points += game_frame[i][h] **2 #add equal tiles
			game_frame[i][h+1] = game_frame[i][h+2] #move item 3 left
			game_frame[i][h+2] = game_frame[i][h+2] #move item 4 left
			game_frame[i][h+3] = 0 #set item 4 in row as zero/empty
			
		if game_frame[i][h+1] == game_frame[i][h+2]: #check if item 2 & 3 are the same
			game_frame[i][h+1] = game_frame[i][h+1]+game_frame[i][h+1] #add item 1 & 2
			points += game_frame[i][h+1] **2 #add equal tiles
			game_frame[i][h+2] = game_frame[i][h+2] #move item 4 left
			game_frame[i][h+3] = 0 #set item 4 in row as zero/empty	

		if game_frame[i][h+2] == game_frame[i][h+3]: #check if item 3 & 4 are the same
			game_frame[i][h+2] = game_frame[i][h+2]+game_frame[i][h+3] #add item 1 & 2
			points += game_frame[i][h+2] **2 #add equal tiles
			game_frame[i][h+3] = 0 #set item 4 in row as zero/empty	

			#---------------------------------------------#

def right(game_frame):
	h = 0
	for i in range(0,4): #iterate through all rows
		if game_frame[i][h]!= 0 or game_frame[i][h+1]!= 0 or game_frame[i][h+2]!= 0 or game_frame[i][h+3]!= 0:
			if game_frame[i][h+3] ==0: #check if item 4 is zero
				while game_frame[i][h+3] ==0:
					game_frame[i][h+3] = game_frame[i][h+2]
					game_frame[i][h+2] = game_frame[i][h+1]
					game_frame[i][h+1] = game_frame[i][h]
					game_frame[i][h] = 0
					
			if game_frame[i][h+2]== 0 and (game_frame[i][h+1]!= 0 or game_frame[i][h]!= 0): #check if item 3 is zero followed by non-zero
				while game_frame[i][h+2] ==0:
					game_frame[i][h+2] = game_frame[i][h+1] #loop till item 3 becomes non-zero
					game_frame[i][h+1] = game_frame[i][h]
					game_frame[i][h] = 0

			if game_frame[i][h+1]== 0 and game_frame[i][h]!= 0: #check if item 2 is zero followed by non-zero
				while game_frame[i][h+2] ==0:
					game_frame[i][h+1] = game_frame[i][h] #loop till item 2 becomes non-zero
					game_frame[i][h] = 0

			#----------------------------------------------#

def right_sum(game_frame):
	h = 0
	global score
	for i in range(0,4): #iterate through all rows
		if game_frame[i][h+3] == game_frame[i][h+2]: #check if item 3 & 4 are the same
			game_frame[i][h+3] = game_frame[i][h+3]+game_frame[i][h+2] #add item 3 & 4
			points += game_frame[i][h+3] **2 #add equal tiles
			game_frame[i][h+2] = game_frame[i][h+1] #move item 2 right
			game_frame[i][h+1] = game_frame[i][h] #move item 1 right
			game_frame[i][h] = 0 #set item 1 in row as zero/empty
			
		if game_frame[i][h+2] == game_frame[i][h+1]: #check if item 2 & 3 are the same
			game_frame[i][h+2] = game_frame[i][h+2]+game_frame[i][h+1] #add item 2 & 3
			points += game_frame[i][h+2] **2 #add equal tiles
			game_frame[i][h+1] = game_frame[i][h] #move item 1 right
			game_frame[i][h] = 0 #set item 4 in row as zero/empty

		if game_frame[i][h+1] == game_frame[i][h]: #check if item 1 & 2 are the same
			game_frame[i][h+1] = game_frame[i][h+1]+game_frame[i][h] #add item 3 & 4
			points += game_frame[i][h+1] **2 #add equal tiles
			game_frame[i][h] = 0 #set item 1 in row as zero/empty

			#---------------------------------------------#

while True:
	print "Your Score is: "
	print str(score)
	print "\n\n"
	print game_frame[0][0], "\t", game_frame[0][1], "\t", game_frame[0][2], "\t", game_frame[0][3], "\n"
	print game_frame[1][0], "\t", game_frame[1][1], "\t", game_frame[1][2], "\t", game_frame[0][3], "\n"
	print game_frame[2][0], "\t", game_frame[2][1], "\t", game_frame[2][2], "\t", game_frame[2][3], "\n"
	print game_frame[3][0], "\t", game_frame[3][1], "\t", game_frame[3][2], "\t", game_frame[3][3], "\n"
	move_next = raw_input("Please choose your move: ")
	
	if move_next == "a":
		up(game_frame)
		up_sum(game_frame)

	elif move_next == "s":
		down(game_frame)
		down_sum(game_frame)

	elif move_next == "d":
		left(game_frame)
		left_sum(game_frame)

	elif move_next == "f":
		right(game_frame)
		right_sum(game_frame)

	else:
		attempt_num += 1
		continue

	row_with_zero = []
	column_with_zero = []
	for i in range(0,4):
		if game_frame[i][h] == 0:
			row_with_zero.append(i)
			column_with_zero.append(h)

		if game_frame[i][h] == 2048:
			print "WE HAVE A WINNER!!!"
			break

		if len(row_with_zero) >1:
			random_index = row_with_zero.index(random.choice(row_with_zero))
			row_entry = row_with_zero[random_index]
			column_entry = column_with_zero[random_index]
			game_frame[row_entry][column_entry] = 2

		elif len(row_with_zero) == 1:
			row_entry = row_with_zero[0]
			column_entry = column_with_zero[0]
			game_frame[row_entry][column_entry] = 2

		else:
			break

	print "CONGRATS!!! Score: ", str(score), "score"
	print "\n\n"
	print "Number of tries: ", str(attempt_num)