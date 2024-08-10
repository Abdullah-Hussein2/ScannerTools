import pyfiglet
import socket
import sys
from datetime import datetime




def portscaner(**kwargs):
    target = input("Enter the target hostname or IP address: ")

    try:
        x = int(input("Starting port: "))
        y = int(input("Ending port: "))

        print("-" * 50)
        print(f"Scanning Target: {target} ")
        print("Scanning started at: " + str(datetime.now()))
        print("-" * 50)

        for port in range(x, y + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service_name = socket.getservbyport(port)
                except:
                    service_name = "Unknown service"
                print(f"Port {port} is open ({service_name})")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\nServer not responding !!!!")
        sys.exit()
