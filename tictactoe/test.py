board = {'a1':'x','a2':'_','a3':'_','b1':'_','b2':'_','b3':'_','c1':' ','c2':' ','c3':' '}


def o_move():
	print 'im over at o now'
	



def x_move():

	while True:
		try:
			ans = raw_input('Player x please Enter a location: ') #ask user for location
			f = board[ans] #current value of location selected
			f == '_' or ' ' #checks to see if current location has a '_' or a ' ' which is considered free space and we can write to it
			
		
		except:
			print 'That space is already taken'
			ans = raw_input('Try again-Player x please Enter a location: ')
		else:
			board[ans] == 'x' #writes the user location to the dictionary
			print 'put an x'  #confirms write
			o_move()
		
x_move()
	
	
	
	
	



			
	