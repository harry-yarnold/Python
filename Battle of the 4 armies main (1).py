import sys
print('A long time ago,humans were surviving in the harsh war against orcs while the Dwarves and the Elves were hiding in solitude.One unfateful day, war broke out at the castle of the Shire when orcs broke in and they were winning the war.But the Dwarves heard about the orcs plans and stepped into the battle.Their leader was named Gimli and with his mighty army he managed to turn the tide of battle. This was an important victory for the humans and the dwarves so the war was shifting into the north. While the battle was raging on, elves caught wind of the battle and joined the war.What everyone els didnt know was that the elves had joined for personal gain so that they could reconquer their lost lands and remake the elf empire. Gandalf,knowing of the cunningness of the elves, was not sure if he could trust the elves and feared that thet were not contributing to this war for peace but for personal gain. Gandalf decided to arrange a meeting with the King of the elves Elrond when the first north star appearson the nights sky.')
print()
press=input('Press 1 for the orcs backstory(Press 2 for the elves backstory(Press 3 for the dwarves backstory(Press 4 for Bilbos backstory(Press 5 for the battle of bord khagmol Press Enter if you wish to continue:')

print()
while press!='':
    if press=='1':
        print('During this time the orcs were ravaging the defenseless hobbit settlements but not managing to completely destroy them as the treants were fighting beside hobbits and managing to protect them.There was a bad feeling in the air that the war surely wouldnt end peacefully. Sauron sent an orc messenger to deliver a message to the elves. Sauron warned the elves that if they wouldnt stop taking the Iron Armys part in the war Sauron and his allies would rage war against the Elves by destoying their lands and killing Elrond the great.')
        print()
        press=input('Press 1 for the orcs backstory(Press 2 for the elves backstory(Press 3 for the dwarves backstory(Press 4 for Bilbos backstory(Press 5 for the battle of bord khagmol If you wish to continue Press Enter:')
    elif press=='2':
        print('The concerned elves arranged a meeting with Gandalf.The time came and so did Gandalf.During the meeting Gandalf seized the opportunity and accused them for participating in the war for personal gain.Elrond replied that the war would have been lost if the elves did not help and that he Gandalf should be grateful to be alive. Gandalf, enraged, stormed out of the meeting,seek for a mighty warrior to join the iron army. Moreover, Elrond got frustrated with the orcs message and with Gandalf.')
        print()
        press=input('Press 1 for the orcs backstory(Press 2 for the elves backstory(Press 3 for the dwarves backstory(Press 4 for Bilbos backstory(Press 5 for the battle of bord khagmol If you wish to continue Press Enter:')
    elif press=='3':
        print('the dwarves had lost everything from the previous war and were seeking refuge underground to hide from their mortal enemies, the orcs while now they seek new lands in the upper world. Gimli the dwarves leader, was a madman, a crazy bloodthirsty dwarf longing for his old Honour and orc blood to be spilled on the holy grounds of his peoples ruins.Gimlis end goal was regaining his old wealth that was stored in the mountains were the mighty dragon Smaug rests.')
        print()
        press=input('Press 1 for the orcs backstory(Press 2 for the elves backstory(Press 3 for the dwarves backstory(Press 4 for Bilbos backstory(Press 5 for the battle of bord khagmol If you wish to continue Press Enter:')
    elif press=='4':
        print('Bilbo Baggins was a simple hobbit with a big secret on his hands.He barely escaped the invasion of his village by the orcs with the help of treants.Bilbos secret was that he possesed a mighty ring that can save the war and make peace in these lands.Bilbo Baggins was a good friend of Gandalf and the reason why he possesed such a powerful ring.')
        print()
        press=input('Press 1 for the orcs backstory(Press 2 for the elves backstory(Press 3 for the dwarves backstory(Press 4 for Bilbos backstory(Press 5 for the battle of bord khagmol If you wish to continue Press Enter:')
    elif press=='5':
        print('In 1341 The iron army managed to push the orcs back into Bord Khagmol and managed to gain victory with little to no causalities. moreover the treants along with Garen were helping in this war by helping from the south.')
        print()
        press=input('Press 1 for the orcs backstory(Press 2 for the elves backstory(Press 3 for the dwarves backstory(Press 4 for Bilbos backstory(Press 5 for the battle of bord khagmol If you wish to continue Press Enter:')
