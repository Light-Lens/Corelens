# Corelet
# Modules are imported that will be used in Corelet.
from colorama import Fore, Back, Style
from colorama import init
import time
import sys
import os

from GUI import GUI
import LOG

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
Display = pygame.display.set_mode((475, 650))
pygame.display.set_caption("Corelet")
pygame.display.set_icon(Logo)

os.system('title Corelet')
LOG.CORELET_LOG(Fore.GREEN + "Corelet")

# Virus names
Virus_names = "virus.exe", "exploit.application", "internet_explorer.exe", "fake_virus.bat"

# This function will check whether it should allow any program or not.
def IsVirus(files):
	if files in Virus_names: return True
	else: return False

# Main Antivirus Loop
Title = GUI.Label(Display, (25, 25, 25), 0, 0, 475, 70)
Title_Text = GUI.Text(Display, "Corelet", (90, 90, 90), (160, 10), 50)

Change = GUI.Button(Display, (50, 50, 50), (70, 70, 70), (40, 40, 40), 10, 100, 115, 30)
Change_Text = GUI.Text(Display, "System scan", (255, 255, 255), (15, 104), 21)
Change_Border = GUI.Label(Display, (18, 18, 18), 10, 130, 115, 2)
Change_Left_Border = GUI.Label(Display, (18, 18, 18), 10, 100, 2, 30)
while Loop:
	clock.tick(120)
	Display.fill((44, 44, 44))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	Title.draw()
	Title_Text.draw()

	Change.draw()
	Change_Text.draw()
	Change_Border.draw()
	Change_Left_Border.draw()

	pygame.display.update()
pygame.quit()
