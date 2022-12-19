#Imports
import time
from colorama import Fore, Back, Style
from random import randint
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#Variable list
fakeCPU = 1  #Fake CPU delay for time.sleep function.
statChecks = 0  #How many times the user has ran program 101: STATUS.
programsRan = 0  #How many programs the user has ran.
fuelMax = 500  #Ship fuel capacity
fuelLvl = fuelMax  #Ship fuel is equal to max at init.
fuelWarn = fuelMax / 4  #Warn user if fuel is less than a quarter of max.
cellMax = 15  #Fuel cell kick random max.
cellMaxCap = cellMax #Unchanging fuel cell kick max.
cellMin = 0  #Fuel cell kick random minimum.
commandCost = 5  #Fuel required to execute a command
radarCost = 5  #Fuel required to keep radar on
target = 0  #Current target
orbiting = 1  #Orbiting a planet? 0 or 1
landingCount = 0  #How many times the ship has landed.
emergency = 0  #Emergency State Triggered. 0 or 1
radar = 0  #Radar is active. 0 or 1
door = 0  #Door is open. 0 or 1

#Emergency list, each element is a list of emergency conditions. [Name(str), Can be fixed(0 or 1), Function name(str), Triggered(0 or 1)]
emergencyList = [["Landing Gear is Damaged", 1, "brokenLegs()", 0],
                 ["Fuel Cell is Damaged", 0, "brokenFuel()", 0],
                 ["EVA Hatch is Damaged", 1, "brokenHatch()", 0]]

#Emergency functions


def brokenLegs():
    global emergencyList
    global emergency
    if emergencyList[0][3] == 1:
        repairAttempt = randint(0, 4)
        time.sleep(fakeCPU * 2)
        if repairAttempt >= 1:
            print("Landing Gear successfully repaired!")
            emergencyList[0][3] = 0

        else:
            print("Landing Gear repair failed!")
        time.sleep(fakeCPU)


def brokenFuel():
    global emergency
    global emergencyList
    global cellMax
    cellMax = 0
    emergencyList[1][3] = 0


def brokenHatch():
    global emergency
    global door
    door = 0
    emergencyList[2][3] = 0


#Location list, each element is a list of variables. [Name(str), Distance from Sun(int), Can be landed on(0 or 1), Fuel required to land(int), Atmosphere present(0 or 1), Embarking program(str)]
locList = [["SUN", 0, 0, 0, 0, "codeInput()"],
           ["CALIDUM", 10, 1, 10, 0, "codeInput()"],
           ["IGNIS", 25, 1, 30, 1, "ignis()"],
           ["DOMUM", 50, 1, 10, 1, "domum()"]]

currentLoc = randint(0, len(locList) - 1)
target = currentLoc

#Initialization and titles
clear()
print(Fore.BLUE + "Pilot's Seat" + Fore.GREEN + " v0.5a")
time.sleep(fakeCPU * 2)
print(Fore.WHITE + "Code and design (C) 2021-2022 Trinity K. Martinez")
time.sleep(fakeCPU * 2)
print(Fore.WHITE + "(C)2021 TCORP Studios\n(C)2022 AUVIMA Software")
time.sleep(fakeCPU * 2)
clear()
time.sleep(fakeCPU)
goal = int(input("Set Landing Goal (0 to exit):"))
if goal > 0:
  goal = int(goal)
else:
  print("Exiting...")
  exit()

#codeList contains all code IDs in order. Append new programs to the end, DO NOT insert them between other programs.
codeList = [
    "101: STATUS", "102: RADAR ", "201: LAND  ", "202: ASCEND", "301: OPNDOR",
    "302: CLSDOR", "401: TGTMEN", "402: GTOTGT", "501: EMRGNC", "502: ABORT ",
    "601: FULCEL"
]
#codeNumbers identifies all codes.
codeNumbers = [
    "101", "102", "201", "202", "301", "302", "401", "402", "501", "502", "601"
]


