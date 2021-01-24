# Corelet
# Modules are imported that will be used in Corelet.
from colorama import Fore, Back, Style
from colorama import init
import time
import sys
import os

import LOG
import GUI

# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# Initializing Corelet
init(autoreset = True)
pygame.init()

Loop = True
Logo = pygame.image.load("Logo.png")
clock = pygame.time.Clock()
Display = pygame.display.set_mode((475, 575))
pygame.display.set_caption("Corelet")
pygame.display.set_icon(Logo)

os.system('title Corelet')
LOG.CORELET_LOG(Fore.GREEN + "Corelet")

while Loop:
	clock.tick(60)
	Display.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	pygame.display.update()
pygame.quit()
