import re
import os
import time

def display(a): #Funtion to display the hanged man
    for i in a:
        for j in range(10):
            if j<9:
                print(i[j],end="")
            else:
                print(i[j])
    
def hang(k): #Function to decide the hanged man
    a = [[" "," "," ","+--","--","--","+","  ","  "," "],
        [" ","  ","|","  ","  ","  ","|","  ","  "," "],
        [" ","  "," ","  ","  ","  ","|","  ","  "," "],
        [" ","  "," ","  ","  ","  ","|","  ","  "," "],
        [" ","  "," ","  ","  ","  ","|","  ","  "," "],
        [" ","  "," ","  ","  ","  ","|","  ","  "," "],
        [" ","  "," "," -","--","--","+","--","--","-"]]

    if k==0:
        display(a)
    elif k==1:
        a[2][2]="O"
        display(a)
    elif k==2:
        a[2][2]="O"
        a[3][2]="|"
        display(a)
    elif k==3:
        a[2][2]="O"
        a[3][2]="|"
        a[3][1]=" /"
        display(a)
    elif k==4:
        a[2][2]="O"
        a[3][2]="|"
        a[3][1]=" /"
        a[3][3]="\ "
        display(a)
    elif k==5:
        a[2][2]="O"
        a[3][2]="|"
        a[3][1]=" /"
        a[3][3]="\ "
        a[4][1]=" /"
        display(a)
    elif k==6:
        a[2][2]="O"
        a[3][2]="|"
        a[3][1]=" /"
        a[3][3]="\ "
        a[4][1]=" /"
        a[4][3]="\ "
        display(a)

def index(x,y): #Funtion to return the indices of a specific letter
    indices = [i.start() for i in re.finditer(y,x)]
    return indices

def update(word,v,letter): #Function to update the list to display a specific letter at all indices
    ind=index(word,letter)
    for i in ind:
        v[i]=word[i]
    return v


def check_name(x,name): #Function to check if the word entered by Player2 matches with the word entered by Player 1
    if x==name:
        return True
    else:
        return False

def check_letter(x,letter): #Function to check if the letter entered by Player 2 is present in the word entered by Player 1
    if letter in x:
        return True
    else:
        return False
    
def game(): #Function to call the game
    
    #Description of the game
    print("")
    print("HANGMAN GAME")
    print("")
    print("Rules : ")
    print("->This is a user vs user game")
    print("->One user(Player 1) will input the word and the second user(Player 2) will try guessing the word")
    print("->In the word entered by Player 1 , all the letters except the vowels will be blank so Player 2 can guess the word")
    print("->Player 2 will get two options\n  -To guess the word\n  -To guess a letter")
    print("->The Player 2 can use these two options to guess the word entered by Player 1")
    print("->Player 2 will get a total of 6 chances(the number of chances decrease by 1 with every wrong guess)")
    print("->Once the number of chances reaches 0 and Player 2 still hasnt guessed the word entered by Player 1, It means that Player 2 lost and Player 1 has won")
    print("->With every wong guess the hangman picture becomes a whole, once the chances become 0 , we can see a man figure being hanged meaning game over")
    print("->These are the basic rules of the game, Enjoy!!\n")

    print("Player 1 will start\n")
    n=input("Enter the word to be guessed : ").upper()

    os.system('CLS');

    x=n.strip().split(" ")
    w=[]
    v=[]
    v.append("|")

    word="|"
    for i in x:
        word=word+i+"|"

    for i in x:
        for j in i:
            v.append("_")
        v.append("|")

    vowel=["A","E","I","O","U"]
    for i in vowel:
        v=update(word,v,i)
    k=0

    while 1: #Menu driven program for Player 2
        if k<6:
            print("\n\n")
           # print("------------------------------------------")
            hang(k)
            print("")
            for i in v:
                print(i,end=" ")
    
            print("\n\n")
            print("Choose the operation to perform : ")
            print("   1.Guess the word")
            print("   2.Check if the letter is present")
            op=input("Choose the operation (Enter 1 or 2) : ")

            if op=="1" or op=="2":
                if op=="1":
                    guess_name=input("Enter the word : ").upper()
                    if check_name(n,guess_name)==True:
                        print("\n")
                        print("Correct Guess")
                        print("PLAYER 2 WINS!!!")
                        print("\n")
                        break
                    elif check_name(n,guess_name)==False:
                        k=k+1
                        print("Wrong Guess,Try again!!!")

                elif op=="2":
                    guess_letter=input("Enter the letter : ").upper()
                    if check_letter(n,guess_letter)==True:
                        print("Yes,The letter present in the word!!!")
                        v=update(word,v,guess_letter)
                    elif check_letter(n,guess_letter)==False:
                        k=k+1
                        print("No,The letter is not present in the word,Try again!!!")
            else:
                print("Incorrect Input,Try again!!!")
        else:
            print("\n")
            hang(k)
            print("\nOpps,Run Out Of chances")
            print("PLAYER 1 WINS!!!")
            print("\n")
            break


#Driver code
os.system('CLS');
game()

while 1:
    fop=input("Do you want to play a new match?? (YES|NO) : ").upper()
    if fop=="YES":
        os.system('CLS');
        print("NEW GAME!!!")
        game()

    elif fop=="NO":
        print("THANK YOU")
        break

time.sleep(5)
os.system('CLS')
