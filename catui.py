import pygame
import os
import pygameui as ui
import logging
#import RPi.GPIO as GPIO
import gameboards
 
PINS = {
	'11': 11,
	'12': 12,
	'13': 13,
	'14': 14,
	'15': 15,
	'16': 16
}

#Setup the GPIOs as outputs - only 4 and 17 are available
#GPIO.setmode(GPIO.BCM)
#for gpio_port in PINS.items:
#	GPIO.setup(gpio_port, GPIO.OUT)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(17, GPIO.OUT)
 
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
		
		self.image_view = ui.view_for_image_named('bg', True)
		self.image_view.frame.right = LCD_WIDTH
		self.image_view.frame.top = 0
		self.add_child(self.image_view)

		self.title_rect = ui.Rect(0, 0, LCD_WIDTH, 60)
		self.title = ui.Label(self.title_rect, 'Cinematronics Audio Tester')
		self.add_child(self.title)
		
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
		sm.selected_game = btn.text
		sm.set_contents()
		ui.scene.pop()
		ui.scene.push(sm)

class SoundMenu(ui.Scene):

	def __init__(self):
		ui.Scene.__init__(self)
		
		self.selected_game = ''
		
		self.image_view = ui.view_for_image_named('bg', True)
		self.image_view.frame.right = LCD_WIDTH
		self.image_view.frame.top = 0
		self.add_child(self.image_view)

	def set_contents(self):
		self.title_rect = ui.Rect(0, 0, LCD_WIDTH, 40)
		self.title = ui.Label(self.title_rect, 'Activate Sound for ' + self.selected_game + ':')
		self.add_child(self.title)
		
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
			btn = ui.Button(ui.Rect(x, y, btn_w, btn_h), sound[0])
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
		
		adv_btn = ui.Button(ui.Rect(LCD_WIDTH - btn_w, LCD_HEIGHT - btn_h, btn_w, btn_h), 'Avanced >')
		adv_btn.on_clicked.connect(self.adv_btn_clicked)
		self.add_child(adv_btn)
	
	def init_board(self, btn, mbtn):
		logger.info('Initialize clicked')
	
	def play_sound(self, btn, mbtn):
		#GPIO.output(17, False)
		logger.info(btn.text)
		
	def back_btn_clicked(self, btn, mbtn):
		ui.scene.pop()
		ui.scene.push(MainMenu())

	def adv_btn_clicked(self, btn, mbtn):
		am = AdvMenu()
		am.selected_game = self.selected_game
		am.set_contents()
		ui.scene.pop()
		ui.scene.push(am)

class AdvMenu(ui.Scene):

	def __init__(self):
		ui.Scene.__init__(self)
		
		self.selected_game = ''
		
		self.image_view = ui.view_for_image_named('bg', True)
		self.image_view.frame.right = LCD_WIDTH
		self.image_view.frame.top = 0
		self.add_child(self.image_view)

		self.title_rect = ui.Rect(0, 0, LCD_WIDTH, 40)
		self.title = ui.Label(self.title_rect, 'Toggle/Pulse pins directly:')
		self.add_child(self.title)
		
	def set_contents(self):

		btn_w = 60
		btn_h = 40
		
		# toggle row
		lbl = ui.Label(ui.Rect(10, 100, 70, btn_h), 'Toggle')
		self.add_child(lbl)
		for col in range(6):
			pin = 11 + col
			x = 90 + col * (btn_w + 5)
			y = 100
			
			tgl_btn = ui.Button(ui.Rect(x, y, btn_w, btn_h), str(pin))
			tgl_btn.on_clicked.connect(self.tgl_btn_clicked)
			self.add_child(tgl_btn)

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
	
	def init_board(self, btn, mbtn):
		logger.info('Initialize clicked')
	
	def tgl_btn_clicked(self, btn, mbtn):
		#GPIO.output(17, False)
		logger.info('Toggle:' + btn.text)
		
	def pls_btn_clicked(self, btn, mbtn):
		#GPIO.output(17, False)
		logger.info('Pulse:' + btn.text)

	def back_btn_clicked(self, btn, mbtn):
		ui.scene.pop()
		ui.scene.push(MainMenu())

	def adv_btn_clicked(self, btn, mbtn):
		sm = SoundMenu()
		sm.selected_game = self.selected_game
		sm.set_contents()
		ui.scene.pop()
		ui.scene.push(sm)
		
if __name__ == '__main__':
	
	ui.init('Cinematronics Audio Tester', (LCD_WIDTH, LCD_HEIGHT))
	pygame.mouse.set_visible(False)
	
	ui.scene.push(MainMenu())
	
	ui.run()