''' 
Board layout reference

    1   2   3
a  ___|___|___
b  ___|___|___
c     |   |  
 
'''

board = {'a1':'_','a2':'_','a3':'_','b1':'_','b2':'_','b3':'_','c1':' ','c2':' ','c3':' '}
open_positions = ['_', ' ']

	
def play_again():
	a = raw_input('Game over!. Would you like to play again. type y or n: ')
	if a == 'y':
		#fix board back to original
		reset()
		start()
	elif a == 'n':
		quit()
	else:
		pass
		
def reset():
	board['a1'] = '_'
	board['a2'] = '_'
	board['a3'] = '_'
	board['b1'] = '_'
	board['b2'] = '_'
	board['b3'] = '_'
	board['c1'] = ' '
	board['c2'] = ' '
	board['c3'] = ' '
	

def prt_board():
    #This is the main layout which gets the positions from variable board above.
    print '\n    1   2   3\na  _%s_|_%s_|_%s_\nb  _%s_|_%s_|_%s_\nc   %s | %s | %s \n\n' % (
        board['a1'],board['a2'],board['a3'],
        board['b1'],board['b2'],board['b3'],
        board['c1'],board['c2'],board['c3'])

def x_move():
	ans = raw_input('Player x please Enter a location: ')
	
	if ans in board.keys():
		if board[ans] in open_positions:
			board[ans] = 'x'
			prt_board()
			chk()
			o_move()
		else:
			print 'That space is already taken. Try again-'
			x_move()
	else:
		print 'It looks like you entered an invaild location. Try again-'
		x_move()
			
	
    
def o_move():
	ans = raw_input('Player o please Enter a location: ')
	
	if ans in board.keys():
		if board[ans] in open_positions:
			board[ans] = 'o'
			prt_board()
			chk()
			x_move()
		else:
			print 'That space is already taken. Try again-'
			x_move()
	else:
		print 'It looks like you entered an invaild location. Try again-'
		o_move()
			
	
def chk():
	if board[
	'a1'] == 'x' and board['a2'] == 'x' and board['a3'] == 'x' or board[
	'b1'] == 'x' and board['b2'] == 'x' and board['b3'] == 'x' or board[
	'c1'] == 'x' and board['c2'] == 'x' and board['c3'] == 'x' or board[
	'a1'] == 'x' and board['b1'] == 'x' and board['c1'] == 'x' or board[
	'a2'] == 'x' and board['b2'] == 'x' and board['c2'] == 'x' or board[
	'a3'] == 'x' and board['b3'] == 'x' and board['c3'] == 'x' or board[
	'a1'] == 'x' and board['b2'] == 'x' and board['c3'] == 'x' or board[
	'a3'] == 'x' and board['b2'] == 'x' and board['c1'] == 'x':
		prt_board()
		print 'X Wins!!!!!!!!!!!!!'
		play_again()

	elif board[
	'a1'] == 'o' and board['a2'] == 'o' and board['a3'] == 'o' or board[
	'b1'] == 'o' and board['b2'] == 'o' and board['b3'] == 'o' or board[
	'c1'] == 'o' and board['c2'] == 'o' and board['c3'] == 'o' or board[
	'a1'] == 'o' and board['b1'] == 'o' and board['c1'] == 'o' or board[
	'a2'] == 'o' and board['b2'] == 'o' and board['c2'] == 'o' or board[
	'a3'] == 'o' and board['b3'] == 'o' and board['c3'] == 'o' or board[
	'a1'] == 'o' and board['b2'] == 'o' and board['c3'] == 'o' or board[
	'a3'] == 'o' and board['b2'] == 'o' and board['c1'] == 'o':
		prt_board()
		print 'O Wins!!!!!!!!!!!!!'
		play_again()



	elif board[
	'a1'] != '_' and board['a2'] != '_' and board['a3'] != '_' and board[
	'b1'] != '_' and board['b2'] != '_' and board['b3'] != '_' and board[
	'c1'] != ' ' and board['c2'] != ' ' and board['c3'] != ' ':
		prt_board()
		print 'Game ended in a Tie!'
		play_again()
	
	else:
		pass
   

def start():   
	who = raw_input('Which player will be going first? type x or o: ')

	if who == 'x':
		prt_board()
		x_move()
		
		
	elif who == 'o':
		prt_board()
		o_move()
		
		
start()

     