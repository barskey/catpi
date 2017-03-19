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
	'Tank En.':    {'type': 'set', 'active': False, 'pin': '12'},
	'Been En.':    {'type': 'set', 'active': False, 'pin': '13'},
	'Chopper En.': {'type': 'set', 'active': False, 'pin': '14'},
	'Tank Fire':   {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b10000000},
	'Hi Expl.':    {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b01000000},
	'Jeep Fire':   {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b00100000},
	'Lo Expl.':    {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b00010000},
	'Tank Speed':  {'type': 'clk', 'reg': 1,  'active': True,  'pin': 0b00001111}
}

#// Rip Off
ROInit = {'len': 17,
	'11': '01111111000000000',
	'12': '00101010010101000',
	'13': '00000000000000010',
	'14': '11111111111111111',
	'15': '11111111111111111',
	'16': '11111111111111111'
}
ROSounds = {
	'Explsn':   {'type': 'set', 'active': False, 'pin': '16'},
	'Laser':    {'type': 'set', 'active': False, 'pin': '15'},
	'Torpedo':  {'type': 'set', 'active': False, 'pin': '14'},
	'BG Speed': {'type': 'clk', 'reg': 1,  'active': True, 'pin': 0b111000},
	'BG En.':   {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b000100},
	'Beep':     {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b000010},
	'Motor':    {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b000001}
}

#// Solar Quest
SQInit = {'len': 59,
	'11': '11111111111111111111110000000000000000000000000000000000010',
	'12': '00000000000000000000100000000000000000000000000000000000000',
	'13': '00000000000000000000000000000000000000000000000000000000000',
	'14': '11111111111111111111111111111111111111111111111111111111111',
	'15': '01001001001010101010000101010101010101010101010010101001000',
	'16': '00011100011111111111110000000000000000000000000111111100000'
}
SQSounds = {
	'Loud Explsn':  {'type': 'clk', 'reg': 1, 'active': False, 'pin': 0b10000000},
	'Soft Explsn':  {'type': 'clk', 'reg': 1, 'active': False, 'pin': 0b01000000},
	'Thrust':       {'type': 'clk', 'reg': 1, 'active': False, 'pin': 0b00100000},
	'Fire':         {'type': 'clk', 'reg': 1, 'active': False, 'pin': 0b00010000},
	'Capture':      {'type': 'clk', 'reg': 1, 'active': False, 'pin': 0b00001000},
	'Nuke':         {'type': 'clk', 'reg': 1, 'active': True , 'pin': 0b00000100},
	'Photon':       {'type': 'clk', 'reg': 1, 'active': False, 'pin': 0b00000010},
	'Music En.':    {'type': 'clk', 'reg': 2, 'active': True,  'pin': 0b1000000000000000},
	'Music Vol':    {'type': 'clk', 'reg': 2, 'active': False, 'pin': 0b0111000000000000},
	'Music Pitch':  {'type': 'clk', 'reg': 2, 'active': True,  'pin': 0b0000111111111111}
}

#// Space War
SWInit = {'len': 1,
	'11': '0',
	'12': '0',
	'13': '1',
	'14': '1',
	'15': '1',
	'16': '1'
}
SWSounds = {
	'Explsn':    {'type': 'set', 'active': True, 'pin': '11'},
	'Fire':      {'type': 'set', 'active': True, 'pin': '12'},
	'Thrust 1':  {'type': 'set', 'active': False, 'pin': '13'},
	'Thrust 2':  {'type': 'set', 'active': False, 'pin': '14'}, # TODO need to also set Thrust 1 to on?
	'Sound En.': {'type': 'set', 'active': False, 'pin': '15'}
}

#// Star Castle
SCInit = {'len': 23,
	'11': '00000000000000000000010',
	'12': '11111111111111111111111',
	'13': '11111111111111111111111',
	'14': '11111111111111111111111',
	'15': '00101010010100100101000',
	'16': '10000000111110001111111'
}
SCSounds = {
	'Loud Explsn':   {'type': 'set', 'active': False, 'pin': '12'}, # TODO Should be pulse?
	'Soft Explsn':   {'type': 'set', 'active': False, 'pin': '13'}, # TODO Should be pulse?
	'Laser En.':     {'type': 'set', 'active': False, 'pin': '14'},
	'Fireball En.':  {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b10000000},
	'Shield En.':    {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b01000000},
	'Star En.':      {'type': 'clk', 'reg': 1,  'active': True,  'pin': 0b00100000},
	'Thrust En.':    {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b00010000},
	'BG En.':        {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b00001000},
	'BG Speed':      {'type': 'clk', 'reg': 1,  'active': True,  'pin': 0b00000111}
}

