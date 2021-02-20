# Corelet
# Modules are imported that will be used in Corelet.
from colorama import Fore, Back, Style
from colorama import init
import time
import json
import sys
import os

from ENGINE import *
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

# Global variables
Count = 1
Loop = True
WinDir = os.environ['SYSTEMDRIVE']
Username = os.environ['USERNAME']
CONSOLE_DATA = "RealTime Protection is activated."
Logo = pygame.image.load("Logo.png")
Circle = pygame.image.load("Circle.png")
clock = pygame.time.Clock()
IsPressed = {
'System_scan' : 0,
'Custom_scan' : 0,
'Realtime_protection' : 0
}

# Setting up window
Display = pygame.display.set_mode((475, 650))
pygame.display.set_caption("Corelet")
pygame.display.set_icon(Logo)

# Setting up Terminal
os.system('title Corelet')
LOG.CORELET_LOG(Fore.GREEN + "Corelet")
LOG.CORELET_LOG(Fore.GREEN + f"Your Windows installtion drive \"{WinDir}\\\" has been detected for scan.")
with open("PROPERTIES.json", "r") as READ:
	Content = json.load(READ)
	for Data in Content["PROPERTIES"]:
		if Data["realtime_protection"] == True and Data["startup_protection"] == True:
			LOG.CORELET_LOG("Startup Protection is enabled.")
			LOG.CORELET_LOG("Realtime Protection is enabled.\n")
			RealTime_Protection(Count)

		elif Data["realtime_protection"] == False and Data["startup_protection"] == False:
			LOG.CORELET_ERROR_LOG("Startup Protection is disabled.")
			LOG.CORELET_ERROR_LOG("Realtime Protection is disabled.\n")

		elif Data["realtime_protection"] == False: LOG.CORELET_ERROR_LOG("Realtime Protection is disabled.\n")
		elif Data["startup_protection"] == False: LOG.CORELET_ERROR_LOG("Startup Protection is disabled.\n")
		elif Data["startup_protection"] == True:
			LOG.CORELET_LOG("Startup Protection is enabled.\n")
			RealTime_Protection(Count)

		elif Data["realtime_protection"] == True:
			LOG.CORELET_LOG("Realtime Protection is enabled.\n")
			RealTime_Protection(Count)

# Virus names
Virus_names = "virus.exe", "exploit.application", "internet_explorer.exe", "fake_virus.bat"

# This function will check whether it should allow any program or not.
def IsVirus(files):
	if files in Virus_names: return True
	else: return False

# Main Antivirus Loop
Title = GUI.Label(Display, (25, 25, 25), 0, 0, 475, 70)
Title_Text = GUI.Text(Display, "Corelet", (90, 90, 90), (160, 10), 50)

SystemScan = GUI.Button(Display, (50, 50, 50), (70, 70, 70), (40, 40, 40), 30, 100, 120, 30)
SystemScan_Info = GUI.Text(Display, f"Scan {WinDir} drive (Cannot scan other drives)", (0, 0, 0), (38, 140), 13)
SystemScan_Text = GUI.Text(Display, "System scan", (255, 255, 255), (38, 104), 21)
SystemScan_Border = GUI.Label(Display, (18, 18, 18), 30, 130, 120, 2)
SystemScan_Left_Border = GUI.Label(Display, (18, 18, 18), 30, 100, 2, 30)

CustomScan = GUI.Button(Display, (50, 50, 50), (70, 70, 70), (40, 40, 40), 30, 200, 120, 30)
CustomScan_Info = GUI.Text(Display, f"Scans only a particular file, folder or drive", (0, 0, 0), (38, 240), 13)
CustomScan_Text = GUI.Text(Display, "Custom scan", (255, 255, 255), (38, 204), 21)
CustomScan_Border = GUI.Label(Display, (18, 18, 18), 30, 230, 120, 2)
CustomScan_Left_Border = GUI.Label(Display, (18, 18, 18), 30, 200, 2, 30)
while Loop:
	clock.tick(120)
	Display.fill((44, 44, 44))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	Title.draw()
	Title_Text.draw()

	IsPressed['System_scan'] = SystemScan.draw()
	SystemScan_Text.draw()
	SystemScan_Info.draw()
	SystemScan_Border.draw()
	SystemScan_Left_Border.draw()
	Display.blit(Circle, (10, 109))
	if IsPressed['System_scan'] == 1:
		System_scan()

	IsPressed['Custom_scan'] = CustomScan.draw()
	CustomScan_Text.draw()
	CustomScan_Info.draw()
	CustomScan_Border.draw()
	CustomScan_Left_Border.draw()
	Display.blit(Circle, (10, 209))
	if IsPressed['Custom_scan'] == 1:
		LOG.CORELET_LOG("Do a Custom scan\n")

	pygame.display.update()
pygame.quit()
