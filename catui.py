import pygame
import os
import time
import resource
import pygameui as ui
import logging
#import RPi.GPIO as GPIO
import gameboards

# maps the schematic pins(J2 11-16) to GPIO pins
PINS = {
	'11': 22,
	'12': 23,
	'13': 27,
	'14': 17,
	'15': 18,
	'16': 4
}

# time to delay after setting bits
DELAY = 0.001 # 0.001s = 1ms = 1KHz

#Setup the GPIOs as outputs - only 4 and 17 are available
#GPIO.setmode(GPIO.BCM)
#for pin, gpio_port in PINS.items():
#	GPIO.setup(gpio_port, GPIO.OUT)

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

LCD_WIDTH = 480
LCD_HEIGHT = 320
MAXCOLS = 3

GameBoard = gameboards.GameBoard()

class MainMenu(ui.Scene):

	def __init__(self):
		ui.Scene.__init__(self)

		image_view = ui.view_for_image_named('bg', True)
		image_view.frame.right = LCD_WIDTH
		image_view.frame.top = 0
		self.add_child(image_view)

		title_rect = ui.Rect(0, 0, LCD_WIDTH, 60)
		title = ui.Label(title_rect, 'Select A Sound Board:')
		self.add_child(title)

		btn_w = 130
		btn_h = 50
		space = 20
		row = 0
		col = 0
		for game in GameBoard.Boards.iterkeys():
			x = space + col * (btn_w + space)
			y = 75 + row * (btn_h + space)
			btn = ui.Button(ui.Rect(x, y, btn_w, btn_h ), game)
			btn.on_clicked.connect(self.game_btn_clicked)
			self.add_child(btn)
			if col < MAXCOLS - 1:
				col += 1
			else:
				col = 0
				row += 1

	def game_btn_clicked(self, btn, mbtn):
		sm = SoundMenu()
		sm.set_contents(btn.text)
		ui.scene.pop()
		ui.scene.push(sm)

