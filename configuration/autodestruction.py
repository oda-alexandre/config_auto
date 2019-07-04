# coding:utf-8

import os

print("\033[36;1m"
      "\n"
      "IN THE WINDOW THAT WILL FOLLOW INQUIRY AS THIS :\n\n"

      "1-Enter your decryption password (the one used when starting the PC)\n"
      "2-Enter your password for self destruction\n"
      "3-Confirm password for self destruction\n"
      "\n"
      "\033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

print("\033[36;1m \nCONFIG OF PASSWORD SELF DESTRUCTION WITH CRYPTSETUP\n \033[0m")

os.system("sudo cryptsetup luksAddNuke /dev/sda3")
