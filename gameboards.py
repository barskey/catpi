#// Armor Attack
AAInit = {'len': 20,
	'11': '00000000000000000010',
	'12': '11111111111111111111',
	'13': '11111111111111111111',
	'14': '11111111111111111111',
	'15': '01010101001010101000',
	'16': '00000000011111111111'
}
AASounds = {
	'Tank En.': {'len': 1,
		'12': '0',
		'13': '1',
		'14': '1'
	},
	'Been En.': {'len': 1,
		'12': '0',
		'13': '0',
		'14': '1'
	},
	'Chopper En.': {'len': 1,
		'12': '0',
		'13': '0',
		'14': '0'
	},
	'Hi Expl.': {'len': 42,
		'11': '000000000000000000010000000000000000000010',
		'15': '010101010010101001000001010101001010101000',
		'16': '0000000001111111000000000000000ßß11111111111'
	},
}
#AASounds = [
#	[ 'Tank En.',    'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 1],
#	[ 'Beep En.',    'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
#	[ 'Chopper En.', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
#	[ 'Tank Fire',      'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 7],
#	[ 'Hi Explosion',   'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 6],
#	[ 'Jeep Fire',      'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 5],
#	[ 'Lo Explosion',   'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 4],
#	[ 'Tank Speed',     'ACT_SET', 0, 'ST_AAS', 0x000F, 0x0000, 0]
#]
#// Rip Off
ROInit = {'len': 17,
	'11': '01111111000000000',
	'12': '00101010010101000',
	'13': '00000000000000010',
	'14': '11111111111111111',
	'15': '11111111111111111',
	'16': '11111111111111111'
}
ROSounds = [
	[ 'Explsn',         'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 7],
	[ 'Laser',             'ACT_PLS', 4, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Torpedo',           'ACT_PLS', 3, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'BG Speed',  'ACT_SET', 0, 'ST_ROS', 0x0007, 0x0000, 3],
	[ 'BG En.', 'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 2],
	[ 'Beep',              'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 1],
	[ 'Motor',             'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 0]
]

#// Solar Quest
SQInit = {'len': 59,
	'11': '11111111111111111111110000000000000000000000000000000000010',
	'12': '00000000000000000000100000000000000000000000000000000000000',
	'13': '00000000000000000000000000000000000000000000000000000000000',
	'14': '11111111111111111111111111111111111111111111111111111111111',
	'15': '01001001001010101010000101010101010101010101010010101001000',
	'16': '00011100011111111111110000000000000000000000000111111100000'
}
SQSounds = [
	[ 'Loud Explsn', 'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  7],
	[ 'Soft Explsn', 'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  6],
	[ 'Thrust',         'ACT_TGL', 0, 'ST_SQ1', 0x0001, 0x0001,  5],
	[ 'Fire',           'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  4],
	[ 'Capture',        'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  3],
	[ 'Nuke',           'ACT_TGL', 0, 'ST_SQ1', 0x0001, 0x0000,  2],
	[ 'Photon',         'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  1],
	[ 'Music En.',   'ACT_TGL', 0, 'ST_SQ2', 0x0001, 0x0000, 15],
	[ 'Music Vol',   'ACT_SET', 0, 'ST_SQ2', 0x0007, 0x0007, 12],
	[ 'Music Pitch',    'ACT_SET', 0, 'ST_SQ2', 0x0FFF, 0x0000,  0]
]

#// Space War
SWInit = {'len': 1,
	'11': '0',
	'12': '0',
	'13': '1',
	'14': '1',
	'15': '1',
	'16': '1'
}
SWSounds = [
	[ 'Explosion',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Fire',         'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Thrust 1',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Thrust 2',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Sound En.', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4]
]

#// Star Castle
SCInit = {'len': 23,
	'11': '00000000000000000000010',
	'12': '11111111111111111111111',
	'13': '11111111111111111111111',
	'14': '11111111111111111111111',
	'15': '00101010010100100101000',
	'16': '10000000111110001111111'
}
SCSounds = [
	[ 'Loud Explsn',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Soft Explsn',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Laser En.',      'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Fire Ball En.',  'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 7],
	[ 'Shield En.',     'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 6],
	[ 'Star En.',       'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0000, 5],
	[ 'Thrust En.',     'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 4],
	[ 'BG En.', 'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 3],
	[ 'BG Speed',  'ACT_SET', 0, 'ST_AAS', 0x0007, 0x0000, 0]
]

#// Star Hawk
SHInit = {'len': 1,
	'11': '0',
	'12': '0',
	'13': '0',
	'14': '1',
	'15': '1',
	'16': '0'
}
SHSounds = [
	[ 'Explosion',     'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Laser 1',       'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Laser 2',       'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0000, 2],
	[ 'K On/Off',      'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Master On/Off', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'K Exit',        'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0000, 7]
]

#// Sundance
SDInit = {'len': 1,
	'11': '1',
	'12': '1',
	'13': '1',
	'14': '1',
	'15': '1',
	'16': '1'
}
SDSounds = [
	[ 'Bong',      'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 0],
	[ 'Whoosh',    'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Explsn', 'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Ping 1',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Ping 2',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Hatch',     'ACT_PLS', 6, 'ST_OUT', 0x0001, 0x0001, 7]
];

#// Tailgunner
TGInit = {'len': 13,
	'11': '0000000000000',
	'12': '0000000000000',
	'13': '0000000000000',
	'14': '1111111111111',
	'15': '1010101010101',
	'16': '1111111111111'
}
TGSounds = [
	[ 'Explsn',     'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 0],
	[ 'Rumble',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 1],
	[ 'Laser',         'ACT_TGR',  4, 'ST_TGS', 0x0001, 0x0001, 2],
	[ 'Shield',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 3],
	[ 'Shield Bounce', 'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 4],
	[ 'Hyperspace',    'ACT_PLS', 34, 'ST_TGS', 0x0001, 0x0001, 5],
]

GameBoards = {
	'Armor Attack': {'sounds': AASounds, 'init': AAInit},
	'Rip Off': {'sounds': ROSounds, 'init': AAInit},
	'Solar Quest': {'sounds': SQSounds, 'init': AAInit},
	'Space Wars': {'sounds': SWSounds, 'init': AAInit},
	'Star Castle': {'sounds': SCSounds, 'init': AAInit},
	'Star Hawk': {'sounds': SHSounds, 'init': AAInit},
	'Sundance': {'sounds': SDSounds, 'init': AAInit},
	'Tailgunner': {'sounds': TGSounds, 'init': AAInit}
}

class GameBoard():

	def __init__(self):

		self.Boards = GameBoards
