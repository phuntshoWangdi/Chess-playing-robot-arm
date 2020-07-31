import os
import cv2
import numpy as np
from time import sleep
from PIL import ImageGrab





filenames = [filename for filename in os.listdir("./template/") if '.jpg' in filename]

delay = 0.7
"""
positions = [

['g1 x75 y31 z-35',   'g1 x65 y35 z-35'    'g1 x58 y42 z-35',   'g1 x51 y48 z-35',   'g1 x45 y54 z-35',   'g1 x38 y59 z-35',   'g1 x34 y67 z-35',   'g1 x29 y78 z-35'],
['g1 x89 y42 z-35',   'g1 x80 y48 z-45',   'g1 x72 y54 z-45',   'g1 x64 y61 z-45',   'g1 x58 y67 z-35',   'g1 x49 y73 z-35',   'g1 x45 y82 z-35',   'g1 x37 y89 z-35'],
['g1 x102 y53 z-35',  'g1 x91 y60 z-35',   'g1 x84 y65 z-35',   'g1 x76 y71 z-35',   'g1 x69 y79 z-35',   'g1 x61 y87 z-35',   'g1 x55 y95 z-35',   'g1 x47 y105 z-35'],
['g1 x115 y64 z-35',  'g1 x105 y71 z--35', 'g1 x96 y77 z-35',   'g1 x89 y85 z-35',   'g1 x81 y91 z-35',   'g1 x74 y101 z-35',  'g1 x68 y112 z-35',  'g1 x58 y122 z-35'],
['g1 x131 y79 z-35',  'g1 x121 y85 z--35', 'g1 x112 y91 z-35',  'g1 x100 y100 z35',  'g1 x96 y108 z-35',  'g1 x85 y115 z-35',  'g1 x78 y125 z-35',  'g1 x68 y135 z-35'],
['g1 x141 y88 z--35', 'g1 x132 y95 z--35', 'g1 x124 y105 z-35', 'g1 x113 y111 z-35', 'g1 x105 y120 z-35', 'g1 x98 y130 z-35',  'g1 x90 y140 z-35',  'g1 x80 y145 z-35'],
['g1 x149 y97 z-40',  'g1 x140 y105 z-40', 'g1 x132 y111 z-35', 'g1 x121 y119 z-35', 'g1 x114 y129 z-35', 'g1 x109 y139 z-35', 'g1 x98 y150 z-35',  'g1 x90 y160 z-35'],
['g1 x164 y108 z-40', 'g1 x153 y116 z-37', 'g1 x143 y125 z-35', 'g1 x133 y132 z-35', 'g1 x125 y140 z-35', 'g1 x116 y149 z-35', 'g1 x107 y159 z-35', 'g1 x101 y171 z-35']

]
"""


positions = [
#        0                    1                    2                   3                    4                    5                    6                      7
['g1 x75 y31 z-0',    'g1 x67 y38 z-0',    'g1 x58 y42 z-0',    'g1 x56 y50 z-0',    'g1 x48 y54 z-0',    'g1 x38 y59 z-0',    'g1 x34 y67 z-0',    'g1 x29 y78 z-0'],
#        1
['g1 x89 y42 z-35',   'g1 x80 y48 z-45',   'g1 x72 y54 z-45',   'g1 x64 y61 z-45',   'g1 x58 y67 z-35',   'g1 x49 y73 z-35',   'g1 x45 y82 z-35',   'g1 x37 y89 z-35'],
#        2
['g1 x102 y53 z-35',  'g1 x93 y60 z-35',   'g1 x84 y65 z-35',   'g1 x76 y71 z-35',   'g1 x69 y79 z-35',   'g1 x61 y87 z-35',   'g1 x55 y95 z-35',   'g1 x47 y105 z-35'],
#        3
['g1 x115 y64 z-35',  'g1 x105 y71 z-35',  'g1 x96 y77 z-35',   'g1 x89 y85 z-35',   'g1 x81 y91 z-35',   'g1 x74 y101 z-35',  'g1 x68 y112 z-35',  'g1 x58 y122 z-35'],
#        4
['g1 x131 y79 z-35',  'g1 x121 y85 z-35',  'g1 x112 y91 z-35',  'g1 x100 y100 z-35',  'g1 x96 y108 z-35',  'g1 x85 y115 z-35',  'g1 x78 y125 z-35',  'g1 x68 y135 z-35'],
#        5
['g1 x141 y88 z-35',  'g1 x132 y95 z-35',  'g1 x124 y105 z-35', 'g1 x113 y111 z-35', 'g1 x105 y120 z-35', 'g1 x98 y130 z-35',  'g1 x90 y140 z-35',  'g1 x80 y145 z-35'], #5
#        6
['g1 x149 y97 z-30',  'g1 x140 y105 z-35', 'g1 x132 y111 z-35', 'g1 x121 y119 z-35', 'g1 x114 y129 z-35', 'g1 x109 y139 z-35', 'g1 x98 y150 z-35',  'g1 x90 y160 z-35'],
#        7
['g1 x164 y108 z-35', 'g1 x153 y116 z-35', 'g1 x143 y125 z-35', 'g1 x133 y132 z-35', 'g1 x125 y140 z-35', 'g1 x116 y149 z-35', 'g1 x107 y159 z-35', 'g1 x101 y171 z-35']

]

