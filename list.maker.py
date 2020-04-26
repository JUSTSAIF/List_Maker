#===========================#
#    Coded By  : SAIF       #
#    My Instagram : qq_iq   #
#    site : v.ht/GgBoys28   #
#===========================#

import random
from colorama import Fore
import sys
import time

print("\n\n")
print(Fore.RED +"           ___          _ _      _     _     __  __       _              ")
print("          / _ \        | | |    (_)   | |   |  \/  |     | |             ")
print("__      _| | | |_ __ __| | |     _ ___| |_  | \  / | __ _| | _____ _ __  ")
print("\ \ /\ / / | | | '__/ _` | |    | / __| __| | |\/| |/ _` | |/ / _ \ '__| ")
print(" \ V  V /| |_| | | | (_| | |____| \__ \ |_  | |  | | (_| |   <  __/ |    ")
print("  \_/\_/  \___/|_|  \__,_|______|_|___/\__| |_|  |_|\__,_|_|\_\___|_|    ")
print(Fore.GREEN +"                          || INSTA : @qq_iq || ")
print(Fore.BLUE + "\n\n")
wordlist_file = open('wordlist.txt', 'w')

input_1 = input("Type letters Or Numbers You Want : ")
     
if input_1 == "":
    sys.exit(Fore.RED + 'ERROR :: The field is empty ')
    
input_2 = input("Word Length : ")
while True:
    
    try:
        
        i = int(input_2)
        break
    
    except ValueError:
        sys.exit(Fore.RED + 'ERROR :: The field is empty Or You Typed a Letter \n Please type a Number ')
        

input_3 = input("How Many : ")

while True:
    
    try:
        
        i = int(input_3)
        break
    
    except ValueError:
        sys.exit(Fore.RED + 'ERROR :: The field is empty Or You Typed a Letter \n Please type a Number ')
        


def rand_wordlist(length=1):
    return ''.join((random.choice(input_1) for i in range(length)))

for i in range(int(input_3)):
    
    print(rand_wordlist(int(input_2)))


    wordlist_file.write(rand_wordlist(int(input_2)) + '\n')
# status generator
def range_with_status(total):
    n = 0
    while n < total:
        done = '#' * (n + 1)
        todo = '-' * (total - n - 1)
        s = '||{0}||'.format(done + todo)
        if not todo:
            s += '\n'
        if n > 0:
            s = '\r' + s
        print(s, end='\r')
        sys.stdout.flush()
        yield n
        n += 1
for i in range_with_status(50):
    time.sleep(0.1)

print("======================================================")
print("The List Has Been Saved in File Named 'wordlist.txt' ")
print("======================================================")
