import random

List=['rock', 'scissor','paper']

while True:
    Ccount=0
    Ucount=0
    GameInput=input('''
Game is start...
If you are continue in game so enter(Y/y)other wise enter else: 
    ''')

    if GameInput=='Y' or GameInput=='y':

        for i in range(0,5):
                UserInput=int(input('''
    Enter 1 For Rock
    Enter 2 For Scissor
    Enter 3 For Paper
            '''))
                if UserInput>=1 and UserInput<=3:
                    if UserInput==1:
                        UserChoice='rock'
                    elif UserInput==2:
                        UserChoice='scissor'
                    elif UserInput==3:
                        UserChoice='paper'
                        
                    ComChoice=random.choice(List)
                    if UserChoice==ComChoice:
                        print("Game is draw")
                        print("User choice value is : ",UserChoice)
                        print("Computer choice value is : ",ComChoice)
                        Ccount=Ccount+1
                        Ucount=Ucount+1

                    elif ((UserChoice=='rock' and ComChoice=='scissor')or (UserChoice=='paper' and ComChoice=='rock') or (UserChoice=='scissor' and ComChoice=='paper')):
                        print("User choice value is : ",UserChoice)
                        print("Computer choice value is : ",ComChoice)
                        print("User win this Round")
                        Ucount=Ucount+1

                    else:
                        print("User choice value is : ",UserChoice)
                        print("Computer choice value is : ",ComChoice)
                        print("Computer win this Round")
                        Ccount=Ccount+1

                else:
                    print("Invalid choice")
                

        if Ucount==Ccount:
            print("Final game is draw")
            print("User score is : ",Ucount)
            print("Computer score is : ",Ccount)
        elif Ucount>Ccount:
            print("Final User win the game")
            print("User score is : ",Ucount)
            print("Computer score is : ",Ccount)
        else:
            print()
            print("Final Computer win the game")
            print("User score is : ",Ucount)
            print("Computer score is : ",Ccount)
        
            
    else:
        print("Thank you")
        break