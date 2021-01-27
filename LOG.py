# Modules are important for using LOG.
from colorama import Fore, Back, Style
from colorama import init
import os

# Initializing LOG
init(autoreset = True)

# It's a Log message function
def CORELET_LOG(message):
	print(message)

# It's a Error Log message function
def CORELET_ERROR_LOG(message):
	print(Fore.RED + message)

# It's a Clear Log message function
def CORELET_LOG_CLEAR():
	os.system('cls')
	CORELET_LOG(Fore.GREEN + "Corelet")
