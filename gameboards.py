#// Armor Attack
AAInit = {'len': 17,
	'11': '01111111000000000',
	'12': '00101010010101000',
	'13': '00000000000000100',
	'14': '11111111111111111',
	'15': '11111111111111111',
	'16': '11111111111111111'
}
AASounds = {
	'Tank En.': {'len': 8,
		'11': '01010101',
		'12': '10101010',
		'13': '01010101'
	},
	'Been En.': {'len': 1,
		'15': '0'
	}
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
SWSounds = [
	[ 'Explosion',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Fire',         'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Thrust 1',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Thrust 2',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Sound En.', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4]
]

#// Star Castle
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
SHSounds = [
	[ 'Explosion',     'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Laser 1',       'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Laser 2',       'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0000, 2],
	[ 'K On/Off',      'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Master On/Off', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'K Exit',        'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0000, 7]
]

#// Sundance
SDSounds = [
	[ 'Bong',      'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 0],
	[ 'Whoosh',    'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Explsn', 'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Ping 1',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Ping 2',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Hatch',     'ACT_PLS', 6, 'ST_OUT', 0x0001, 0x0001, 7]
];

#// Tailgunner
TGSounds = [
	[ 'Explsn',     'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 0],
	[ 'Rumble',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 1],
	[ 'Laser',         'ACT_TGR',  4, 'ST_TGS', 0x0001, 0x0001, 2],
	[ 'Shield',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 3],
	[ 'Shield Bounce', 'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 4],
	[ 'Hyperspace',    'ACT_PLS', 34, 'ST_TGS', 0x0001, 0x0001, 5],
]

SoundBoard = [
	[ 'Armor Attack', len(AASounds), AASounds],
	[ 'Rip Off',      len(ROSounds), ROSounds],
	[ 'Solar Quest',  len(SQSounds), SQSounds],
	[ 'Space Wars', len(SWSounds), SWSounds],
	[ 'Star Castle',  len(SCSounds), SCSounds],
	[ 'Star Hawk',    len(SHSounds), SHSounds],
	[ 'Sundance',     len(SDSounds), SDSounds],
	[ 'Tailgunner',   len(TGSounds), TGSounds]
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
		

