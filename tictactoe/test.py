board = {'a1':'x','a2':'_','a3':'_','b1':'_','b2':'_','b3':'_','c1':' ','c2':' ','c3':' '}


def o_move():
	print 'im over at o now'
	
	

def x_move():
	
	ans = raw_input('Player x please Enter a location: ') #ask user for location
	f = board[ans] #current value of dictionary location selected

	while f is '_' or f is ' ':
		board[ans] == 'x' #writes the user location selected to the dictionary
		o_move() #everything was good, move on
		break #break the loop 
	else:
		
		print 'space not available Try again'	
		ans = raw_input('Player x please Enter a location: ') #ask again
		
		
		
board = {'a1':'x','a2':'_','a3':'_','b1':'_','b2':'_','b3':'_','c1':' ','c2':' ','c3':' '}


def o_move():
	print 'im over at o now'
	
	

def x_move():
	
	ans = raw_input('Player x please Enter a location: ') #ask user for location
	f = board[ans] #current value of dictionary location selected

	while f is '_' or f is ' ':
		board[ans] == 'x' #writes the user location selected to the dictionary
		o_move() #everything was good, move on
		break #break the loop 
	else:
		
		print 'space not available Try again'	
		x_move()
		
		
		
x_move()
	
	
	
#if I enter a1 as my location I should get an error because it is not true 
#because I put an x in the 'a1' dictionary
	
	



			
	