#// Star Hawk
SHInit = {'len': 1,
	'11': '0',
	'12': '0',
	'13': '0',
	'14': '1',
	'15': '1',
	'16': '0'
}
SHSounds = {
	'Explosion':     {'type': 'set', 'active': True,  'pin': '11'}, # TODO Should be pulse?
	'Laser 1':       {'type': 'set', 'active': True,  'pin': '12'}, # TODO Should be pulse?
	'Laser 2':       {'type': 'set', 'active': True,  'pin': '13'},
	'K On/Off':      {'type': 'set', 'active': False, 'pin': '14'}, # TODO also sets 15 low?
	'Master On/Off': {'type': 'set', 'active': False, 'pin': '15'},
	'K Exit':        {'type': 'set', 'active': True,  'pin': '16'} # TODO also sets 14 low and 15 low?
}

#// Sundance
SDInit = {'len': 1,
	'11': '1',
	'12': '1',
	'13': '1',
	'14': '1',
	'15': '1',
	'16': '1'
}
SDSounds = {
	'Bong':   {'type': 'set', 'active': False,  'pin': '11'}, # TODO Should be pulse?
	'Whoosh': {'type': 'set', 'active': False,  'pin': '12'}, # TODO Should be pulse?
	'Explsn': {'type': 'set', 'active': False,  'pin': '13'}, # TODO Should be pulse?
	'Ping 1': {'type': 'set', 'active': False,  'pin': '14'}, # TODO Should be pulse?
	'Ping 2': {'type': 'set', 'active': False,  'pin': '15'}, # TODO Should be pulse?
	'Hatch':  {'type': 'set', 'active': False,  'pin': '16'} # TODO Should be pulse? Needs pause?
}

#// Tailgunner
TGInit = {'len': 13,
	'11': '0000000000000',
	'12': '0000000000000',
	'13': '0000000000000',
	'14': '1111111111111',
	'15': '1010101010101',
	'16': '1111111111111'
}
TGSounds = {
	'Explsn':        {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b100000},
	'Rumble':        {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b010000},
	'Laser':         {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b000010},
	'Shield':        {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b001000},
	'Shield Bounce': {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b000001},
	'Hyperspace':    {'type': 'clk', 'reg': 1,  'active': False, 'pin': 0b000100}
}
#TGSounds = [
#	[ 'Explsn',     'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 0],
#	[ 'Rumble',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 1],
#	[ 'Laser',         'ACT_TGR',  4, 'ST_TGS', 0x0001, 0x0001, 2],
#	[ 'Shield',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 3],
#	[ 'Shield Bounce', 'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 4],
#	[ 'Hyperspace',    'ACT_PLS', 34, 'ST_TGS', 0x0001, 0x0001, 5],
#]

GameBoards = {
	'Armor Attack': {'sounds': AASounds, 'latchpin': '11', 'clkpin': '15', 'datapin': '16'},
	'Rip Off':      {'sounds': ROSounds, 'latchpin': '13', 'clkpin': '12', 'datapin': '11'},
	'Solar Quest':  {'sounds': SQSounds, 'latchpin': '12', 'clkpin': '15', 'datapin': '16'},
	'Space Wars':   {'sounds': SWSounds, 'latchpin': None, 'clkpin': None, 'datapin': None},
	'Star Castle':  {'sounds': SCSounds, 'latchpin': '11', 'clkpin': '15', 'datapin': '16'},
	'Star Hawk':    {'sounds': SHSounds, 'latchpin': None, 'clkpin': None, 'datapin': None},
	'Sundance':     {'sounds': SDSounds, 'latchpin': None, 'clkpin': None, 'datapin': None},
	'Tailgunner':   {'sounds': TGSounds, 'latchpin': None, 'clkpin': '15', 'datapin': '14'}
}

class GameBoard():

	def __init__(self):
		self.Boards = GameBoards
