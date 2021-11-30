#===========================#
#    Coded By  : SAIF       #
#    My Instagram : qq_iq   #
#===========================#

import random,sys
wordlist_file = open('wordlist.txt', 'w')
LENGTH = input("Length : ")
HM = input("How Many : ")

print("\n\n[+] Generating Random Wordlist")
print("[+] Please Wait...")
for i in range(int(HM)):
    wordlist_file.write(''.join((random.choice('abcdefghijklmnopqrstuvwxyz1234567890_') for i in range(int(LENGTH))))+"\n")
wordlist_file.close()
print("\n\n[+] Wordlist Generated Successfully")
print("[+] File Saved As : wordlist.txt")
print("[+] Done !")
sys.exit()

