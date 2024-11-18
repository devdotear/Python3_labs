#! /usr/bin/env python3
# Author:
# Version:
# Description:

import showcard

number = input("Pick a card (1-52):")
filename = "BMP" + number + "GIF"
showcard.display_file(filename)

