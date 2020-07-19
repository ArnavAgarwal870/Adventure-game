import random

p=0
flag=0
flag1=0
FlagReplay=True
movement=[]
l=0
lstr=[]


rooms={(0,0,0):'field',(1,0,0):'ground floor staircase',(2,0,0):'canteen',(1,0,1):'first floor staircase',(1,0,2):'second floor staircase',(0,1,0):'ground floor staffroom ',(1,1,0):'basketball court',(2,1,0):'Gandhi Area',(1,2,0):'Main Gate',(2,2,0):'Science park',(0,1,1):'first floor staffroom '}
lstr=['psycho lab','rep table','CS lab','classroom','male washroom','physics lab','chemistry lab','junior library','middle library','senior library','art room','Mac lab','Yoga room','discovery lab','female washroom','dance room']

while FlagReplay==True:
    Help=input("Do you want to print Help?[Y/N]")
    if Help== "Y":
        print('''
Hello! Welcome to DPS Sec45,you are Arnav Agarwal a student of class XI J who is late in submitting
his CS project to Chanchal Ma'am.
you are in a random room in any of the three floors of this school and are supposed to submit 
the project and return to class safely.
But it  is not all a safe passage! If youo run into Chanchal ma'am twice you get caught for bunking
and lose if Shraddha ma'am sees you and you run into her:
a)by trying to go in a direction there isn't a room? GAME OVER
b)by backtracking into a room you were already in the move before? GAME OVER
but don't worry shraddha ma'am will not chase you forever and will stop after a few turns
You can also go to the floor above or below using the staircases
HOW TO PLAY:
N:North
S:South
E:East
W:West
U:Upper Floor
L:Lower Floor
Helpful Tip: the staircases are always below one another, You'll soon know how this helps:)
             You'll also need a pen and paper
                                               Good Luck!!!
                ''')

    elif Help== "N":
        print("                                Good Luck!!!")

    else:
        print("enter valid input")
              
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if (i,j,k) not in rooms:
                    t=random.choice(lstr)
                    if t=='classroom':
                        w=(i,j,k)
                    rooms[(i,j,k)]=t
                    lstr.remove(t)

    x=random.randint(0,2)
    y=random.randint(0,2)
    z=random.randint(0,2)
    teacherpos=(x,y,z)

    a=random.randint(0,2)
    b=random.randint(0,2)
    c=random.randint(0,2)

    st_pos=(a,b,c)
    print("You are starting from ",rooms[st_pos])

    movement.append(st_pos)
    coord=(a,b,c)

    delivered=False

    while delivered==False or (a,b,c)!=w:
        ch=input("Enter direction (N,S,E,W,U,L)")

        if ch=='N':

            if b==2:
                print("there is nowhere to go")

            else:
                b+=1

        elif ch=='S':

            if b==0:
                print("there is nowhere to go")

            else:
                b-=1

        elif ch=='E':

            if a==2:
                print("there is nowhere to go")

            else:
                a+=1

        elif  ch=='W':

            if a==0:
                print("there is nowhere to go")

            else:
                a-=1

        elif ch=='U' and a==1 and b==0:

            if c==2:
                print("there is nowhere to go")

            else:
                c+=1

        elif ch=='L' and a==1 and b==0:

            if c==0:
                print("there is nowhere to go")

            else:
                c-=1

        else :
            print("Invalid choice")
            continue
            coord=(a,b,c)
        movement.append(coord)

        if len(movement)>=7 or delivered==True and flag1==0:
            x1=random.randint(1,4)

            if x1==3:
                y1=random.randint(3,6)
                flag1=1
                l=0

        elif flag1==1:

            if movement[len(movement)-1]==movement[len(movement)-2] or movement[len(movement)-1]==movement[len(movement)-3]:
                flag=2
                break
            l+=1

        if flag1==1 and l==y1:
            flag1=0
            l=0
            y1=0
            print("You have escaped from Shradha ma'am <for now>!")

        if flag1==1 and l==0:
            print("Shradha Ma'am has seen you. Better not run into her!")
        print("You are in ",rooms[a,b,c])

        if flag1==1 and l!=y1:
            print("Shradha ma'am is coming after you. Keep moving")

        if (a,b,c)==(x,y,z):
            p+=1

            if p==1:
                delivered=True
                print("You have delivered the project. Now go back to class")

            elif p==2:
                flag=1
                break
    if flag==0:
        print("Congratulations, you have successfully delivered the project and returned.")

    elif flag==1:
        print("You were caught by Chanchal ma'am for bunking. You were taken to Headmistress maam\nand given a yellow card.\n                   YOU LOSE!!!!!")

    elif flag==2:
        print("You  were caught by Shradha ma'am for bunking. You were taken to Headmistress maam\nand given a yellow card.\n                   YOU LOSE!!!!!")
    
    while True:
        a=input("Do you want to play again?[Y/N]")

        if a == "Y":
            break

        elif a == "N":
            FlagReplay=False
            break

        else:
            print("Enter valid input")

        
