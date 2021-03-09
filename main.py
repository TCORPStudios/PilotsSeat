#Imports
import time
from colorama import Fore
from random import randint
import replit

#Variable list
fakeCPU = 1 #Fake CPU delay for time.sleep function.
statChecks = 0 #How many times the user has ran program 101: STATUS.
programsRan = 0 #How many programs the user has ran.


#Initialization and titles
replit.clear()
print(Fore.BLUE + "Pilot's Seat")
time.sleep(fakeCPU)
print(Fore.WHITE + "Code and design (C) 2021 Trinity K. Martinez")
time.sleep(fakeCPU)
replit.clear()

#codeList contains all code IDs in order.
codeList = ["101: STATUS", "102: RADAR ", "201: LAND  ", "211: ASCEND", "301: OPNDOR", "311: CLSDOR", "401: TGTMEN", "402: GTOTGT", "501: EMRGNC", "502: ABORT "]
#codeNumbers identifies all codes.
codeNumbers = ["101", "102", "201", "211", "301", "311", "401", "402", "501", "502"]

#codeInput is run to get user input and store it into a variable for codeInterpreter.
def codeInput():
  varCode = input(Fore.WHITE + "Input Code:")
  time.sleep(fakeCPU)
  codeInterpreter(varCode)

#codeInterpreter is run to identify the user input, and determine user errors.
def codeInterpreter(code):
  if code != "": #Test if input isn't empty.
    print(Fore.GREEN + "Code #"+code+" Processing")
    time.sleep(fakeCPU)
    try:
      codeIndex = codeNumbers.index(code)
      print(Fore.GREEN + codeList[codeIndex])
      progRun(codeIndex)
    except ValueError: #If an error happens, run codeInput again.
      print(Fore.RED + "Code Input Error #001 (General Fault) \nRetrying...")
      time.sleep(fakeCPU)
      codeInput()
  else: #If input is empty, run codeInput again.
    print(Fore.RED + "Code Input Error #002 (Null Input) \nRetrying...")
    time.sleep(fakeCPU)
    codeInput()

def progRun(programVar): #progRun is ran to interpret input and run programs.
  global programsRan
  for i in range(0,((len(codeNumbers))-1),1): #Makes a loop from 0 to the length of codeNumbers.
    if programVar == i:
      print(Fore.WHITE + "Running program #"+ str(codeNumbers[programVar]))
      time.sleep(fakeCPU)
      programsRan += 1 #Adds 1 to the programsRan counter.
      eval("prog" + str(programVar) + "()") #Run progX() with X being programVar input.
    else:
      print(Fore.RED + "Code Input Error #003 (Program is Undefined) \nRetrying...")
      codeInput()

#Program functions below. If adding another program, then an entry must be added to here in addition codeList and codeNumbers.

def prog0():
  global statChecks
  statChecks += 1
  time.sleep(fakeCPU)
  print(Fore.BLUE + "STATUS CHECKS:" + Fore.WHITE + str(statChecks))
  time.sleep(fakeCPU)
  print(Fore.GREEN + "PROGRAMS RAN :" + Fore.WHITE + str(programsRan))
  codeInput()

codeInput()