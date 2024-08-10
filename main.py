from netsacner import scan, display_results
from portscan import portscaner
import pyfiglet
from WHOIS import WHOIS

def main():
    while True:
        ascii_banner = pyfiglet.figlet_format("main_menu")
        print(ascii_banner)
        print("1. Port Scanner")
        print("2. Network Scanner")
        print("3. WHOIS")
        print("4. Exit")

        user_input = input("What do you need: ")

        if user_input == "1":
            ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
            print(ascii_banner)
            portscaner()

        elif user_input == "2":
            ascii_banner = pyfiglet.figlet_format("Network Scanner")
            print(ascii_banner)
            target_ip = input("Enter the IP you want to scan: ")
            scan_results = scan(target_ip)
            display_results(scan_results)

        elif user_input == "3":
            ascii_banner = pyfiglet.figlet_format("WHOIS")
            print(ascii_banner)
            WHOIS()

        elif user_input == "4":
            print("Exiting Program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()