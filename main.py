from utils import boardConfiguration, _printBoard, algrebraicNotation2Arraypostions, positions, MoveIt
from stockfish import Stockfish
from time import sleep
import serial
import chess





#open port for communication with arduino
try:
	portToArduino = serial.Serial('COM7', 9600)
except:
	print('Couldnot open the port')
	exit()

try:
	stockfish = Stockfish("./stockfish-11-win/stockfish-11-win/Windows/stockfish_20011801_x64.exe")
	
except:
	print('Couldnot initialize stockfish')
	exit()

#______________________________________________________#


input('Press enter to continue')
#______________________________________________________#

try:
	while 1:
		repInFEN = boardConfiguration()

		# feed repInFEN to stockfish to get move
		stockfish.set_fen_position(repInFEN)

		board = chess.Board(repInFEN)

		#move = stockfish.get_best_move_time(20)
		move = stockfish.get_best_move()
		print(move)

		#convert move to array positions
		#a2a3 -> (2,0,3,0)
		sRow, sCol, dRow, dCol = algrebraicNotation2Arraypostions(move)
		print(sRow,sCol,dRow,dCol)

		startPosition = positions[sRow][sCol]+'\n'
		endPosition = positions[dRow][dCol]+'\n'

		# send robot arm into action
		MoveIt(startPosition, endPosition, sRow, sCol, dRow, dCol, portToArduino)
		
		input()

except KeyboardInterrupt:
	portToArduino.close()

# print(stockfish.get_board_visual())
#print(f'MOVE: {move}')



