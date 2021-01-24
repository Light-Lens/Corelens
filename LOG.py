# Os module is important to use Command Prompt commands.
import os

# It's a Log message function
def CORELET_LOG(message):
	print(message)

# It's a Error Log message function
def CORELET_ERROR_LOG(message):
	print(Fore.RED + message)

# It's a Clear Log message function
def CORELET_LOG_CLEAR():
	HEXA_ENGINE_LOG(Fore.GREEN + "Hexa engine")
	os.system('cls')