class SoundMenu(ui.Scene):

	def __init__(self):
		ui.Scene.__init__(self)

		image_view = ui.view_for_image_named('bg', True)
		image_view.frame.right = LCD_WIDTH
		image_view.frame.top = 0
		self.add_child(image_view)

	def set_contents(self, selected_game):
		self.selected_game = selected_game

		title_rect = ui.Rect(0, 0, LCD_WIDTH, 40)
		title = ui.Label(title_rect, 'Activate Sound for ' + self.selected_game + ':')
		self.add_child(title)

		btn_w = 130
		btn_h = 40
		space = 15

		btn = ui.Button(ui.Rect(space + 15, 55, btn_w, btn_h), 'Init')
		btn.on_clicked.connect(self.init_board)
		self.add_child(btn)

		row = 0
		col = 1
		for sound in GameBoard.Boards[self.selected_game]['sounds']:
			x = space + 15 + col * (btn_w + space)
			y = 55 + row * (btn_h + space)
			btn = ui.Button(ui.Rect(x, y, btn_w, btn_h), sound)
			btn.on_clicked.connect(self.play_sound)
			self.add_child(btn)
			if col < MAXCOLS - 1:
				col += 1
			else:
				col = 0
				row += 1

		back_btn = ui.Button(ui.Rect(0, LCD_HEIGHT - btn_h, btn_w, btn_h), '<< Back')
		back_btn.on_clicked.connect(self.back_btn_clicked)
		self.add_child(back_btn)

		adv_btn = ui.Button(ui.Rect(LCD_WIDTH - btn_w, LCD_HEIGHT - btn_h, btn_w, btn_h), 'Advanced >')
		adv_btn.on_clicked.connect(self.adv_btn_clicked)
		self.add_child(adv_btn)

	def init_board(self, btn, mbtn):
		ui.show_notification('%s Initialized' % self.selected_game)

		latch_pin = GameBoard.Boards[self.selected_game]['latchpin']
		clk_pin = GameBoard.Boards[self.selected_game]['clkpin']
		data_pin = GameBoard.Boards[self.selected_game]['datapin']

		# loop thru all sounds and set each one that is not clocked
		for name, data in GameBoard.Boards[self.selected_game]['sounds'].items():
			if data['type'] == 'set':
				#GPIO.output(PINS[data['pin']], not data['active'])
				print 'GPIO.output(PINS[%s])' % data['pin'], not data['active']

		# build off register for remaining sounds
		register = self.build_reg_off(GameBoard.Boards[self.selected_game]['sounds'])
		self.send_clk_bits(register, latch_pin, clk_pin, data_pin)

	def play_sound(self, btn, mbtn):
		soundname = btn.text
		ui.show_notification('%s Activated' % soundname)
		sound = GameBoard.Boards[self.selected_game]['sounds'][soundname]

		latch_pin = GameBoard.Boards[self.selected_game]['latchpin']
		clk_pin = GameBoard.Boards[self.selected_game]['clkpin']
		data_pin = GameBoard.Boards[self.selected_game]['datapin']

		soundtype = sound['type']
		if soundtype == 'set': # if sound type is set, only need to set single bit
			#GPIO.output(PINS[sound['pin']], sound['active'])
			print 'GPIO.output(PINS[%s])' % sound['pin'], sound['active']
		else: # else, need to loop through all clocked sounds and make register to load all at once
			register = self.build_reg_off(GameBoard.Boards[self.selected_game]['sounds'])
			print 'Current register:', '{0:b}'.format(register)
			if sound['active']: # if this sound is active high (True)
				register |= sound['pin'] # set this sound to 1 to play
			else:
				register &= ~sound['pin'] # else set it to 0 to play
			print soundname, '{0:b}'.format(register)
			self.send_clk_bits(register, latch_pin, clk_pin, data_pin)

	# Builds a register setting each bit to off as appropriate considering its active state
	def build_reg_off(self, sounds):
		register = 0
		for name, data in sounds.items(): # iterate through each sound
			if data['type'] == 'clk': # only need to look at sounds that are clocked
				bits = data['pin'] # get the bits for this sound
				if not data['active']: # if this sound is active low (False), set this bit to 1 to turn it off
					register |= bits # bitwise OR with register
				print name, '{0:b}'.format(register)

		return register

	# for each bit in register this sets data pin and sends clk pulse, then sends latch at end
	def send_clk_bits(self, register, latch_pin, clk_pin, data_pin):
		# set pins to False to start
		#GPIO.output(PINS[latch_pin], False)
		#GPIO.output(PINS[data_pin], False)
		#GPIO.output(PINS[clk_pin], False) if self.selected_game != 'Tailgunner' else True

		# need to send bits in reverse order
		# TODO need to change 8 to variable size register
		reg_str = '{0:08b}'.format(register)  # store register as string to reverse it
		for bit in reg_str[::-1]: # for each bit in reverse order
			#GPIO.output(PINS[data_pin], bool(int(bit))) # set data pin to this bit
			self.send_pulse(clk_pin) # pulse the clk pin

		if latch_pin:
			self.send_pulse(latch_pin) # latch the register (only if latch_pin is set, e.g. tailgunner has no latch)

	def send_pulse(self, pin):
		#GPIO.output(PINS[pin], True if self.selected_game != 'Tailgunner' else False)
		print PINS[pin], True if self.selected_game != 'Tailgunner' else False
		time.sleep(DELAY)
		#GPIO.output(PINS[pin], False if self.selected_game != 'Tailgunner' else True)
		time.sleep(DELAY)
		print PINS[pin], False if self.selected_game != 'Tailgunner' else True

	def back_btn_clicked(self, btn, mbtn):
		ui.scene.pop()
		ui.scene.push(MainMenu())

	def adv_btn_clicked(self, btn, mbtn):
		am = AdvMenu()
		am.set_contents(self.selected_game)
		ui.scene.pop()
		ui.scene.push(am)

