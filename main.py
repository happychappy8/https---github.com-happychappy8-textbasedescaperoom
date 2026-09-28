def chapter1():
    print("you wake up in a room not knowing who you are and what you are doing thereyou see 3 doors and look through the key hole to see")
    print("through the firs is  a lion who clearly hasn't eaten for more than 14 days,the next is a river of lava,and third you see an empty room")
    choice = input("so what will it be? A:the first door B:the second door C:the third door?")
    if choice == "a":
        print("you briskly walk past the dead lion on the floor as the room at this point has a horrid odour")
        return True
    if choice.lower == "b":
        print("you see a rock floating down stream and jump on it trying to get to the other side ")
        print("you only end up melting your shoes and slip and fall into the molten lava")
        print("you have died")
        return False
    if choice == "c":
        print("you enter the room and nothing happens you look around the room and suddenly you see a figure")
        print("the figure walks towards you and hits you over the head it goes black")
        pass
def chapter2(i):
    if i == True:
        print("you walk through the door on the opposite side of the room")
        print("you see on the other side a card and a abicus the card says what is 3000 X 200 ")
        choice = input("the answer is:")
        if choice == "600000":
            print("well done!the adacuss starts to glow and you see a flash of light and you are teleported to a new room")
            return True
        else:
            print("your math needs alot of improvement!the card glows red and it explodes")
            print("you died!")
            return False
    if i == False:
        pass
def chapter3(i):
    if i == True:
        print("this room has a small man sitting calmly almost like he was expecting you and he says to you:")
        print("what do you seek but never find something money can never buy?")
        choice = input("there are 3 possible answers 1 is love 2 is happiness 3 is health")
        if choice == "2" or choice == "3":
            print("he slowly smiles and pulls a lever you fall down a trap door!")
            return True
        else:
            print("he looks at you sadly and you look down in shame wishing you could go back in time")
            return False
    if i == False:
        pass
def chapter4(i):
   if i == True:
        print("you are sliding down a metal chute in the dark!you finally come to a room,slightly daized you sit up to see a mirror")
        print("oooh my goodness you look terrible you look like yo haven't showered for days!Then the mirror starts to distort")
        print("you see a distorted face and here a loud booming voice")
        name = input('"What is your name young lad?"')
        if name == "":
            print("you remain silent and the mirrors face looks angry!it goes pitch black")
            chapter1()
        else:
            print(f"well hello their {name} it has been a while since we have met!Do you remember me.")
            choice = input("you are nervous you dont remember so you have 2 options Yes(lie) or No(Truth)")
            if choice == "lie" or "yes":
                print(f"He smile sand laughs and looks at you then he goes angry and he says {name} why did you lie i can smell peoples lies?")
                chapter1()
            if choice == "no" or "truth":
                print('he looks at you shiftily and gives a stiff laugh and says "you shoud be on your way" and you see a door apear and go through it')
        if i == False:
            print("you died")
            pass

        
chapter4(chapter3(chapter2(chapter1())))