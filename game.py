import random
import app
import role1
import role2



def pick_role():
    x= -1
    while x != 20:
        print("Select a role:")
        select_character = input("King or Queen").lower()  # input choices as King or Queen
        if select_character == "king" or select_character == "queen": # if positive and negative
        # if they give proper response
            print("Your character is " + select_character) 
            x= 20
            return select_character
        else: 
            print("Invalid Input")



def roll_dice():
    # random = random.randit(1,6)
    # return random
    return random.randint(1, 6)

def challenges():
    role = pick_role()
    strength = -100
    dexterity = -100
    intelligence = -100
    hp = -1
    if role == "king":
        strength = role1.strength
        dexterity = role1.dexterity
        intelligence = role1.intelligence 
        print("your strength is = " + str(strength), "Your dexterity is = " + str(dexterity), "Your intelligence is = " + str(intelligence))
        #print("your strength is = " + strength, "Your dexterity is = " + dexterity, "Your intelligence is = " + intelligence)
        #role1.king
    else:
          strength = role2.strength
          dexterity = role2.dexterity
          intelligence = role2.intelligence 
    print("your strength is = " + str(strength), "Your dexterity is = " + str(dexterity), "Your intelligence is = " + str(intelligence))

    #print("your strength is = " + strength, "Your dexterity is = " + dexterity,  "Your intelligence is = " + intelligence, end= "")
    
    def challenge_1():
        myRoll = roll_dice()
        print(" welcome to challenge 1 ")
        print(" May we see if you are worthy for the rest of the trials..  ")
        print(input(" please enter a key to continue "))
        if myRoll < 2:
            print("Critical Loss!")
            strength -= 1
        elif myRoll < 3:
            print("Loss!")
            # nothing happens to stats
        elif myRoll < 4:
            print("Win!")
            # nothing happens to stats, meaning they werent hurt in challenge
        else:
            print("Critical Win!")
            strength += 1
    
        challenge_2()
        return strength
        
        # challenge 2 int
        # intellingence challenge 
    def challenge_2():
        myRoll = roll_dice()
        print("This is the intelligence challenge")
        print(input(" please enter a key to continue "))
        if myRoll < 2:
            print("Critical Loss!")
            intelligence -= 1
        elif myRoll < 3:
            print("Loss!")
            # nothing happens to stats
        elif myRoll < 4:
            print("Win!")
            # nothing happens to stats, meaning they werent hurt in challenge
        else:
            print("Critical Win!")
            intelligence += 1
        
        challenge_3()
        
        return intelligence

    # this is a challenge for dexterity
    def challenge_3():
        myRoll = roll_dice()
        print("This is the Dexterity challenge")
        print(input(" please enter a key to continue "))
        if myRoll < 2:
            print("Critical Loss!")
            dexterity -= 1
        elif myRoll < 3:
            print("Loss!")
            # nothing happens to stats
        elif myRoll < 4:
            print("Win!")
            # nothing happens to stats, meaning they werent hurt in challenge
        else:
            print("Critical Win!")
            dexterity += 0
        
        return dexterity
    
 
    if strength > 1:
        print("You have passed the strength trial")
    else:
        print("you have not passed the strength trials")
        
        if intelligence > 1:
            print("you have passed the intelligence trial aswell")
        else:
            print("you have not passed the intelligence trial")

            if dexterity > 0:
                print("you have passed the dexterity trials")
            else:
                print("sadly you have not passed the dexterity trial")
    
        
    




def main():
    pick_role()
    roll_dice()
    challenges()


if __name__ == "__main__":
    main()


