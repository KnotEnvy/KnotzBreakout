WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720

BLOCK_MAP = [
    '222233332222',
    '222222222222',
    '111111111111',
    '111111111111',
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
TOP_OFFSET = WINDOW_HEIGHT // 30

UPGRADES = ['speed', 'laser', 'heart', 'size']
