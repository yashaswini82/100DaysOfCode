print(r'''treasure chest:
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("After walking for hours in the island, you reach a fork in the path")
fork = input('Where do you want to go? "left" or "right"? \n').lower()
if fork == "left":
    path = input('You reached near an canyon which has a bridge to cross. \nDo you want to cross the bridge or find alternative path? \nType "cross" to cross the bridge or "find" to find alternative path. \n').lower()
    if path == "find":
        cave = input('In the search of alternative path, you walked into cave. \nYou found a way which has little golden light coming from it and a completely dark way. \nType "gold" to know where the golden light is coming from or type "dark" to go into that dark way. \n').lower()
        if cave ==  "dark":
            print("YAY! You found the TRASEURE!!!")
        elif cave == "gold":
            print("You got tricked by golden light and fallen into a pit. \n GAME OVER!")
        else:
            print("You have not chosen any of the given paths. Please choos only from the given ways.")
    elif path == "cross":
        print("The bridge collapsed and you died.. \n GAME OVER!")
    else:
        print("You have not chosen any of the given paths. .Please choose only from the given paths.")
elif fork == "right":
    print("You walked into quicksand and died. \n GAME OVER!. ")
else:
    print("You have not chosen any of the given paths. Please choose only from the given ways.")
