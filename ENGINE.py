# All these imports are important for Engine
from colorama import Fore, Back, Style
from colorama import init
import time
import sys
import os

import LOG

# Initializing Corelet ENGINE
init(autoreset = True)

# Global variables
Is_virus = []
RootDir = sys.path[0]
Username = os.environ['USERNAME']
WinDir = os.environ['SYSTEMDRIVE']
Userprofile = os.environ['USERPROFILE']

def Listall_items():
	with open("Listings.corelet", "r") as Lines:
		for Data in Lines:
			Line = Data.replace("\n", "")
			Is_virus.append(Line)

"""
Engine will have all features for Corelet (All features that an antivirus has).
All features
"""
def System_scan():
	LOG.CORELET_LOG(f"Scanning {Userprofile}")
	Listall_items()
	os.chdir(Userprofile)
	Content = os.listdir()
	for Files in Content:
		for items in Is_virus:
			if items in Files:
				if os.path.isfile(Files) == True:
					LOG.CORELET_ERROR_LOG(f"Virus found, removed {Files}")
					os.remove(Files)

	os.chdir(RootDir)
	LOG.CORELET_LOG(f"{Userprofile} scanned successfully.")
	LOG.CORELET_LOG(Fore.GREEN + "Your System is safe!\n")

def Custom_scan(CustomFilePath):
	pass

def RealTime_Protection(timer):
	if timer == 3:
		timer = 1
		System_scan()