print()
print('1342 the rise of the orcs and the loss of bord khamol.The orcs were planning to reconquer Bord Khagmol for a northern star to appear to start fighting at Bord Khagmol. When Sauron gave them the order to invade The Misty Mountains and regain the fallen lands. So, they did and were victorious because the elves had stopped attacking from the threat of Sauron.While the orcs keep gaining ground Gandalf starts losing his mind and makes a meeting with the elves and the dwarfs this was known as the great meeting of the iron alliance which happened at 1343 at the fall of Erebor.Finally in 1345 Gandalf suggested bringing in the heroes from every army to defend the last human city. The iron alliance pushed back the orcs at and gained some ground with the new heroes. The last fight broke in and the iron alliance was victorious once again and the orcs have lost the battle, but they managed to capture.')
print()
heroes=input('Type your hero(Type the hero exactly as you see it)\n Wizard Dumbledore\n Archer Legolas\n Hobbit Bilbo Baggins:')
count=1

while heroes!='' and count<=1:
    count+=1
    if heroes=='wizard dumbledore' or heroes=='Wizard dumbledore' or heroes=='wizard Dumbledore' or heroes=='Wizard Dumbledore':
        print('Wizard Dumbledore That fought in the great war of the 4 armies the dwarfs the elves the orcs and the humans but he was captured and imprisoned for 8 years in shaurons prison and tortured')
        dumbledore=input('Press Enter to continue')
    elif heroes=='Archer Legolas' or heroes=='archer Legolas' or heroes=='Archer legolas' or heroes=='archer legolas':
        print('Archer Legolas That fought in the great war of the 4 armies the dwarfs the elves the orcs and the humans but he was captured and imprisoned for 8 years in shaurons prison and tortured')
        print("In a dark dungeon underneath Bord Khagmol Legolas sits waiting for his chance to escape.")
        print("The chains are tight around his hands and feet with the other end attached to the wall.")
        print("As he is thinking the guard starts walking past his cell. Legolas notices that this isn't the normal guard that patrols this section of the dungeon. The guard makes eye contact with Legolas but continues to walk past his cell.")
        print("He notices something shiny on the floor 'the guard must have kicked it over to him' he thought.")
        shiny = input("He picks up a:\n1:Lockpick\n2:Key\n3:Arrow Head\n:")

        if shiny == "1":
            print("Legolas grabs the lockpick and shoves it into the keyhole.")
            print("In such a rush to get out the lockpick snaps.")
            print("luckily, there is just enough of the lockpick left for him to use.")
            print("he slowly twists and the lock opens.")
            print("Now he must find a way out of the cell.")
            print("He notices that the heavy iron cell door is on two-barrel hinges and if he has some leverage, he can push the door up and off its hinges.")
            print("Legolas heads over to a metal pipe sticking out of the wall he starts carving away at the brick around it with what remains of the broken lockpick.")
            print("The pipe comes loose and falls to the ground.")
            print("Legolas picks the pipe up and uses it as a lever to lift the iron door of its hinges.")
            print("It works the door hits the ground with a mighty thud.")
        elif shiny == "2":
            print("Legolas attempts to release his chains with the key.")
            print("However, the key doesn't fit it must be the key to open his cell.")
            print("He starts rubbing the bow of the key against the stone walls allowing him to turn the end of the key into a lockpick.")
            print("He slowly rakes the lock with the end of the key and the lock opens.")
            print("He pulls his hands and feet free from the chains and heads over to the door of his cell.")
            print("The key works and the door swing open with a loud squeak.")
        elif shiny == "3":
            print("Legolas takes the arrow head and jams it in the keyhole.")
            print("He rams the lock against the cold stone wall behind him. in doing so the arrow head pushes down on the pins and with a small twist of the arrow head the lock opens.")
            print("As Legolas removes the chains the lock falls to the ground and smashes.")
            print("He grabs one of the chunks of metal and heads over to the cell door. He uses the chunk of metal as a lockpick and the cell door swings open.")

        print()
        print("Due to all the commotion of Legolas breaking out of his cell he alerts the guards.")
        print("Two guards come running towards his cell.")
        legolasEscape = input("What does Legolas do?\n1:Climbs up a ladder\n2:Runs down the corridor ahead of him\n3:Gets caught\n:")

        if legolasEscape == "1":
            print("Legolas climbes up the ladder and reaches a grate at the top.")
            print("He pushces on the grate")
            print("He find that he is on a street in Bord Khagmol.")
            print("Legolas uses the back alleys to escape the city and heads to Erebor")
        elif legolasEscape == "2":
            print("Two guards come running towards his cell.")
            print("He carries on running until he reaches the storage room.")
            print("He quickly runs through the door and closes it behind him.")
            storageRoom = input("In the corner of the storage room he notices:\n1:His bow and quiver\n2:A Straircase\n3:A Map")
    
            if storageRoom == "3":
                print("The Map shows tunnels underneath the city.")
                print("Legolas follows the map whihc leads him out of the dungeons and out of the city of Bord Khagmol.")
                print("Legolas is sad that he left his bow and quiver at Bord Khagmol.")
                print("Legolas goes to Erebor")
            elif storageRoom == "2":
                print("At the top of the staircase Legolas find an invisibility potion")
                print("Legolas excapes the City and heads to Erebor")
            elif storageRoom == "1":
                print("Legolas hears the orcs get to the door outside the storage room.")
                print("He knocks an arrow and draws his bow.")
                print("The orcs smash through the door")
                print("He releases his arrow whihc goes staight through both of the orcs heads.")
                print("Legolas heads back throught he corridor and climbs up a ladder")
                print("Legolas climbes up the ladder and reaches a grate at the top.")
                print("He pushes on the grate")
                print("He finds that he is on a street in Bord Khagmol.")
                print("Legolas uses the back alleys to escape the city and heads to Erebor")
        elif legolasEscape == "3":
            print("Legolas gets caught by the Orcs.")
            legolasVSOrcs = input("what does Legolas do\n1:Gets Killed\n2:Fights the orcs and wins\n:")
    
            if legolasVSOrcs == "1":
                print("The orcs killed Legolas")
            elif legolasVSOrcs == "2":
                legolasWins = input("Legolas kills the orcs and\n1:Heads to the storage room\n2:Climbs up a ladder\n:")
        
                if legolasWins == "1":
                    print("Legolas heads to the storage room")
                    storageRoomSecond = input("In the corner of the storage room he notices:\n1:His bow and quiver\n2:A Straircase\n3:A Map")
                    if storageRoomSecond == "1":
                        print("Legolas grabs his bow and quiver")
                        print("Legolas heads back down the corridor to the ladder")
                        print("Legolas climbs the ladder")
                        print("At the top of the ladder Legolas finds a grate")
                        print("Legolas pushes on the grate")
                        print("He finds that he is on a street in Bord Khagmol.")
                        print("Legolas uses the back alleys to escape the city and heads to Erebor")
                    elif storageRoomSecond == "2":
                        print("At the top of the staircase Legolas find an invisibility potion")
                        print("Legolas excapes the City and heads to Erebor")
                    elif storageRoomSecond == "3":
                        print("The Map shows tunnels underneath the city.")
                        print("Legolas follows the map whihc leads him out of the dungeons and out of the city of Bord Khagmol.")
                        print("Legolas is sad that he left his bow and quiver at Bord Khagmol.")
                        print("Legolas goes to Erebor")
                
                elif legolasWins == "2":
                    print("Legolas climbs the ladder")
                    print("At the top of the ladder Legolas finds a grate")
                    print("Legolas pushes on the grate")
                    print("He finds that he is on a street in Bord Khagmol.")
                    print("Legolas uses the back alleys to escape the city and heads to Erebor")
    finish = input("Press Enter to Exit:")
    if finish == "Enter":
        sys.exit()
                     
                
    elif heroes=='Hobbit Bilbo Baggins' or heroes=='hobbit bilbo baggins' or heroes=='Hobbit bilbo baggins' or heroes=='hobbit Bilbo baggins' or heroes=='hobbiy bilbo Baggins':
        print('YOU CHOSE THE MISCHIEVOUS HOBBIT')


