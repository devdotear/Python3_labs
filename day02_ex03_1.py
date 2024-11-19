#! /usr/bin/env python3
# Author: Earl E
# Version: 1.0
# Description:
import getpass

master_pin = "0123"
pin = None
attempts = 0


while pin != master_pin and attempts < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    print("Too many attempts")
    print("Your card has been captured! Have a worse day!")

print("Done.")