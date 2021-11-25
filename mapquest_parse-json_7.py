import urllib.parse
import requests
import time
import os

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Fog7lroZGntKj1Es8s4P62KF9xFa9LtK"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

clear = lambda: os.system('clear')

restart = True
while restart == True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        clear()
        print("Exiting program...")
        time.sleep(2)
        clear()
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        clear()
        print("Exiting program...")
        time.sleep(2)
        clear()
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data ["info"]["statuscode"]
    if json_status == 0:
        print ("API Status: " + str(json_status) + " = A successful route call. \n")
        clear()
        from prettytable import PrettyTable
        t = PrettyTable(['Starting Point', 'End Point', 'Duration', 'Kilometers', 'Fuel Used (Ltr)'])
        t.add_row([orig,dest, (json_data["route"]["formattedTime"]), str("{:.2f}".format((json_data["route"]["distance"] )*1.61)), str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))])
        print(t)
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(bcolors.WARNING + (each["narrative"]) + bcolors.ENDC + bcolors.OKGREEN + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)" + bcolors.ENDC))
            time.sleep(1)
        
        repeat = input("\nRestart? [Y/N]: ")
        if repeat == "N" or repeat == "n":
            restart = False
            clear()
            print("Exiting program...")
            time.sleep(2)
            clear()
            break
        else:
            clear()
    
    elif json_status == 402:
        print(bcolors.FAIL + "\nStatus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.\n" + bcolors.ENDC)

    elif json_status == 611:
        print(bcolors.FAIL + "\nStatus Code: " + str(json_status) + "; Missing an entry for one or both locations.\n" + bcolors.ENDC)

    else:
        print(bcolors.FAIL + "\nFor Staus Code: " + str(json_status) + "; Refer to:\n" + bcolors.ENDC)
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")