#codeInput is run to get user input and store it into a variable for codeInterpreter.
def codeInput():
    global emergency
    global goal
    global emergencyList
    if landingCount == goal:
        print(Fore.GREEN + "Landing Count Reached")
        time.sleep(fakeCPU*4)
        clear()
        print(Fore.GREEN + "Your journey has come to an end, you are satsified with your exploration of the universe!")
        time.sleep(fakeCPU*4)
        endGame()
    emergency = 0
    if fuelLvl <= 0:  #When fuelLvl reaches 0 or lower, end the game.
        endGame()
    for em in range(0, len(emergencyList) - 1, 1):
        emergency = emergencyList[em][3] + emergency
    if emergency > 0:
        print(Fore.RED + "EMERGENCY INTERRUPT")
        codeInterpreter("501")
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


def prog0():  #Program 101, Status Check
    global statChecks
    global fuelLvl
    global radar
    statChecks += 1
    time.sleep(fakeCPU)
    print(Fore.BLUE + "STATUS CHECKS:" + Fore.WHITE + str(statChecks))
    time.sleep(fakeCPU)
    print(Fore.GREEN + "PROGRAMS RAN :" + Fore.WHITE + str(programsRan))
    time.sleep(fakeCPU)
    print(Fore.YELLOW + "FUEL USAGE   :" + Fore.WHITE + str(commandCost))
    time.sleep(fakeCPU)
    if fuelLvl < fuelWarn:
        print(Fore.YELLOW + "FUEL LEVEL   :" + Fore.WHITE + str(fuelLvl) +
              Fore.YELLOW + " WARNING\nRun Program #601 to run the Fuel Cell")
    else:
        print(Fore.YELLOW + "FUEL LEVEL   :" + Fore.WHITE + str(fuelLvl))
    time.sleep(fakeCPU)
    if radar == 1:
        print(Fore.MAGENTA + "LOCATION     :" + Fore.WHITE +
              str(locList[currentLoc][0]))
    else:
        print(Fore.YELLOW + Style.BRIGHT +
              "RADAR SYSTEM IS OFF\nRun Program #102 to toggle radar on/off." +
              Style.RESET_ALL)
    time.sleep(fakeCPU)
    if orbiting == 1:
        print(Fore.MAGENTA +
              "IN ORBIT\nRun Program #201 to initialize Landing Procedure.")
    else:
        print(Fore.MAGENTA +
              "LANDED\nRun Program #202 to initialize Ascent Procedure.")
    time.sleep(fakeCPU)
    print(Fore.CYAN + "LANDINGS     :" + Fore.WHITE + str(landingCount))
    time.sleep(fakeCPU)
    codeInput()


def prog1():  #Program 102, Radar System Toggle
    global radar
    global commandCost
    global radarCost
    print(Fore.MAGENTA + Style.BRIGHT + "Toggling Radar System...")
    time.sleep(fakeCPU)
    if radar == 0:
        radar = 1
        print(Fore.MAGENTA + Style.BRIGHT + "RADAR ON")
        time.sleep(fakeCPU)
        commandCost = commandCost + radarCost
        print(
            Style.RESET_ALL + Fore.MAGENTA +
            "Navigation and Targeting Subsystem Online\nRun Program #401 to select a Target\nRun Program #402 to travel to a Target"
        )
    else:
        radar = 0
        print(Fore.MAGENTA + Style.BRIGHT + "RADAR OFF")
        time.sleep(fakeCPU)
        commandCost = commandCost - radarCost
        print(
            Style.RESET_ALL + Fore.MAGENTA +
            "Navigation and Targeting Subsystem Offline\nDistances cannot be calculated with the radar off.\nTraveling to a Target is impossible."
        )
    codeInput()


def prog2():  #Program 201, Landing Program
    global landingCount
    global orbiting
    global fuelLvl
    global currentLoc
    global locList
    global emergencyList
    if orbiting == 0:
        print(Fore.RED +
              "Code Input Error #005 (Program Error)\nAlready Landed")
        codeInput()
    if locList[currentLoc][2] == 1:
        if fuelLvl >= locList[currentLoc][3]:
            landingCount += 1
            print(Fore.CYAN + "Landing Procedure Initialized")
            time.sleep(fakeCPU)
            for i in range(locList[currentLoc][3], 0, -1):
                print(Fore.CYAN + "Altitude : " + Fore.WHITE + str(i))
                time.sleep(fakeCPU)
                fuelLvl -= 1
            print(Fore.CYAN + "Landing Procedure Completed")
            orbiting = 0
            time.sleep(fakeCPU)
            failure = randint(0, 5)
            if failure >= 5:
                emergencyList[0][3] = 1
            else:
                failure = 0
        else:
            print(
                Fore.YELLOW +
                "Insufficient Fuel\nRun Program #601 to run the Fuel Cell\nRun Program #101 to see status"
            )
    else:
        print(Fore.RED + "Current Location cannot be landed on")
    codeInput()


