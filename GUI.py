# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# All engine featues
class GUI:
	class Label:
		def __init__(self, Graphics, Colors, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors
			self.Graphics = Graphics

		def draw(self):
			pygame.draw.rect(self.Graphics, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

	class Button:
		def __init__(self, Graphics, Colors, NewColor, Pressed, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors
			self.NewColor = NewColor
			self.Pressed = Pressed
			self.Graphics = Graphics

		def draw(self):
			pygame.draw.rect(self.Graphics, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))
			self.mouseX, self.mouseY = pygame.mouse.get_pos()
			if self.Posx + self.Sizex > self.mouseX > self.Posx and self.Posy + self.Sizey > self.mouseY > self.Posy:
				pygame.draw.rect(self.Graphics, self.NewColor, (self.Posx, self.Posy, self.Sizex, self.Sizey))
				if pygame.mouse.get_pressed()[0]:
					pygame.draw.rect(self.Graphics, self.Pressed, (self.Posx, self.Posy, self.Sizex, self.Sizey))
					pygame.time.delay(100)
					return 1

				else: return 0

			else: pygame.draw.rect(self.Graphics, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

	class Text:
		def __init__(self, Graphics, Text, Colors, Font_Pos, Font_size):
			self.Colors = Colors
			self.Font_Pos = Font_Pos
			self.Font_size = Font_size
			self.Text = Text
			self.Graphics = Graphics

		def draw(self):
			self.font = pygame.font.SysFont("calibri", self.Font_size)
			self.text = self.font.render(self.Text, True, self.Colors)
			self.Graphics.blit(self.text, self.Font_Pos)
