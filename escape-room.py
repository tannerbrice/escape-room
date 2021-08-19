#Escape Room game
##Coding Goal1- To experiment with going back and forth to different "areas" where the variables change and unlock new options
##Coding Goal2- To gain equipment, and adding them to a list. Then being able to combine them into new items.


#change "under" section for socks after you take shoes off
#check out using items on the grate
#ruby stays in inventory after using it on gargoyle
#gargoyle main message appears too much after getting ruby and when using items
#add name to end message
#think about personalized password


#Imports
from time import sleep

#Main Function of Game
def main():

    #Variables
    name = None
    moveon = False
    itemsmoveon = False
    freedom = False
    choice = True
    takenapart = False
    ruby = False
    boxopenned = False
    done = False
    itemsdone = False
    location = None
    itemone = None
    itemtwo = None
    usedone = True
    namedone = False

    #Inventory
    inventorydict = {}

    #Introduction
    while namedone == False:
        name = input("""
            What is your name?
        """)
        print(f"""
            Hello {name}! It's nice to meet you. I wish it were on better circumstances.
            It seems that right now you are stuck in a room.
        """)
        namedone = True
        sleep(2)


    #Move On prompt - what player returns to after investigating and interacting
    while freedom == False:
        location = None
        print("""
            The room is poorly lit. It is roughly 4 meters by 4 meters. There is a door across from you,
            a gargoyle statue behind you, a painting of an old landscape to your right, an iron grate
            on the floor against the wall to your left and a cardboard box sitting to your left.
            The room is lit by a single light behind a textured glass on the ceiling.
            You are wearing jeans, a t-shirt, and gym shoes.
        """)
        sleep(3)
        personsays = input(f"""
            What would you like to to investigate, {name}?
            (door, statue, painting, grate, box, light, clothes, inventory)
        """).lower()

        if personsays == "door":
            freedom = door(freedom)
        elif personsays == "light":
            inventorydict = light(inventorydict)
        elif personsays == "painting":
            takenapart, inventorydict = painting(takenapart, inventorydict)
        elif personsays == "grate":
            location, inventorydict, ruby = grate(location, inventorydict, ruby)
        elif personsays == "box":
            location, inventorydict = box(location, inventorydict)
        elif personsays == "statue":
            location, inventorydict = statue(location, inventorydict)
        elif personsays == "clothes":
            location, inventorydict, name = clothes(location, inventorydict, name)
        elif personsays == "inventory":
            location, inventorydict = inventory(location, inventorydict)
        else:
            invalid()




#Functions
def invalid():
    print("""
        Sorry, can you repeat that?
    """)


def door(freedom):
    moveon = False
    while freedom == False and moveon == False:
        print("""
            The door is made of thick wood with a metal doorknob attached to a number keypad. The doorknob won't budge.
        """)
        sleep(2)
        personsays = input("""
        The keypad is a standard 9-digit pinpad:

        |||||||||
        |||123|||
        |||456|||
        |||789|||
        |||*0#|||
        |||||||||

        Want to enter a number? (yes/no)
        """).lower()
        if personsays == "yes":
            personsays = input("""
                Password:
            """).lower()
            if personsays == "12345":
                sleep(3)
                print("""
                    There is a sharp click and a high-pitched beep. The doorknob automatically turns.
                    The door slowly opens. You are free, enjoy it. It was nice to meet you!
                """)
                sleep(6)
                freedom = True
            else:
                sleep(3)
                print("""
                    "Errrr", there is a low buzz. The door is still locked.
                """)
                sleep(2)
        elif personsays == "no":
            print("""
                Ok, you can try again later.
            """)
            sleep(2)
            moveon = True
        else:
            invalid()
    return freedom