def prog3():  #Program 202, Ascent Program
    global orbiting
    global fuelLvl
    global currentLoc
    global locList
    global door
    if door == 1:
      print(Fore.RED + "Door is Open\nRun Program #302 to close the door.")
      time.sleep(fakeCPU)
    if orbiting == 1:
        print(Fore.RED +
              "Code Input Error #005 (Program Error)\nAlready in Orbit")
        codeInput()
    if fuelLvl >= locList[currentLoc][3]:
        print(Fore.CYAN + "Ascent Procedure Initialized")
        time.sleep(fakeCPU)
        for i in range(0, locList[currentLoc][3], 1):
            print(Fore.CYAN + "Altitude : " + Fore.WHITE + str(i))
            time.sleep(fakeCPU)
            fuelLvl -= 1
        print(Fore.CYAN + "Ascent Procedure Completed")
        orbiting = 1
    else:
        print(
            Fore.YELLOW +
            "Insufficient Fuel\nRun Program #601 to run the Fuel Cell\nRun Program #101 to see status"
        )
    codeInput()


def prog4():  #Program 301, Open Door
    global currentLoc
    global locList
    global orbiting
    global door
    if orbiting == 1:
        print(
            Fore.RED +
            "Code Input Error #005 (Program Error)\nCannot Open Door while in orbit.\nRun Program #201 to land."
        )
        time.sleep(fakeCPU)
        codeInput()
    if door == 0:
        if locList[currentLoc][4] == 1:
            print(Fore.BLUE + Style.BRIGHT + "Opening Door..." +
                  Style.RESET_ALL)
            time.sleep(fakeCPU)
            door = 1
            print(Fore.BLUE + "Door Open")
            time.sleep(fakeCPU)
            print("Embark on " + locList[currentLoc][0] + "? (Y/N)")
            embark = input()
            if embark == "Y" or embark == "y":
                print(Fore.BLUE + "Embarking on " + locList[currentLoc][0] +
                      "...")
                time.sleep(fakeCPU)
                eval(locList[currentLoc][5])
            elif embark == "N" or embark == "n":
                print(Fore.BLUE + "Returning to Cockpit...")
                time.sleep(fakeCPU)
                codeInput()
            else:
                print(Fore.BLUE + "Invalid Input\nReturning to Cockpit...")
                time.sleep(fakeCPU)
                codeInput()
        else:
            print(Fore.BLUE + locList[currentLoc][0] +
                  " has no breathable Atmosphere.")
            time.sleep(fakeCPU)
            codeInput()
    else:
        print(Fore.BLUE + "Door is already open.")
        time.sleep(fakeCPU)
        print("Embark on " + locList[currentLoc][0] + "? (Y/N)")
        embark = input()
        if embark == "Y" or embark == "y":
            print(Fore.BLUE + "Embarking on " + locList[currentLoc][0] + "...")
            time.sleep(fakeCPU)
            eval(locList[currentLoc][5])
        elif embark == "N" or embark == "n":
            print(Fore.BLUE + "Returning to Cockpit...")
            time.sleep(fakeCPU)
            codeInput()
        else:
            print(Fore.BLUE + "Invalid Input\nReturning to Cockpit...")
            time.sleep(fakeCPU)
            codeInput()


def prog5():  #Program 302, Close Door
    global door
    if door == 1:
        print(Fore.BLUE + "Closing Door...")
        time.sleep(fakeCPU)
        door = 0
        print(Fore.BLUE + "Door Closed")
        time.sleep(fakeCPU)
        codeInput()
    else:
        print(Fore.BLUE + "Door is already closed.")
        time.sleep(fakeCPU)
        codeInput()


