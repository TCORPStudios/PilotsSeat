#Imports
import time
from colorama import Fore, Back, Style
from random import randint
import replit

#Variable list
fakeCPU = 1  #Fake CPU delay for time.sleep function.
statChecks = 0  #How many times the user has ran program 101: STATUS.
programsRan = 0  #How many programs the user has ran.
fuelMax = 100  #Ship fuel capacity
fuelLvl = fuelMax  #Ship fuel is equal to max at init.
fuelWarn = fuelMax / 2  #Warn user if fuel is less than half of max.
cellMax = 15  #Fuel cell kick random max.
cellMin = 0  #Fuel cell kick random minimum.
commandCost = 5  #Fuel required to execute a command
radarCost = 5  #Fuel required to keep radar on
target = 0  #Current target
orbiting = 1  #Orbiting a planet? 0 or 1
landingCount = 0  #How many times the ship has landed.
emergency = 0  #Emergency State Triggered. 0 or 1
radar = 0  #Radar is active. 0 or 1

#Emergency list, each element is a list of emergency conditions. [Name(str), Can be fixed(0 or 1), Function name(str), Triggered(0 or 1)]
emergencyList = [["Landing Gear is Damaged", 1, "brokenLegs()", 0],
                 ["Fuel Cell is Damaged", 0, "brokenFuel()", 0]]

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
    global cellMax
    cellMax = 0
    emergencyList[1][3] = 0


#Location list, each element is a list of 4 variables. [Name(str), Distance from Sun(int), Can be landed on(0 or 1), Fuel required to land(int)]
locList = [["SUN", 0, 0, 0], ["CALIDUM", 10, 1, 10], ["IGNIS", 25, 1, 30],
           ["DOMUM", 50, 1, 10]]

currentLoc = randint(0, len(locList) - 1)
target = currentLoc

#Initialization and titles
replit.clear()
print(Fore.BLUE + "Pilot's Seat" + Fore.GREEN + " v0.4a")
time.sleep(fakeCPU * 2)
print(Fore.WHITE + "Code and design (C) 2021-2022 Trinity K. Martinez")
time.sleep(fakeCPU * 2)
print(Fore.WHITE + "(C)2021 TCORP Studios\n(C)2022 AUVIMA Software")
time.sleep(fakeCPU * 2)
replit.clear()

#codeList contains all code IDs in order.
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
    global emergencyList
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
        print(Fore.MAGENTA + "IN ORBIT")
    else:
        print(Fore.MAGENTA + "LANDED")
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
    replit.clear()
    time.sleep(fakeCPU)
    print(Back.RED)
    time.sleep(0.5)
    replit.clear()
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
        replit.clear()
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
    replit.clear()
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


if fuelLvl > 0:
    codeInput()
