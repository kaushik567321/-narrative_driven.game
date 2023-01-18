print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Relic Hunt.")
print("Your mission is to find the Staf of The First Mage .")



#Write your code below this line 👇

chocie1 = input(
    'you are standing infront of a cave with two entrances ,type "left" or "right".').lower()
if chocie1 == "left":
  choice2 =input('aftering entering the secret room ,where you see a "knight statue" and "goliath statue",').lower()
  if choice2 == "knight statue":
    print("a portal opens in the wall")
    choice3 = input("by entering the portal,you find yourself in an underground tunnel.In the end of the tunnelyou see a 'golden tresure chest' and an 'old rusty casket'half burried in the ground").lower()
    if choice3=="old rusty casket":
      print("the casket turns into an ancient Staf with nordic runes carved on it! You have found ,The Relic!!.")    
    else:
      print("GAME OVER!the tunnel gets filled with toxicfog out of nowhere.")
  else:
    print("GAME OVER!! you got killed by the Goliath")
else:
   print("GAME OVER ! you got attacked by a gargoyle")