def prog6():  #Program 401, Target Menu
    global currentLoc
    global locList
    global target
    global radar
    for i in range(len(locList)):
        print(Fore.WHITE + str(i) + " " + Fore.MAGENTA + str(locList[i][0]) +
              Fore.WHITE + " - Distance: " +
              str(abs(locList[i][1] - locList[currentLoc][1]) * radar))
        time.sleep(fakeCPU)
    target = input(Fore.WHITE + "Select a Target:")
    if int(target) > int(len(locList) - 1):
        print(Fore.RED +
              "Code Input Error #005 (Program Error)\nTarget Does Not Exist")
        target = 0
    elif currentLoc == target:
        print(
            Fore.RED +
            "Code Input Error #005 (Program Error)\nAlready at Target\nRun Program #201 to land"
        )
        target = 0
    else:
        print(Fore.MAGENTA +
              "Target Selected\nRun Program #402 to proceed to destination")
    codeInput()


def prog7():  #Program #402, Go to Target
    global currentLoc
    global locList
    global target
    global fuelLvl
    global fuelMin
    global orbiting
    global radar
    if radar == 0:
        print(
            Fore.RED +
            "Radar System Offline\nDistances cannot be calculated with the radar off.\nTraveling to a Target is impossible.\nRun Program #102 to toggle radar on/off."
        )
        codeInput()
    if orbiting == 0:
        print(
            Fore.RED +
            "Code Input Error #005 (Program Error)\nNot in Orbit\nRun Program #202 to start the Ascent procedure"
        )
        codeInput()
    i = 0
    for i in range(abs(locList[int(target)][1] - locList[int(currentLoc)][1])):
        if abs(locList[int(target)][1] -
               locList[int(currentLoc)][1]) > fuelLvl:
            print(
                Fore.YELLOW +
                "Insuffcient Fuel\nRun Program #601 to run the Fuel Cell\nRun Program #101 to see status"
            )
            break
        print(Fore.MAGENTA + "Distance to Target: " + Fore.WHITE +
              str((abs(locList[int(target)][1] - locList[int(currentLoc)][1]) -
                   i)))
        fuelLvl -= 1
        time.sleep(fakeCPU)
    if i == abs(locList[int(target)][1] - locList[int(currentLoc)][1]) - 1:
        print(Fore.MAGENTA + "Arrived at Target")
        currentLoc = int(target)
    if currentLoc == target:
        print(
            Fore.RED +
            "Code Input Error #005 (Program Error)\nAlready at Target\nRun Program #401 to select a Target"
        )
        target = 0
    codeInput()


def prog8():  # Program #501, Emergency Menu
    global emergency
    global emergencyList
    if emergency == 0:
        print(
            Fore.WHITE + Back.CYAN +
            "Program Error #006 (Emergency System Error)\nEmergency Menu Disabled\nEmergency systems are not reporting any errors.\nThis program will execute automatically when an emergency is detected."
        )
        print(Style.RESET_ALL)
        codeInput()
    clear()
    time.sleep(fakeCPU)
    print(Back.RED)
    time.sleep(0.5)
    clear()
    print(Fore.WHITE + "EMERGENCY STATE TRIGGERED!")
    time.sleep(fakeCPU)
    print(
        Fore.BLACK +
        "Emergency Systems are reporting an emergency state.\nThis program was executed automatically."
    )
    time.sleep(fakeCPU)
    for progexec in range(0, len(emergencyList)):
        emergency = 0
        for em in range(0, len(emergencyList) - 1, 1):
            emergency = emergencyList[em][3] + emergency
        print("State of System " + str(progexec) + ": ")
        time.sleep(fakeCPU)
        if emergencyList[progexec][3] == 1:
            print("System " + str(progexec) +
                  " is reporting an emergency state: \n" +
                  emergencyList[progexec][0])
            if emergencyList[progexec][1] == 1:
                print("System " + str(progexec) + " can be repaired.")
                time.sleep(fakeCPU)
                print("Repairing System " + str(progexec) + "...")
            else:
                print("System " + str(progexec) + " cannot be repaired.")
                time.sleep(fakeCPU)

                emergencyList[progexec][3] = 0
            eval(emergencyList[progexec][2])
        else:
            print("System " + str(progexec) +
                  " is not reporting an emergency state")
            emergencyList[progexec][3] = 0
    if emergency == 0:
        time.sleep(fakeCPU)
        print(Style.RESET_ALL)
        clear()
        time.sleep(fakeCPU * 4)
        print(Fore.WHITE + "Emergency State has been cleared.")
        codeInput()