class AdvMenu(ui.Scene):
	toggle_state = {'11': False, '12': False, '13': False, '14': False, '15': False, '16': False}

	def __init__(self):
		ui.Scene.__init__(self)

		image_view = ui.view_for_image_named('bg', True)
		image_view.frame.right = LCD_WIDTH
		image_view.frame.top = 0
		self.add_child(image_view)

		title_rect = ui.Rect(0, 0, LCD_WIDTH, 40)
		title = ui.Label(title_rect, 'Toggle/Pulse pins directly:')
		self.add_child(title)

	def set_contents(self, selected_game):
		self.selected_game = selected_game

		btn_w = 60
		btn_h = 40

		# toggle row
		lbl = ui.Label(ui.Rect(10, 100, 70, btn_h), 'Toggle')
		self.add_child(lbl)
		xvals = [90, 155, 220, 285, 350, 415]
		yval = 100

		self.btn11 = ui.Button(ui.Rect(xvals[0], yval, btn_w, btn_h), '11')
		self.btn11.on_clicked.connect(self.tgl_btn_clicked)
		self.add_child(self.btn11)
		self.btn12 = ui.Button(ui.Rect(xvals[1], yval, btn_w, btn_h), '12')
		self.btn12.state = 'selected'
		self.btn12.on_clicked.connect(self.tgl_btn_clicked)
		self.add_child(self.btn12)
		self.btn13 = ui.Button(ui.Rect(xvals[2], yval, btn_w, btn_h), '13')
		self.btn13.on_clicked.connect(self.tgl_btn_clicked)
		self.add_child(self.btn13)
		self.btn14 = ui.Button(ui.Rect(xvals[3], yval, btn_w, btn_h), '14')
		self.btn14.on_clicked.connect(self.tgl_btn_clicked)
		self.add_child(self.btn14)
		self.btn15 = ui.Button(ui.Rect(xvals[4], yval, btn_w, btn_h), '15')
		self.btn15.on_clicked.connect(self.tgl_btn_clicked)
		self.add_child(self.btn15)
		self.btn16 = ui.Button(ui.Rect(xvals[5], yval, btn_w, btn_h), '16')
		self.btn16.on_clicked.connect(self.tgl_btn_clicked)
		self.add_child(self.btn16)

		# pulse row
		lbl = ui.Label(ui.Rect(10, (100 + btn_h + 30), 70, btn_h), 'Pulse')
		self.add_child(lbl)
		for col in range(6):
			pin = 11 + col
			x = 90 + col * (btn_w + 5)
			y = 100 + (btn_h + 30)

			pls_btn = ui.Button(ui.Rect(x, y, btn_w, btn_h), str(pin))
			pls_btn.on_clicked.connect(self.pls_btn_clicked)
			self.add_child(pls_btn)

		back_btn = ui.Button(ui.Rect(0, LCD_HEIGHT - btn_h, btn_w * 2, btn_h), '<< Back')
		back_btn.on_clicked.connect(self.back_btn_clicked)
		self.add_child(back_btn)

		adv_btn = ui.Button(ui.Rect(LCD_WIDTH - btn_w * 2, LCD_HEIGHT - btn_h, btn_w * 2, btn_h), '< Easy')
		adv_btn.on_clicked.connect(self.adv_btn_clicked)
		self.add_child(adv_btn)

		# set all pins to off (False)
		for pin, state in self.toggle_state.items():
			#GPIO.output(PINS[pin], state)
			pass

	def tgl_btn_clicked(self, btn, mbtn):
		btns = {'11': self.btn11, '12': self.btn12, '13': self.btn13, '14': self.btn14, '15': self.btn15, '16': self.btn16}
		pin = btn.text
		new_state = not self.toggle_state[pin]
		#GPIO.output(PINS[pin], new_state)
		self.toggle_state[pin] = new_state
		btns[pin].state = 'selected'
		btns[pin].stylize()
		logger.info('Toggle:' + btn.text)

	def pls_btn_clicked(self, btn, mbtn):
		pin = btn.text
		#GPIO.output(PINS[pin], True if self.selected_game != 'Tailgunner' else False)
		time.sleep(DELAY)
		#GPIO.output(PINS[pin], False if self.selected_game != 'Tailgunner' else True)
		time.sleep(DELAY)
		logger.info('Pulse:' + btn.text)

	def back_btn_clicked(self, btn, mbtn):
		ui.scene.pop()
		ui.scene.push(MainMenu())

	def adv_btn_clicked(self, btn, mbtn):
		sm = SoundMenu()
		sm.set_contents(self.selected_game)
		ui.scene.pop()
		ui.scene.push(sm)

if __name__ == '__main__':
	clear_color = (0, 0, 0, 0)
	title_color = (85, 128, 255)
	yellow_color = (255, 255, 0)
	shadow_color = (100, 100, 100)
	shadow_offset = (2, 2)
	button_bg = (128, 128, 128, 200)
	button_text = (200, 200, 200)
	title_font_size = 24

	ui.init('Cinematronics Audio Tester', (LCD_WIDTH, LCD_HEIGHT))
	pygame.mouse.set_visible(False)

	ui.theme.current.set(class_name='Label', state='normal', key='background_color', value=clear_color)
	ui.theme.current.set(class_name='Label', state='normal', key='text_color', value=title_color)
	ui.theme.current.set(class_name='Label', state='normal', key='text_shadow_color', value=shadow_color)
	ui.theme.current.set(class_name='Label', state='normal', key='text_shadow_offset', value=shadow_offset)
	ui.theme.current.set(class_name='Label', state='normal', key='font', value=resource.get_font(title_font_size, True))

	ui.theme.current.set(class_name='Button', state='normal', key='background_color', value=button_bg)
	ui.theme.current.set(class_name='Button', state='normal', key='text_color', value=button_text)
	ui.theme.current.set(class_name='Button', state='normal', key='text_shadow_color', value=None)
	ui.theme.current.set(class_name='Button', state='normal', key='text_shadow_offset', value=None)
	ui.theme.current.set(class_name='Button', state='selected', key='background_color', value=yellow_color)

	ui.theme.current.set(class_name='NotificationView', state='normal', key='font', value=resource.get_font(8, False))
	ui.theme.current.set(class_name='NotificationView', state='normal', key='text_color', value=shadow_color)
	ui.theme.current.set(class_name='NotificationView', state='normal', key='background_color', value=((190, 200, 255), (100, 100, 100)))
	ui.theme.current.set(class_name='NotificationView', state='normal', key='border_color', value=shadow_color)

	ui.scene.push(MainMenu())

	ui.run()
