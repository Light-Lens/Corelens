# All these imports are important for Engine
import time
import sys
import os

import LOG

# Global variables
WinDir = os.environ['SYSTEMDRIVE']
Timer = 0

"""
Engine will have all features for Corelet (All features that an antivirus has).
All features
"""
def System_scan(WinDir):
	LOG.CORELET_LOG(f"Scanning {WinDir}\\ drive")

def Custom_scan(CustomFilePath):
	pass

def RealTime_Protection(WinDir):
	pass
