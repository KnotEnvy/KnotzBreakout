WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720

BLOCK_MAP = [
    '633655556336',
    '511441144115',
    '331111331133',
    '212112222211',
    '111111111111',
    '            ',
    '            ',
    '            ',
    '            '
]

COLOR_LEGEND = {
	'1': 'blue',
	'2': 'green',
	'3': 'red',
	'4': 'orange',
	'5': 'purple',
	'6': 'bronce',
	'7': 'grey',
}

GAP_SIZE = 2
BLOCK_HEIGHT = WINDOW_HEIGHT / len(BLOCK_MAP) - GAP_SIZE #hieght of individual block scalable
BLOCK_WIDTH = WINDOW_WIDTH / len(BLOCK_MAP[0]) - GAP_SIZE
