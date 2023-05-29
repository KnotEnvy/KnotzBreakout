WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720

BLOCK_MAP = [
    '777766515777',
    '444455515444',
    '333351515333',
    '555551515555',
    '222251115222',
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
