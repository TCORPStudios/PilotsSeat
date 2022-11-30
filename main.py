#Imports
import time
from colorama import Fore
from random import randint
import replit

#Variable list
fakeCPU = 1  #Fake CPU delay for time.sleep function.
statChecks = 0  #How many times the user has ran program 101: STATUS.
programsRan = 0  #How many programs the user has ran.
fuelMax = 1000  #Ship fuel capacity
fuelLvl = fuelMax  #Ship fuel is equal to max at init.
fuelToLand = 100  #Fuel required to land or ascend.
cellMax = 5  #Fuel cell kick random max.
cellMin = 0  #Fuel cell kick random minimum.
commandCost = 5  #Fuel required to execute a command

#Initialization and titles
replit.clear()
print(Fore.BLUE + "Pilot's Seat" + Fore.GREEN + "v0.2a")
time.sleep(fakeCPU * 2)
print(Fore.WHITE + "Code and design (C) 2021-2022 Trinity K. Martinez")
time.sleep(fakeCPU * 2)
print(Fore.WHITE + "(C)2021 TCORP Studios\n(C)2022 AUVIMA Software")
time.sleep(fakeCPU * 2)
replit.clear()

#codeList contains all code IDs in order.
codeList = [
    "101: STATUS", "102: RADAR ", "201: LAND  ", "211: ASCEND", "301: OPNDOR",
    "311: CLSDOR", "401: TGTMEN", "402: GTOTGT", "501: EMRGNC", "502: ABORT ",
    "601: FULCEL"
]
#codeNumbers identifies all codes.
codeNumbers = [
    "101", "102", "201", "211", "301", "311", "401", "402", "501", "502", "601"
]


#codeInput is run to get user input and store it into a variable for codeInterpreter.
def codeInput():
    varCode = input(Fore.WHITE + "Input Code:")
    time.sleep(fakeCPU)
    if fuelLvl <= 0:  #When fuelLvl reaches 0 or lower, end the game.
      endGame()
    else:
      codeInterpreter(varCode)


#codeInterpreter is run to identify the user input, and determine user errors.
def codeInterpreter(code):
    if code != "":  #Test if input isn't empty.
        print(Fore.GREEN + "Code #" + code + " Processing")
        time.sleep(fakeCPU)
        try:
            codeIndex = codeNumbers.index(code)
            print(Fore.GREEN + codeList[codeIndex])
            progRun(codeIndex)
        except ValueError:  #If an error happens, run codeInput again.
            print(Fore.RED +
                  "Code Input Error #001 (General Fault) \nRetrying...")
            time.sleep(fakeCPU)
            codeInput()
    else:  #If input is empty, run codeInput again.
        print(Fore.RED + "Code Input Error #002 (Null Input) \nRetrying...")
        time.sleep(fakeCPU)
        codeInput()


def progRun(programVar):  #progRun is ran to interpret input and run programs.
    global programsRan
    global codeNumbers
    global fuelLvl
    global commandCost
  
    fuelLvl = fuelLvl - commandCost  #Every command costs a certain ammount of fuel
  
    codesMax = ((len(codeNumbers))
                )  #Makes a variable that measures how many codes there are.
    for i in range(
            0, codesMax, 1
    ):  #Makes a loop from 0 to the length of codeNumbers via the codesMax variable.
        if programVar >= i:
            print(Fore.WHITE + "Running program #" +
                  str(codeNumbers[programVar]))
            time.sleep(fakeCPU)
            programsRan += 1  #Adds 1 to the programsRan counter.
            eval("prog" + str(programVar) +
                 "()")  #Run progX() with X being programVar input.
        else:
            print(Fore.RED +
                  "Code Input Error #003 (Program is Undefined) \nRetrying...")
            codeInput()


#Program functions below. If adding another program, then an entry must be added to here in addition codeList and codeNumbers.


def prog0():  #Program 101, status checking.
    global statChecks
    global fuelLvl
    statChecks += 1
    time.sleep(fakeCPU)
    print(Fore.BLUE + "STATUS CHECKS:" + Fore.WHITE + str(statChecks))
    time.sleep(fakeCPU)
    print(Fore.GREEN + "PROGRAMS RAN :" + Fore.WHITE + str(programsRan))
    time.sleep(fakeCPU)
    print(Fore.YELLOW + "FUEL LEVEL   :" + Fore.WHITE + str(fuelLvl))
    time.sleep(fakeCPU)
    codeInput()


def prog10():  #Program 601, Fuel Cell kick.
    global fuelMax
    global fuelLvl
    global cellMax
    global cellMin
    time.sleep(fakeCPU)
    print(Fore.YELLOW + "Fuel Cell Kick in progress...")
    time.sleep(fakeCPU * 2)
    fuelGain = randint(
        cellMin, cellMax
    )  #Makes new variable to store how much the random chance yeilded.
    fuelLvl += fuelGain  #Adds fuelGain variable to fuelLvl variable.
    print(Fore.GREEN + "Fuel gained from Fuel Cell:" + Fore.WHITE +
          str(fuelGain))
    fuelCheck()


def fuelCheck(
):  #Checks if fuel goes over maximum capacity, and adjusts accordingly.
    global fuelMax
    global fuelLvl
    if fuelLvl > fuelMax:
        fuelLvl = fuelMax
    codeInput()

def endGame(
):  #Ending the game.
  print(Fore.RED + "Code Input Error #004 (Insufficient Fuel to Execute)\nCannot Retry. Powering Down" + Fore.WHITE)
  time.sleep(fakeCPU*2)
  replit.clear()
  time.sleep(fakeCPU*3)
  print("Game Over")
  time.sleep(fakeCPU)
  print(Fore.BLUE + "STATUS CHECKS:" + Fore.WHITE + str(statChecks))
  time.sleep(fakeCPU)
  print(Fore.GREEN + "PROGRAMS RAN :" + Fore.WHITE + str(programsRan))
  time.sleep(fakeCPU)
  
if fuelLvl > 0:
  codeInput()
