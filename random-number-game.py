import random

computer_num=random.randint(1, 100)
tries=0
win=0
repeat="Οχι"

#print(computer_num)
while True :
    if repeat=="Ναι" :
        computer_num=random.randint(1, 100)
        #print(computer_num)
        repeat="Οχι"
        pass
    user_num=int(input("Μαντεψε τον αριθμο απο το 1-100:"))
    while user_num<1 or user_num>100 :
        print("Μην ξεχνας απο το 1-100.")
        break
    else :
        while user_num!=computer_num :
            if user_num<computer_num :
                print("ΟΧΙ ειναι μεγαλυτερο")
                tries+=1
                break
            elif user_num>computer_num :
                print("ΟΧΙ ειναι μικροτερο")
                tries+=1
                break
    if user_num==computer_num :
        print("Το βρηκες με {} προσπαθειες.".format(tries))
        win+=1
        tries=0
        repeat=(input("Να ξανα παιξουμε:(Ναι/Οχι)"))
        if repeat=="Οχι" :
            print("Κερδισες {} ποντους \nGoodbye!!".format(win))
            break