relative_pos = [
    #0   #1  #2  #3  #4  #5  #6  #7
	[53, 53, 53, 53, 53, 52, 53, 53], #0
	[54, 53, 53, 53, 52, 53, 54, 54], #1
	[55, 55, 54, 54, 54, 54, 54, 54], #2
	[56, 55, 55, 55, 55, 55, 55, 56], #3
	[56, 56, 56, 56, 56, 56, 56, 56], #4
	[57, 57, 57, 57, 57, 57, 57, 57], #5
	[58, 58, 58, 58, 58, 58, 58, 58], #6
	[59, 58, 58, 58, 58, 58, 58, 59]  #7
]



rowTranslation = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7}
columnTranslation = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

def algrebraicNotation2Arraypostions(notation) -> tuple:

	src = notation[:2]  #column row
	dest = notation[2:4]

	srcColumn = columnTranslation[src[0]]
	srcRow = rowTranslation[int(src[1])]


	destColumn = columnTranslation[dest[0]]
	destRow = rowTranslation[int(dest[1])]

	return srcRow, srcColumn, destRow, destColumn


def _printBoard(bcfg) -> None:
	print(*bcfg[:8],    sep=" ")
	print(*bcfg[8:16],  sep=" ")
	print(*bcfg[16:24], sep=" ")
	print(*bcfg[24:32], sep=" ")
	print(*bcfg[32:40], sep=" ")
	print(*bcfg[40:48], sep=" ")
	print(*bcfg[48:56], sep=" ")
	print(*bcfg[56:64], sep=" ")


def MoveIt(startPosition, endPosition, sR, sC, dR, dC, portToArduino) -> None:

	for i, pos in enumerate([startPosition,endPosition]):
		if i == 0:
			Row = sR
			Col = sC
		elif i == 1:
			Row = dR
			Col = dC

		sleep(delay)
		#From Start Position
		cmd = pos
		cmd_temp = cmd[:]
		cmd = cmd.encode('utf-8')
		portToArduino.write(cmd)
		
		print(f'CMD: {cmd}')
		sleep(delay)

		#drop down
		new_cmd = ''

		for char in cmd_temp:
			if char == 'z':
				break
			new_cmd = new_cmd + char
		
		new_cmd = new_cmd+'z-'+str(relative_pos[Row][Col])+'\n'
		new_cmd = new_cmd.encode('utf-8')
		portToArduino.write(new_cmd)

		print(f'NEW CMD: {new_cmd}')

		#pull up
		portToArduino.write(cmd)

		print(f'CMD: {cmd}')
		sleep(delay)
		print('---------------------------------------')

	#return back to home position
	new_cmd = 'endstop\n'
	new_cmd =  new_cmd.encode('utf-8')
	portToArduino.write(new_cmd)


