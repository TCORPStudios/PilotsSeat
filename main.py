#Imports
import time
from colorama import Fore, Back, Style
from random import randint
import replit

#Variable list
fakeCPU = 1  #Fake CPU delay for time.sleep function.
statChecks = 0  #How many times the user has ran program 101: STATUS.
programsRan = 0  #How many programs the user has ran.
fuelMax = 1000  #Ship fuel capacity
fuelLvl = fuelMax  #Ship fuel is equal to max at init.
cellMax = 10  #Fuel cell kick random max.
cellMin = 0  #Fuel cell kick random minimum.
commandCost = 5  #Fuel required to execute a command
target = 0 #Current target
orbiting = 0 #Orbiting a planet? 0 or 1

#Location list, each entry is a list of 4 variables. [Name(str), Distance from Sun(int), Can be landed on(0 or 1), Fuel required to land(int)]
locList = [
  ["SUN", 0, 0, 0], ["CALIDUM", 10, 1, 10], ["IGNIS", 25, 1, 30], ["DOMUM", 50, 1, 10]
]

currentLoc = randint(0, len(locList)-1)
target = currentLoc

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
    print(Fore.MAGENTA + "LOCATION     :" + Fore.WHITE + str(locList[currentLoc][0]))
    time.sleep(fakeCPU)
    codeInput()

def prog6(): #Program 401, Target Menu
  global currentLoc
  global locList
  global target
  for i in range(len(locList)):
    print(Fore.WHITE + str(i) + " " + Fore.MAGENTA + str(locList[i][0]) + Fore.WHITE + " - Distance: " + str(abs(locList[i][1]-locList[currentLoc][1])))
    time.sleep(fakeCPU)
  target = input(Fore.WHITE + "Select a Target:")
  if int(target) > int(len(locList)-1):
    print(Fore.RED + "Code Input Error #005 (Program Error)\nTarget Does Not Exist")
    target = 0
  elif currentLoc == target:
    print(Fore.RED + "Code Input Error #005 (Program Error)\nAlready at Target")
    target = 0
  else:
    print(Fore.MAGENTA + "Target Selected\nRun Program #402 to proceed to destination")
  codeInput()

def prog7(): #Program #402, Go to Target
  global currentLoc
  global locList
  global target
  global fuelLvl
  global fuelMin
  i = 0
  for i in range(abs(locList[int(target)][1]-locList[int(currentLoc)][1])):
    if abs(locList[int(target)][1]-locList[int(currentLoc)][1]) > fuelLvl:
      print(Fore.YELLOW + "Insuffcient Fuel\nRun Program #601 to run the Fuel Cell\nRun Program #101 to see status")
      break
    print(Fore.MAGENTA + "Distance to Target: " + Fore.WHITE + str((abs(locList[int(target)][1]-locList[int(currentLoc)][1])-i)))
    fuelLvl -= 1
    time.sleep(fakeCPU)
  if i == abs(locList[int(target)][1]-locList[int(currentLoc)][1])-1:
    print(Fore.MAGENTA + "Arrived at Target")
  if currentLoc == target:
    print(Fore.RED + "Code Input Error #005 (Program Error)\nAlready at Target\nRun Program #401 to select a Target")
  target = 0
  codeInput()
  
def prog9(): # Program #502, Abort Sequence
  print(Fore.WHITE + Back.RED + "ABORT SEQUENCE ARMED!")
  print(Style.RESET_ALL + Fore.RED + "Are you sure you want to abort?")
  check = randint(100, 999)
  check = str(check)
  sure = input(Fore.WHITE + "Type "+ check +" to confirm:")
  if sure == check:
    print(Style.RESET_ALL)
    endGame()
  else:
    print(Fore.WHITE + "Abort Sequence Cancelled")
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
  global fuelLvl
  if fuelLvl < commandCost:
    print(Fore.RED + "Code Input Error #004 (Insufficient Fuel to Execute)\nCannot Retry. Powering Down" + Fore.WHITE)
  fuelLvl = 0
  time.sleep(fakeCPU*2)
  replit.clear()
  time.sleep(fakeCPU*3)
  print("Game Over")
  time.sleep(fakeCPU)
  print(Fore.BLUE + "STATUS CHECKS:" + Fore.WHITE + str(statChecks))
  time.sleep(fakeCPU)
  print(Fore.GREEN + "PROGRAMS RAN :" + Fore.WHITE + str(programsRan))
  time.sleep(fakeCPU)
  exit("Thank you for Playing")

if fuelLvl > 0:
  codeInput()