count=1
while dumbledore=='' and count<=1:
    print('The mighty wizard dumbledore has been captured by an orc commander orgolth and send to Bord Khagmol for 8 years until he \n Escaped\n Died in prison')
    print()
    Q1=input('Press 1 for Escaped or press 2 for died in prison:')
    print()
    if Q1=='1': #Question 1 part 1
        print('When the orcs had a great feast dumbledore found the chance and \nstole the commanders key \ncast a spell to pry the door open')
        print()
        Q2=input('Press 1 stole the commanders key or press 2 for cast a spell to pry the door open:')
        if Q2=='1':#Question 2 part 1
            print('After the feast the guard came in and slept on his chair next to dumbledore cell while he was sleeping dumbledore was close enough to steal the key with a little magic.After that Dumbledore \nWas waiting for the right moment to open the cell door \nOpened the cell door immediately')
            print()
            Q3=input('Press 1 for Was waiting for the right moment to open the cell door or press 2 for Opened the cell door immediately:')
            if Q3=='1':#Question 3 Part 1
                print('so he did and one morning he decided to escape he opened the door and')
                print()
                print('\nsneak past the guards \ntry to cast a spell \nupstairs and propably leave the underground fortress \ndownstairs and propably be captured')
                print()
                Q4=input('press 1 for sneak past the guards press 2 for try to cast a spell press 3 upstairs and propably leave the underground fortress or press 4 downstairs and propably be captured:')
                if Q4=='1':#Question 4 Part 1
                    print('He chooses to sneak past the guards and manages to leave the fortress and go to Bord Khagmo close to erebor')
                    print()
                    print('After that he tried to go to erebor')
                    print()
                    print('While going into erebor he finds an orc in the road he')
                    print()
                    print('\nkills the orc warrior \nsneaks past the orc')
                    Q5=input('Press 1 kills the orc warrior or press 2 sneaks past the orc:')
                    if Q5=='1':#Question third 5 part 1
                        print('dumbledore tries to kill the orc but he gets heavily injured and breathless')
                        print()
                        print('\ntries to find refuge \ncontinues to erebor (risky)')
                        Q5_1=input('Press 1 tries to find refuge or press 2 for continues to erebor (risky)')
                        if Q5_1=='1':#Question third 5.1 part 1
                            print('Dumbledore finds refuge in a nearby village and rest for 4 days -40 gold After the rest he')
                            print()
                            print('goes to erebor')
                    elif Q5=='2':#Question third 5.1 part 2
                        print('Dumbledore continues at erebor but the orcs find him and get him back to his cell')
                        print()
                        print('Dumbledore dies aged 89')
                elif Q4=='2':#Question 4 Part 2
                    print('So he did and the spell took him straight at erebor')
                    print()
                    print('Goes to erebor')
                elif Q4=='3':#Question 4 Part 3
                    print('Dumbledore rushed upstairs and went outside the fortress and found a bag this bag was sent by Gandalf and he could ony choose one item')
                    print()
                    print('\nMagic wand \nSmall goblin \nPouch of gold \nNothing might be a trap \nLucky stone')
                    print()
                    Q5=input('Press 1 for Magic wand press 2 for Small goblin press 3 for pouch of gold press 4 nothing might be a trap or press 5 for Lucky stone:')
                    if Q5=='1':#Question 5 Part 1
                        print('He chose the magic wand and has +1 intelligence he can kill foes easier and can become invisible.After he picks up the wand he')
                        print()
                        print('goes to erebor')
                    elif Q5=='2':#Question 5 Part 2
                        print('He got the small goblin that can steal gold for him after he')
                        print()
                        print('goes to erebor')                     
                    elif Q5=='3':#Question 5 Part 3
                        print('Dumbledore gains +100 gold and')
                        print()
                        print('goes to erebor')                   
                    elif Q5=='4':#Question 5 Part 4
                        print('Dumbledore is suspicious about the bag and dosent open it and')
                        print()
                        print('goes to erebor')
                    elif Q5=='5':#Question 5 Part 5
                        print('He opens the bag and finds a lucky stone and gets +10 intelligence and +200 gold and then')
                        print()
                        print('goes to erebor')                       
                elif Q4=='4':#Question 4 Part 4
                    print('Dumbledore rushed downstairs and thanks to his great luck he found a portal and heard the voice of gandalf telling him to go inside dumbledore')
                    print()
                    print('\njumped into the portal \nkept heading downstairs')
                    print()
                    Q5=input('Press 1 jumped into the portal or press 2 kept heading downstairs:')
            elif Q3=='2':#Question 3 part 2
                print('Dumbledore without thinking about it opens the cell door immediately. The guards hear him and capture him')
                print()
                print('Our hero died age 134')
        elif Q2=='2':#Question 2 part 2
            print('Dumbledore casted a spell to open the cell door it worked but the orc guards heard the big blast and started chasing him Dumbledore could go \nupstairs and propably leave the underground fortress \ndownstairs and propably be captured')
            print()
            Q3=input('Press 1 upstairs and propably leave the underground fortress or press 2 downstairs and propably be captured:')
            if Q3=='1':#Question second 3 Part 1
                print('Dumbledore rushed upstairs and went outside the fortress and found a bag this bag was sent by Gandalf and he could ony choose one item')
                print()
                print('\nMagic wand \nSmall goblin \nPouch of gold \nNothing might be a trap \Lucky stone')
                print()
                Q4=input('Press 1 Magic wand press 2 Small goblin press 3 Pouch of gold press 4 nothing might be a trap or press 5 lucky stone:')
                if Q4=='1':#Question second 4 Part 1
                    print('He chose the magic wand and has +1 intelligence he can kill foes easier and can become invisible.After he picks up the wand he')
                    print()
                    print('Goes to erebor')
                elif Q4=='2':#Question second 4 Part 2
                    print('He got the small goblin that can steal gold for him after he')
                    print()
                    print('Goes to erebor')
                elif Q4=='3':#Question second 4 Part 3
                    print('Dumbledore gains +100 gold and')
                    print()
                    print('He goes to erebor')
                elif Q4=='4':#Question second 4 Part 4
                    print('Dumbledore is suspicious about the bag and dosent open it and then')
                    print()
                    print('goes to erebor')
                elif Q4=='5':#Question second 4 Part 5
                    print('He opens the bag and finds a lucky stone and gets +10 intelligence and +200 gold and then')
                    print()
                    print('goes to erebor')
            elif Q3=='2':#Question second 3 Part 2
                print('Dumbledore rushed downstairs and thanks to his great luck he found a portal and heard the voice of gandalf telling him to go inside dumbledore')
                print()
                print('\njumped into the portal \nkept heading downstairs')
                print()
                Q4=input('Press 1 for jumped into the portal or 2 kept heading downstairs:')
                if Q4=='1':#Question Third 4 Part 1
                    print('Dumbledore jumped into the portal and found himself right outside erebor so he')
                    print()
                    print('goes to erebor')
                elif Q4=='2':#Question Third 4 Part 2
                    print('Dumbledore kept heading downstairs and finds a prison and he sees legolas and')
                    print()
                    print('\ndecides to free him \ndecides not to take him(legolas will remember that)')
                    print()
                    Q5=input('Press 1 Decides to free him or press 2 decides not to take him(legolas will remember that)')
                    if Q5=='1':#Second Question 5 part 1
                        print('Dumbledore decides to free him and then he')
                        print()
                        print('Goes back to the portal')
                        print()
                        print('Legolas and dumbledore go back into the portal and they decide to jump into the portal')
                        print()
                        print('The portal leaves Dumbledore and Legolas right outside erebor so legolas and dumbledore goes to erebor')
                    elif Q5=='2':#Second Question 5 part 2
                        print('Dumbledore decides not to free him and goes into the portal')
                        print()
                        print('Dumbledore goes back to the portal and jumps on it')
                        print()
                        print('Dumbledore jumped into the portal and found himself right outside erebor so he goes to erebor')
    elif Q1=='2':#Question 2 Part 2
        count=2
        print('Dumbledore stayed for the rest of his life in prison and never saw the light of the sun again.')
  

        
    