def formatString(string) -> str:
    n = {}
    string = [s for s in string]
    newString_list = string[:]

    i = 0
    while i<len(string):

        if string[i] == '.':
            count = 1
            
            for j in range(i+1, len(string)):
                if string[j] == '.':
                    count+=1
                else:                    
                    n[i] = count
                    i += count
                    break
        else:
            i+=1
    for key in n:
        newString_list[key] = str(n[key])
    
    
    newString_list = [s for s in newString_list if s != '.']
    
    formated_string = ''
    for c in newString_list:
        formated_string+=c

    return formated_string


def boardConfiguration() -> str:

	pil_img = ImageGrab.grab(bbox=(220,350,740,870)) #520x520

	image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

	cropped_images = [

	image[0:60,    0:63], image[0:60,   65:129],  image[0:60,    130:194], image[0:60,    195:259], image[0:60,    260:324], image[0:60,    326:390], image[0:60,    392:456], image[0:60,    457:521],
	image[61:125,  0:63], image[61:125, 65:129],  image[61:125,  130:194], image[61:125,  195:256], image[61:125,  260:324], image[61:125,  326:390], image[61:125,  392:456], image[61:125,  457:521],
	image[126:189, 0:63], image[126:189, 65:129], image[126:189, 130:194], image[126:189, 195:256], image[126:189, 260:324], image[126:189, 326:390], image[126:189, 392:456], image[126:189, 457:521],
	image[191:258, 0:63], image[191:258, 65:129], image[191:258, 130:194], image[191:258, 195:256], image[191:258, 261:324], image[191:258, 326:390], image[191:258, 392:456], image[191:258, 457:521],
	image[259:322, 0:63], image[259:322, 65:129], image[259:322, 130:194], image[259:322, 195:256], image[259:322, 261:324], image[259:322, 326:390], image[259:322, 392:456], image[259:322, 457:521],
	image[323:386, 0:63], image[323:386, 65:129], image[323:386, 130:194], image[323:386, 195:256], image[323:386, 261:324], image[323:386, 326:390], image[323:386, 392:456], image[323:386, 457:521],
	image[389:450, 0:63], image[387:450, 65:129], image[387:450, 130:194], image[387:450, 195:256], image[387:450, 261:324], image[387:450, 326:390], image[387:450, 392:456], image[387:450, 457:521],
	image[454:514, 0:63], image[454:517, 63:129], image[454:514, 130:194], image[454:514, 195:256], image[454:514, 261:324], image[454:514, 326:390], image[454:514, 392:456], image[454:514, 457:521],

		  ]

	board_config = ['.']*64

	for i in range(len(cropped_images)):
		for filename in filenames:
			
			template_img = cv2.imread('./template/'+filename)
			comparison_result = cv2.matchTemplate(cropped_images[i], template_img, cv2.TM_CCOEFF_NORMED)


			if np.amax(comparison_result) >= 0.65:
				
				if filename[:2] == 'bb':
					board_config[i] = 'b'
				
				elif filename[:2] == 'bk':
					board_config[i] ='k'

				elif filename[:2] == 'bn':
					board_config[i] ='n'

				elif filename[:2] == 'bp':
					board_config[i] ='p'

				elif filename[:2] == 'bq':
					board_config[i] ='q'

				elif filename[:2] == 'br':
					board_config[i] ='r'

				elif filename[:2] == 'wb':
					board_config[i] = 'B'
				
				elif filename[:2] == 'wk':
					board_config[i] ='K'

				elif filename[:2] == 'wn':
					board_config[i] ='N'

				elif filename[:2] == 'wp':
					board_config[i] ='P'

				elif filename[:2] == 'wq':
					board_config[i] ='Q'

				elif filename[:2] == 'wr':
					board_config[i] ='R'

				elif filename[:2] == 'b_' or filename[:2] == 'w_':
					board_config[i] = '.'
	
	_printBoard(board_config)
	board_config.insert(8,'/')
	board_config.insert(17,'/')
	board_config.insert(26,'/')
	board_config.insert(35,'/')
	board_config.insert(44,'/')
	board_config.insert(53,'/')
	board_config.insert(62,'/')
	board_config = board_config

	fString = ''
	for c in board_config:
		fString+=c 
	fString = fString + ' w'

	return formatString(fString)