def prog9():  # Program #502, Abort Sequence
    print(Fore.WHITE + Back.RED + "ABORT SEQUENCE ARMED!")
    print(Style.RESET_ALL + Fore.RED + "Are you sure you want to abort?")
    check = randint(100, 999)
    check = str(check)
    sure = input(Fore.WHITE + "Type " + check + " to confirm:")
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
    if cellMax == 0:
        print(
            Fore.RED +
            "Code Input Error #005 (Program Error)\nFuel Cell has been disabled by the Emergency Systems to prevent further damage."
        )
        codeInput()
    failure = randint(0, 20)
    if failure >= 20:
        emergencyList[1][3] = 1
        codeInput()
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


def endGame():  #Ending the game.
    global fuelLvl
    if fuelLvl < commandCost:
        print(
            Fore.RED +
            "Code Input Error #004 (Insufficient Fuel to Execute)\nCannot Retry. Powering Down"
            + Fore.WHITE)
    fuelLvl = 0
    time.sleep(fakeCPU * 2)
    clear()
    time.sleep(fakeCPU * 3)
    print("Game Over")
    time.sleep(fakeCPU)
    print(Fore.BLUE + "STATUS CHECKS:" + Fore.WHITE + str(statChecks))
    time.sleep(fakeCPU)
    print(Fore.GREEN + "PROGRAMS RAN :" + Fore.WHITE + str(programsRan))
    time.sleep(fakeCPU)
    print(Fore.CYAN + "LANDINGS     :" + Fore.WHITE + str(landingCount))
    time.sleep(fakeCPU)
    exit("Thank you for Playing")


#Embarking programs


def ignis():
    global door
    global fuelLvl
    global fuelMax
    global emergency
    global emergencyList
    global cellMax 
    global cellMaxCap
    print(Fore.YELLOW +
          "After arriving on Ignis, you are in a safe environment.")
    time.sleep(fakeCPU)
    print(Fore.YELLOW + "The soil of Ignis is very rich in minerals.")
    time.sleep(fakeCPU)
    print(
        Fore.YELLOW +
        "Depending on the location of the landing, you may be able to find a spare "
        + Style.BRIGHT + "fuel cell, " + Style.RESET_ALL + Fore.YELLOW +
        "or harvest the soil for a " + Style.BRIGHT + "complete refuel." +
        Style.RESET_ALL + Fore.WHITE)
    time.sleep(fakeCPU)
    print("(S)earch for Fuel Cell? - (H)arvest Soil? - (R)eturn to Lander?")
    search = input()
    if search == "s" or search == "S":
        print(Fore.YELLOW + "Searching for a spare fuel cell...")
        time.sleep(fakeCPU)
        searchFuel = randint(0, 7)
        if searchFuel == 7:
            print(Fore.YELLOW + "A fuel cell has been found!")
            if emergencyList[1][3] == 1:
                print(
                    Fore.YELLOW +
                    "Emergency Systems previously reported a fuel cell failure.\n The damaged fuel cell has been replaced."
                )
                emergencyList[1][3] = 0
                cellMax = cellMaxCap
                codeInput()
            else:
                print(Fore.YELLOW + "Fuel Cell is already in good condition.")
                codeInput()

        else:
            print(Fore.YELLOW + "No spare fuel cell found.")
            codeInput()
    elif search == "h" or search == "H":
        print(Fore.YELLOW + "Harvesting Soil...")
        time.sleep(fakeCPU)
        searchFuel = randint(0, fuelMax)
        time.sleep(fakeCPU)
        print(Fore.YELLOW + "Harvesting complete.")
        fuelLvl += searchFuel
        print(Fore.GREEN + "Fuel gained from Soil Harvest:" + Fore.WHITE +
              str(searchFuel))
        fuelCheck()
    else:
        print(Fore.YELLOW + "Returning to Lander...")
        time.sleep(fakeCPU)
        codeInput()


def domum():
    print(Fore.RED + "Under construction. Perhaps in the next version.")
    codeInput()


if fuelLvl > 0:
    codeInput()
  
