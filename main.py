print('''           ____,'`-,
      _,--'   ,' `---.___        ___,_
   |       ,:';:/        ;'"`;"`--./ ,-^.;--.
   |:     ,:';,'         '         `.   ;`   `-.
    \:.,:::/;/ -:.                   `  | `     `-.
     \:::,'//__.;  ,;  ,  ,  :.`-.   :. |  ;       :.
      \,',';/O)^. :'  ;  :   '__` `  :::`.       .:' )
      |,'  |\__,: ;      ;  '/O)`.   :::`;       ' ,'
           |`--''            \__,' , ::::(       ,'
           `    ,            `--' ,: :::,'\   ,-'
            | ,;         ,    ,::'  ,:::   |,'
            |,:        .(          ,:::|   `
            ::'_   _   ::         ,::/:|
           ,',' `-' \   `.      ,:::/,:|
          | : _  _   |   '     ,::,' :::
          | \ O`'O  ,',   ,    :,'   ;::
           \ `-'`--',:' ,' , ,,'      ::
            ``:.:.__   ',-','        ::'
    -hrr-      `--.__, ,::.         ::'
                   |:  ::::.       ::'
                   |:  ::::::    ,::'
''')

print("Find the treasure box to find your gift!")

print(" your mission is to find the Dog")
choise1 = input('You\'re at a crossroad, where do you want to go ?'
                ' Type "Left "or "Right". ').lower()

if choise1 == "left":
   choise2 = input('You\'ve come into a lake. there is an island in the middle of the lake. \n'
         'Type "Swim " if you want to get there \n or " Wait" if you want to wait for a boat. ').lower()

   if choise2 == "wait":
       choise3 = input('You arrive to the island unharmed. there is a house with two doors.'
                       'Red, or Green. Whish door do you choose ?').lower()
       if choise3 == "red":
           print("You have found the dog, Congratulation. ")
       else:
           print("You have fell into the water. Game over.")
   else:
       print("You got attacked by shark. Game over")
else:
    print("you fell into a holl, :( Game over")