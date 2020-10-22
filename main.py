# Script was made by Kristian Knudsen 2020 (https://kristian-knudsen.github.io)

import socket 
from datetime import datetime
import sys 

try:
    if len(sys.argv) == 4: # make sure that user enters a target, a starting port and a closing port
        target = socket.gethostbyname(sys.argv[1]) # translate the hostname into IPV4
        startport = int(sys.argv[2]) # get the starting port for the scan
        closeport = int(sys.argv[3]) # get the closing port for the scan
    else:
        print('Invalid amount of arguments - Please give a target, a startport and a close port. Like this "python main.py 127.0.0.1 150 160"')
        sys.exit()


    beginningtime = datetime.now() # get scanning starting point
    print("Beginning scan of all ports started at {}".format(beginningtime))
    for port in range(startport, closeport + 1): # loop through all the ports that the user wanted. Closeport + 1 is to make sure that the scan is including the closing port
        print("Scanning port {}".format(port)) 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using AF_INET to communicate with IPV4 addresses
        socket.setdefaulttimeout(1) # Ensure that each loop only takes ~1 second so script doesnt take forever to run

        result = s.connect_ex((target, port)) # connect to the targeted port to make communication
        if result == 0: # if the connection is successfully established the return of connect_ex is "0"
            print("Port {} is open".format(port))

        s.close() # close the socket to prepare it for the next runthrough
    print("Scan took {}".format(datetime.now() - beginningtime))

except KeyboardInterrupt: # if user interrupts the script with CTRL + C
    print("\nExiting Portscanner script")
    sys.exit()

except socket.gaierror: # If the hostname isn't available to resolve, then close script 
    print("\nHostname couldn't be resolved")

except socket.error: # if the socket isn't working
    print("\nServer is not responding")
    sys.exit()

except NameError: # script error used primarily if a variable is broken. Mainly used during development
    sys.exit()

except ValueError: # if the user types in a comma number as target or either of the two ports
    print("\nPlease dont use comma numbers!")
    sys.exit()