def light(inventorydict):
    moveon = False
    location = "light"
    while moveon == False and "flashlight" not in inventorydict.keys():
        personsays = input("""
            Above you in the center of the ceiling is a circular plate of textured glass. It is out of reach.
            Would you like to use anything to reach it? (inventory, box, gargoyle, no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "box":
            print("""
                The box seems sturdy enough to stand on. You step up and are in reach of the glass.
                The glass seems like it can be slid to the side, above the wood of the ceiling. As
                you slide the glass, the source of the light is revealed. It is a flashlight hanging
                from a thin string. You can easily tug the light and snap the string. Congratulations,
                you now have a flashlight. There doesn't seem to be anything else behind the glass.
            """)
            sleep(3)
            inventorydict["flashlight"] = True
            moveon = True
        elif personsays == "gargoyle":
            print("""
                While the gargoyle statue is certainly tall and sturdy enough to use, it is much too
                heavy to get directly under the light.
            """)
            sleep(2)
        elif personsays == "no":
            print("""
                Ok. You are free to investigate here again later.
            """)
            sleep(2)
            moveon = True
        else:
            invalid()

    if "flashlight" in inventorydict.keys() and moveon == False:
        print("""
            As you look up at the hole in the ceiling, it is clear there is no new items
            or clues to be gained.
        """)
        sleep(2)
    return inventorydict


def painting(takenapart, inventorydict):
    moveon = False
    location = "painting"
    while moveon == False and "code" in inventorydict:
        print("""
            Most of the painting, aside from the dog, is dissolved. Behind where the paint was is a number written in
            permanent marker: 12345
        """)
        sleep(2)
        moveon = True
    while takenapart == False and moveon == False:
        print("""
            On the wall is a 1 meter by .75 meter painting of a hillside during fall.
            There is a small cottage with light smoke coming from the chimney. 2 children
            seem to be playing with a dog by a stream that runs by the cottage. The sky is
            becoming sunset, emphasising the already turning leaves. The canvas has an old wooden frame
            that does not seem to be held together too tightly. The painting hangs on a single nail.
        """)
        sleep(5)
        personsays = input("""
            Would you like to use something in your inventory on the painting, check behind the painting, or take apart the frame?
            (inventory/behind/frame/no)
        """).lower()
        if personsays == "inventory":
            location, inventorydict = inventory(location, inventorydict)
            if "code" in inventorydict:
                moveon = True
        elif personsays == "behind":
            print("""
                You lift the the painting off of the nail. It's heavy, but managable.
                Putting it on the wall to examine it, you see that there are no markings or
                indications of clues on the back of the painting or on the wall. The nail is
                secure in the wall and messing with it seems to have no effect. It seems there is
                nothing to be gained. You place the painting back on the wall.
            """)
            sleep(5)
        elif personsays == "frame":
            takenapart = True
            print("""
                You first take the painting off the wall to deconstruct it. It's heavy, but managable.
                Putting it on the wall to examine it, you see that there are no markings or indications
                of clues on the back of the painting or on the wall. The frame is unsturdy and easily taken apart.
                On the inner sides of the wooden frame there are no markings of information, and there are
                no hidden items to be used.
            """)
            sleep(5)
        elif personsays == "no":
            print("""
                Ok, you can come back to the painting later.
            """)
            sleep(2)
            moveon = True
        else:
            invalid()
    while takenapart == True and moveon == False:
            print("""
                On the ground is the 1 meter by .75 meter painting that you have taken apart.
                The pieces of wooden frame rest on the ground and the canvas remains in tact.
                The painting is of a hillside during fall. There is a small cottage with light smoke
                coming from the chimney. 2 children seem to be playing with a dog by a stream that runs by
                the cottage. The sky is becoming sunset, emphasising the already turning leaves.
            """)
            sleep(5)
            personsays = input("""
                Would you like to use something in your inventory on the painting? (yes/no)
            """).lower()
            if personsays == "yes":
                location, inventorydict = inventory(location, inventorydict)
                if "code" in inventorydict:
                    moveon = True
            elif personsays == "no":
                print("""
                    Ok, you can come back to the painting later.
                """)
                moveon = True
                sleep(2)
            else:
                invalid()
    while moveon == False and "code" in inventorydict:
        print("""
            Most of the painting, aside from the dog, is dissolved. Behind where the paint was is a number written in
            permanent marker: 12345
        """)
        sleep(2)
    return takenapart, inventorydict


def grate(location, inventorydict, ruby):
    moveon = False
    location = "grate"
    while moveon == False and "flashlight" not in inventorydict.keys():
        print("""
            The iron grate on the floor and against the wall is .5 meters by .25 meters. It has 4 cm thick bars with
            about 6 cm of space between each bar. The angle of the light in the ceiling makes it
            impossible to see the bottom of wherever this grate leads.
        """)
        sleep(3)
        personsays = input("""
            Would you like to use anything in your inventory or try pulling the grate up? (inventory/pull/no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "pull":
            print ("""
                The grate secure on the floor and wont budge at all.
            """)
            sleep(2)
        elif personsays == "no":
            print ("""
                Ok, you can come back to the grate later.
            """)
            sleep(2)
            moveon = True
        else:
            invalid()
    while moveon == False and "flashlight" in inventorydict.keys() and "ruby" not in inventorydict.keys():
        print("""
            The iron grate on the floor and against the wall is .5 meters by .25 meters. It has 4 cm thick bars with
            about 6 cm of space between each bar. With the flashlight in your possesion, you can illuminate the space
            below the bars. There is a rectangular, concrete space 50 cm deep. At the bottom, you can see a red ruby
            collecting dust.
        """)
        sleep(4)
        personsays = input("""
            Would you like to use anything in your inventory or try pulling the grate up? (inventory/pull/no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "pull":
            print ("""
                The grate secure on the floor and wont budge at all.
            """)
            sleep(2)
        elif personsays == "no":
            print ("""
                Ok, you can come back to the grate later.
            """)
            sleep(2)
            moveon = True
        else:
            invalid()
    while moveon == False and "ruby" in inventorydict.keys():
        print("""
            After collecting the ruby from the grate, you can tell there is nothing else to be gained from
            examining the grate.
        """)
        sleep(2)
        moveon = True
    return location, inventorydict, ruby


def box(location, inventorydict):
    moveon = False
    location = "box"
    while "chewing gum" not in inventorydict.keys() and moveon == False:
        personsays = input("""
            There is a .5 meter by .5 meter sturdy, thick cardboard box on the ground. The top flaps of the box are
            closed but not secured by tape. Would you like to lift or open the box or use somehting in your
            in your inventory on the box? (lift/open/inventory/no)
            """).lower()
        if personsays == "lift":
            print("""
                You easily lift the box. It's not heavy. Other than the weight of the cardboard, it doesn't
                have any noticable added weight. Howwever, moving the box around you can hear the sliding of something
                inside of the box.
            """)
            sleep(3)
        elif personsays == "open":
            print("""
                You open the top flaps of the cardboard box. Inside the box is a small, red pack of chewing gum.
                There are several sticks of gum wrapped in foil. They are mint flavored. You take the pack of gum.
                Congratulations, you now have a pack of gum! And good thing, too. Depending on how long you'll be in
                here, your breath might begin to stink!
            """)
            sleep(4)
            inventorydict["chewing gum"] = True
        elif personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "no":
            print("""
                Ok, you can come back to the box later.
            """)
            sleep(2)
            moveon = True
    while "chewing gum" in inventorydict.keys() and moveon == False:
        personsays = input("""
            The .5 meter by .5 meter sturdy, thick cardboard box has been openned and is lying on the floor.
            Would you like to use anything in your inventory on the box? (inventory/no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "no":
            print("""
                Ok, you can come back to the box later.
            """)
            sleep(2)
            moveon = True
    return location, inventorydict


def statue(location, inventorydict):
    moveon = False
    location = "statue"
    while moveon == False and "vial" not in inventorydict.keys():
        print("""
            Across the room from the door stands a 2 meter tall gargoyle. It's a dark grey and made of some
            kind of stone. It's smooth and solid. It is incredibly heavy and cannot be moved. It has large
            folded wings at its back. The right arm is hanging to its side, ending in a clawed hand. The left arm
            is bent at the elbow with it's forearm parallel to the ground. The left hand is curled shut.
            It's face is menacing. It has lowered eyebrows as if it's concentrating. It's mouth is shut with two lower
            fangs peeking out from behind its lips. There is a large, shiny ruby sitting in one hollowed eye socket.
            The other socket is empty.
        """)
        sleep(5)
        personsays = input("""
            Would you like to use an item from your inventory on the gargoyle or climb on it? (inventory/climb/no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "climb":
            print("""
                You begin to climb onto the gargoyle. It can easily carry your weight. You step and grab different edges
                of the statue and end up on top of it. You've put weight on most of the statue and can be certain there is
                not some hidden lever or pressure plate.
            """)
            sleep(3)
        elif personsays == "no":
            print("""
                Ok, you can come back to the statue later.
            """)
            sleep(2)
            moveon = True
    while moveon == False and "vial" in inventorydict.keys():
        print("""
            Across the room from the door stands a 2 meter tall gargoyle. It's a dark grey and made of some
            kind of stone. It's smooth and solid. It is incredibly heavy and cannot be moved. It has large
            folded wings at its back. The right arm is hanging to its side, ending in a clawed hand. The left arm is
            is bent at the elbow with it's forearm parallel to the ground. The left hand is open and empty.
            It's face is menacing. It has lowered eyebrows as if it's concentrating. It's mouth is shut with two lower
            fangs peeking out from behind its lips. There are two, large rubies sitting in its hollowed eye sockets.
            It seems there is nothing else to be gained by inspecting the gargoyle.
        """)
        sleep(5)
        moveon = True
    return location, inventorydict


def clothes(location, inventorydict, name):
    moveon = False
    location = "clothes"
    while moveon == False and "shoelace" not in inventorydict.keys():
        personsays = input(f"""
            All of your clothes fit well. You are wearing wearing a white t-shirt with your name, {name}, printed in red on
            the front. Your jeans fit well and there is nothing in the pockets. You are not wearing a belt. You are wearing
            underwear and socks. The gym shoes you are wearing are grey with blue laces. Would you like to use anything in
            your inventory on your clothes, take apart your shoes, or inspect under your clothes?
            (inventory/shoes/under/no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "shoes":
            print("""
                You begin to take the shoes apart. You notice that there are no tags in the shoes.
                The soles of the shoes can be taken out. There seems to be nothing under the soles and no
                writing. The blue shoelaces are easily removed. Congratulation, you now have shoelaces in your inventory!
            """)
            sleep(3)
            inventorydict["shoelace"] = True
            personsays = input("""
                Is there more you want to do with your clothes? (yes/no)
            """).lower()
            if personsays == "yes":
                print("""
                    Ok, here's a quick explanation again:
                """)
                sleep(2)
            elif personsays == "no":
                print("""
                    Ok, you can return to inspecting your clothes later.
                """)
                sleep(2)
                moveon = True
            else:
                invalid()
        elif personsays == "under":
            done = False
            while done == False:
                personsays = input("""
                    What would you like to inspect under? (shirt/jeans/socks/underwear/done)
                    """).lower()
                if personsays == "shirt":
                    print("""
                        You take off your shirt and look at your chest, shoulders, and what you can see of your back.
                        There doesn't seem to be any markings and everything appears normal. It's a bit chilly in here
                        with your shirt off so you put it back on. Also, you don't know how long you'll be in here and you
                        might start to stink, so lets keep those pits covered.
                    """)
                    sleep(4)
                elif personsays == "jeans":
                    print("""
                        You take off your jeans and look at your legs. There doesn't seem to be any markings and everything
                        appears normal. But this is no time for a pants-off-dance-off. Feel free to celebrate how you will
                        once you are free.
                    """)
                    sleep(3)
                elif personsays == "socks":
                    print("""
                        You take off your shoes off and it feels great, as if you've had them on for quite a while.
                        You then take off your socks off. There doesn't seem to be any markings on or under your feet.
                        Hopefully you get out soon, there doesn't seem to be nail clippers.
                        The floor is a bit chilly on your feet, so for now, you put on your socks.
                    """)
                    sleep(4)
                elif personsays == "underwear":
                    print(f"""
                        {name}, You know I can see you, right? Well, I'm not gonna judge. However, the glare of the gargoyle intensifies.
                        You inspect underneath your underwear and everything seems to be where it should be and there are no new
                        markings or clues to be gathered. It's quite cold in here to be so bare. You cover back up.
                    """)
                    sleep(3)
                elif personsays == "done":
                    print("""
                        Ok, you can inspect later if you need/want to.
                    """)
                    done = True
                    sleep(2)
                else:
                    invalid()
        elif personsays == "no":
            print("""
                Ok, you can take a look at your clothes later.
            """)
            moveon = True
            sleep(2)
        else:
            invalid()
    while moveon == False and "shoelace" in inventorydict.keys():
        personsays = input(f"""
            All of your clothes fit well. You are wearing wearing a white t-shirt with your name, {name}, printed in red on
            the front. Your jeans fit well and there is nothing in the pockets. You are not wearing a belt. You are wearing
            underwear and socks. The gym shoes are taken apart and you have collected the blue laces. Would you like to use
            anything in your inventory on your clothes, or inspect under your clothes?
            (inventory/under/no)
        """).lower()
        if personsays == "inventory":
            inventory(location, inventorydict)
        elif personsays == "under":
            done = False
            while done == False:
                personsays = input("""
                    What would you like to inspect under? (shirt/jeans/socks/underwear/done)
                """).lower()
                if personsays == "shirt":
                    print("""
                        You take off your shirt and look at your chest, shoulders, and what you can see of your back.
                        There doesn't seem to be any markings and everything appears normal. It's a bit chilly in here
                        with your shirt off so you put it back on. Also, you don't know how long you'll be in here and you
                        might start to stink, so lets keep those pits covered.
                    """)
                    sleep(4)
                elif personsays == "jeans":
                    print("""
                        You take off your jeans and look at your legs. There doesn't seem to be any markings and everything
                        appears normal. But this is no time for a pants-off-dance-off. Feel free to celebrate how you will
                        once you are free.
                    """)
                    sleep(3)
                elif personsays == "socks":
                    print("""
                        You take off your shoes off and it feels great, as if you've had them on for quite a while.
                        You then take off your socks off. The floor is a bit chilly on your feet. There doesn't seem to be
                        any markings on or under your feet. Hopefully you get out soon, there doesn't seem to be nail clippers.
                    """)
                    sleep(3)
                elif personsays == "underwear":
                    print(f"""
                        {name}, You know I can see you, right? Well, I'm not gonna judge. However, the glare of the gargoyle intensifies.
                        You inspect underneath your underwear and everything seems to be where it should be and there are no new
                        markings or clues to be gathered. It's quite cold in here to be so bare. You cover back up.
                    """)
                    sleep(3)
                elif personsays == "done":
                    print("""
                        Ok, you can inspect later if you need/want to.
                    """)
                    sleep(2)
                    done = True
                else:
                    invalid()
        elif personsays == "no":
            print("""
                Ok, you can take a look at your clothes later.
            """)
            sleep(2)
            moveon = True
        else:
            invalid()
    return location, inventorydict, name


def examineitem(inventorydict):
    itemsdone = False
    while itemsdone == False:
        personsays = input("""
            What Item would you like to examine? ((enter specific item name)/done/item list)
        """).lower()
        if personsays == "flashlight":
            print("""
                The flashlight is 30 cm long, black, and metal. It has been sealed together and cannot
                be take apart. It appears to be doing fine on battery life. While weilding the torch,
                most of the room is illuminated.
            """)
            sleep(3)
        elif personsays == "ruby":
            print("""
                The ruby is 5 cm across and boasts a dark red hue. It is fabulously cut and with a bit of
                dusting, the gem shines. It must be worth a fortune...
            """)
            sleep(2)
        elif personsays == "shoelace":
            print("""
                The shoelace is blue and in good condition. It is roughly 70 cm long.
            """)
            sleep(2)
        elif personsays == "chewing gum":
            print("""
                The chewing gum is in small, blue packaging labelled "mint chewing gum".
                Inside, there are several sticks of gum wrapped in foil. They are indeed mint flavored.
            """)
            sleep(2)
        elif personsays == "shoelace with gum":
            print("""
                The blue, 70 cm shoelace now has sticky chewing gum globbed onto one end of the string.
                The gum will easily stick to most things.
            """)
            sleep(2)
        elif personsays == "vial":
            print("""
                This crystal vial sparkles under the light of the flashlight. It looks well-crafted and
                fragile. There is a viscous liquid within the vial. There is a cork-filled, crystal cap
                that can be removed to access the liquid.
            """)
            sleep(3)
        elif personsays == "item list":
            for key in inventorydict:
                print(f"{key}")
        elif personsays == "done":
            print("""
                Sure thing. You can examine later.
            """)
            sleep(2)
            itemsdone = True
        elif personsays == "code":
            print("""
                The number found on the painting was "12345".
            """)
            sleep(2)
        else:
            invalid()
    return inventorydict

def combine(inventorydict):
    itemone = None
    itemtwo = None
    itemsdone = False
    itemchosen = False
    itemone = input("""
        What is the first item you would like to combine?
    """).lower()
    while itemchosen == False:
        if itemone in ["flashlight", "ruby", "shoelace", "chewing gum", "shoelace with gum", "vial"]:
            print(f"""
                Got it. The first item is the {itemone}.
            """)
            sleep(2)
            itemchosen = True
        else:
            personsays = input("""
                Sorry, I don't understand what you wrote. Please you reselect the first item?
                Or you can type (done) if you're done combining items.
            """)
            if personsays in ["flashlight", "ruby", "shoelace", "chewing gum", "shoelace with gum", "vial"]:
                itemone = personsays
                print(f"""
                    Got it. The first item is the {itemone}.
                """)
                sleep(2)
                itemchosen = True
            elif personsays == "done":
                itemchosen = True
                itemsdone = True
            else:
                print(" ")
    itemchosen = False
    while itemsdone == False and itemchosen == False:
        itemtwo = input("""
            What is the second item you would like to combine?
        """).lower()
        while itemchosen == False:
            if itemtwo in ["flashlight", "ruby", "shoelace", "chewing gum", "shoelace with gum", "vial"]:
                print(f"""
                    Got it. The second item is the {itemtwo}.
                """)
                sleep(2)
                itemchosen = True
            else:
                personsays = input("""
                    Sorry, I don't understand what you wrote. Please you reselect the second item?
                    Or you can type (done) if you're done combining items.
                """)
                if personsays in ["flashlight", "ruby", "shoelace", "chewing gum", "shoelace with gum", "vial"]:
                    itemone = personsays
                    print(f"""
                        Got it. The second item is the {itemtwo}.
                    """)
                    sleep(2)
                    itemchosen = True
                elif personsays == "done":
                    itemchosen = True
                    itemsdone = True
                else:
                    print(" ")
    while itemsdone == False:
        if itemone == "chewing gum" and itemtwo == "shoelace":
            print("""
                You made something useful! You now have a shoelace with gum on one end that can stick to things.
            """)
            sleep(3)
            inventorydict["shoelace with gum"] = True
            del inventorydict["chewing gum"]
            del inventorydict["shoelace"]
        elif itemtwo == "chewing gum" and itemone == "shoelace":
            print("""
                You made something useful! You now have a shoelace with gum on one end that can stick to things.
            """)
            sleep(3)
            inventorydict["shoelace with gum"] = True
            del inventorydict["chewing gum"]
            del inventorydict["shoelace"]
        else:
            print("""
                It seems these items aren't able to be combined in a useful way.
                But good for you trying to be creative!
            """)
            print(2)
        itemsdone = True
    return inventorydict

def useitem(location, inventorydict):
    usedone = False
    while usedone == False:
        if not inventorydict:
            print("""
                You currently have no items to use.
            """)
            sleep(2)
            usedone = True
        while location == "painting" and usedone == False:
            personsays = input("""
                What Item would you like to use ((specific item name)/none)?
            """).lower()
            if personsays == "vial":
                print("""
                    You pour some of the liquid from the vial onto the painting. The paint starts
                    to dissolve and smear. You rub the liquid into the paint, dissolving the hillside,
                    dissolving the sunset, dissolving the painted children. The dog is fine, you don't
                    get liquid on the dog.

                    From behind the paint, a number is written in permanent marker: 12345
                """)
                sleep(6)
                inventorydict["code"] = True
                usedone = True
            elif personsays == "flashlight":
                print("""
                    You shine the flashlight on the painting. Unfortunately, the light does not reveal anything
                    through the paint.
                """)
                sleep(2)
            elif personsays == "ruby":
                print("""
                    The cut of the ruby seems to scratch the canvas a bit, but that's all.
                    Nothing new is learned by using the ruby
                """)
                sleep(2)
            elif personsays == "shoelace":
                print("""
                    Hm. I'm not too sure what you hoped to gain by using the shoelace. The painting can already
                    be hung on the nail without the help of the shoelace.
                """)
                sleep(2)
            elif personsays == "chewing gum":
                print("""
                    Well. Now you got some gum on the painting. That's great. Hopefully it's not worth much.
                    Nothing is gained from using the gum.
                """)
                sleep(2)
            elif personsays == "shoelace with gum":
                print("""
                    You have a canvas with a string attached to it using gum. What are you gonna do, fly it like a kite?
                    Unfortunately this does not get you any closer to escaping.
                """)
                sleep(2)
            elif personsays == "none":
                print("""
                    Ok, you can use an item later.
                """)
                sleep(1)
                usedone = True
            else:
                invalid()

        while location == "light" and usedone == False:
            personsays = input("""
                What Item would you like to use ((specific item name)/none)?
            """).lower()
            if personsays == "shoelace":
                print("""
                    You try to whip the shoelace up to the glass, but it won't stick to the glass and appears to be of no help.
                """)
                sleep(2)
            elif personsays == "chewing gum":
                print("""
                    You flick chewed up gum toward the ceiling, getting some stuck near the glass.
                    This really isn't helping.
                """)
                sleep(2)
            elif personsays == "shoelace with gum":
                print("""
                    You are able to stick the end of the shoelace to the light! Unfortunately, the light is too heavy.
                    When you pull, the gum stretches and tears apart. This won't help.
                """)
                sleep(2)
            elif personsays == "none":
                print("""
                    Ok, you can use an item later.
                """)
                sleep(2)
                usedone = True
            else:
                invalid()

        usechoice = False
        while location == "grate" and usedone == False:
            personsays = input("""
                What Item would you like to use ((specific item name)/none)?
            """).lower()
            while "flashlight" in inventorydict.keys() and usechoice == False:
                if personsays == "flashlight":
                    print("""
                        With the flashlight, you illuminate the space below the bars. There is a rectangular,
                        concrete space 50 cm deep. At the bottom, you can see a red ruby collecting dust. The flashlight is
                        too wide to fit through the bars and won't seem to be any more help.
                    """)
                    usechoice = True
                    sleep(3)
                elif personsays == "shoelace":
                    print("""
                        You slide the shoelace down between the bars. It reaches the ruby! However, the shoelace won't grip onto
                        the gem, even with a loop. You pull the string back up. You did not get the ruby.
                    """)
                    sleep(2)
                    usechoice = True
                elif personsays == "chewing gum":
                    print("""
                        You drop a piece of gum between the bars. it lands near the ruby, and now sits there to collect dust
                        like the gem. Nothing comes of this.
                    """)
                    sleep(2)
                    usechoice = True
                elif personsays == "shoelace with gum":
                    print("""
                        You carefully lower the shoelace between the bars with the gum stuck at its end. It gets closer
                        to the ruby... And you got it! The gum sticks onto the ruby. it's light enough to lift up without
                        stretching and losing the gum. Congratulations, you now have a ruby!
                    """)
                    sleep(3)
                    inventorydict["ruby"] = True
                    usedone = True
                    usechoice = True
                elif personsays == "none":
                    print("""
                        Ok, you can use an item later.
                    """)
                    sleep(2)
                    usedone = True
                    usechoice = True
                else:
                    invalid()
                    usechoice = True
            while "flashlight" not in inventorydict.keys() and usechoice == False:
                if personsays == "shoelace":
                    print("""
                        You wrap the shoelace around the bars to try and get leverage, but the bars just won't budge.
                    """)
                    sleep(2)
                    usechoice = True
                elif personsays == "chewing gum":
                    print("""
                        If you think grip strength is why you can't get the bars, gum isn't going to help. Best keep your
                        hands clean and try something else.
                    """)
                    sleep(2)
                    usechoice = True
                elif personsays == "shoelace with gum":
                    print("""
                        You lower the shoelace with gum at the end into the dark hole. It sticks to something! As you pull
                        it back out, you realise that it must be a wall, floor, or something stationary because all the gum stretched
                        and tore apart. Without light, this strategy will have you running out of gum before you achieve anything.
                    """)
                    sleep(3)
                    usechoice = True
                elif personsays == "none":
                    print("""
                        Ok, you can use an item later.
                    """)
                    sleep(2)
                    usedone = True
                    usechoice = True
                else:
                    invalid()
                    usechoice = True
            usedone = True

        while location == "box" and usedone == False:
            personsays = input("""
                What Item would you like to use ((specific item name)/none)?
            """).lower()
            if personsays == "vial":
                print("""
                    You pour some of the liquid from the vial onto the box. The box gets a little damp, but that's it.
                    I wouldn't waste more liquid on the box.
                """)
                sleep(2)
            elif personsays == "flashlight":
                print("""
                    You shine the light into the box. It can be used as an imaginery room where in your head you can escape...
                    from this room you really do need to escape. But it doesn't do anything to get you out quicker.
                """)
                sleep(2)
            elif personsays == "shoelace":
                print("""
                    The shoelace can be poked through the side of the box, or put in the box, or wrapped part way around the box...
                    But none of it seems to help the situation.
                """)
                sleep(2)
            elif personsays == "chewing gum":
                print("""
                    Now the box is sticky. Grreeeeeeaaaat.
                """)
                sleep(2)
            elif personsays == "shoelace with gum":
                print("""
                    You can now swing the box around like a flail! But the gum quickly tears and stretches, coming apart.
                    A different strategy is needed.
                """)
                sleep(2)
            elif personsays == "none":
                print("""
                    Ok, you can use an item later.
                """)
                sleep(2)
                usedone = True
            else:
                invalid()

        while location == "statue" and usedone == False:
            personsays = input("""
                What Item would you like to use ((specific item name)/none)?
            """).lower()
            if personsays == "vial":
                print("""
                    You pour some of the liquid from the vial onto the statue. the liquid makes the rubies shine a bit more,
                    but other than that, there is nothing to be gained from this.
                """)
                sleep(2)
            elif personsays == "flashlight":
                print("""
                    You shine the light straight up under the gargoyle's chin. Yikes, it's pretty spooky. It doesn't help
                    your situation, it only makes the whole thing a bit creepier.
                """)
                sleep(2)
            elif personsays == "ruby":
                print("""
                    You plae the ruby into the empty eye socket of the gargoyle. "Click". It secures in place.
                    There is a sound of scraping rock as the fingers on the left hand of the statue curl open, revealing
                    a crystal vial in it's palm. Congratulations, you now have what appears to be a very fragile container
                    with a cork and viscous liquid inside!
                """)
                sleep(4)
                inventorydict["vial"] = True
                usedone = True
            elif personsays == "shoelace":
                print("""
                    Ah, I see that you don't like that the gargoyle isn't wearing any clothes and want to give it
                    some of your own. Unfortunately, we all know that tiny of a string isn't going to help...
                """)
                sleep(2)
            elif personsays == "chewing gum":
                print("""
                    What do you think this is, the bottom of a school desk? Don't be sticking gum all over the statue.
                """)
                sleep(2)
            elif personsays == "shoelace with gum":
                print("""
                    You try to take out the ruby eye with the gum on the shoelace, but it's secure in there. This doesn't
                    do anything for you. Also, it's rude to steal people's eyes.
                """)
                sleep(2)
            elif personsays == "none":
                print("""
                    Ok, you can use an item later.
                """)
                sleep(2)
                usedone = True
            else:
                invalid()

        while location == "clothes" and usedone == False:
            personsays = input("""
                What Item would you like to use ((specific item name)/none)?
            """).lower()
            if personsays == "vial":
                print("""
                    You pour some of the liquid on your socks because you are an absolute sadist. You revel in your moist, rank,
                    feet cacoons. Do I even want you getting out of this room?
                """)
                sleep(2)
            elif personsays == "flashlight":
                print("""
                    You shine the flashlight on the painting. Unfortunately, the light does not reveal any hidden writings
                    or fabrics.
                """)
                sleep(2)
            elif personsays == "ruby":
                print("""
                    You can put the ruby in your pocket and in your socks or shoes. Are you trying to steal it?
                    None of this is furthering your goal.
                """)
                sleep(2)
            elif personsays == "shoelace":
                print("""
                    You just pulled your shoelace out of your shoe, you really want to waste time putting it back in?
                    You can relace when you're free.
                """)
                sleep(2)
            elif personsays == "chewing gum":
                print("""
                    This is one step away from putting the gum directly into your hair. Wait, forget I said that. Don't get any ideas.
                """)
                sleep(2)
            elif personsays == "shoelace with gum":
                print("""
                    Please, please don't put gum on your clothes. It's bad enough it's already on your shoelace.
                """)
                sleep(2)
            elif personsays == "none":
                print("""
                    Ok, you can use an item later.
                """)
                sleep(2)
                usedone = True
            else:
                invalid()
    return location, inventorydict

def inventory(location, inventorydict):
    itemsmoveon = False
    itemsdone = False
    while not inventorydict and itemsmoveon == False:
            print("""
                You currently have no items to use.
            """)
            sleep(2)
            itemsmoveon = True
    while itemsmoveon == False and location in ["light", "box", "clothes", "grate", "statue", "painting"]:
        print("""
            Here's what you have in your inventory:
            """)
        sleep(2)
        for key in inventorydict:
            print(f"{key}")
        personsays = input("""
            Would you like to use, examine, or combine items? (use/examine/combine/exit)
        """).lower()
        if personsays == "use":
            location, inventorydict = useitem(location, inventorydict)
        elif personsays == "examine":
            inventorydict = examineitem(inventorydict)
        elif personsays == "combine":
            inventorydict = combine(inventorydict)
        elif personsays == "exit":
            print("""
                Ok, you can check your inventory later.
            """)
            sleep(2)
            itemsmoveon = True
        else:
            invalid()
    while itemsmoveon == False and location == None:
        print("""
            Here's what you have in your inventory:
        """)
        sleep(2)
        for key in inventorydict:
            print(f"{key}")
        personsays = input("""
            Would you like to examine or combine items? (examine/combine/exit)
        """).lower()
        if personsays == "examine":
            inventorydict = examineitem(inventorydict)
        elif personsays == "combine":
            inventorydict = combine(inventorydict)
        elif personsays == "exit":
            print("""
                Ok, you can check your inventory later.
            """)
            sleep(2)
            itemsmoveon = True
        else:
            invalid()
    return location, inventorydict

main()


#Plan for the whole thing:
#Box has chewing gum inside
#Box is sturdy and can be stood on to reach light
#Glass can be removed. The light is a flashlight that can be taken to look in grate.
#In the grate there is something that needs to be seen with the flash light and grabbed with gum and shoelace
#Shoelace can be taken from shoes
#The gargoyle has one gem eye, other gem is in the grate. Both eyes open the hand
#Vial from gargoyle hand can be spread on painting to remove paint
#Behind the paint, the number is written
