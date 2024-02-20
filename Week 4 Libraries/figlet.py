from pyfiglet import Figlet
import sys
import random

# List of valid options for first paramater
parameter1 = ["-f", "--font"]
figlet = Figlet()

# List of valids fonts
fonts = figlet.getFonts()

#IF the user does not want a random font
if len(sys.argv) == 1:
    user = input("Input: ")
    fontNumber = random.randint(0, len(fonts))
    figlet.setFont(font=fonts[fontNumber])
    print(figlet.renderText(user))

elif len(sys.argv) == 3 and sys.argv[1] in parameter1:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")
    figlet.setFont(font=sys.argv[2])
    user = input("Input: ")
    print(figlet.renderText(user))
else:
    sys.exit("Invalid Usage")