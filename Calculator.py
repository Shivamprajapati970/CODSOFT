class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def Addition(self):
        self.add=self.num1 + self.num2
        print("Addition is : ",self.add)

    def Subtraction(self):
        self.add=self.num1 - self.num2
        print("Addition is : ",self.add)

    def Multiplication(self):
        self.add=self.num1 * self.num2
        print("Addition is : ",self.add)

    def Division(self):
        self.add=self.num1 / self.num2
        print("Addition is : ",self.add)

while(True):
    ans=input("If you are continue in program so enter(Y/y)other wise enter else: ")
    if ans=='Y' or ans=='y':
        num1=int(input("Enter First Number : "))
        num2=int(input("Enter Second Number : "))
        cal=calculator(num1,num2)
        print("""Enter choice :-
presse 1 for Addition of two number.
presse 2 for Subtraction of two number.
presse 3 for Multiplication of two number.
presse 4 for Division of two number.
              """)
        
        a=int(input("enter you choice : "))
        match a:
            case 1:
                cal.Addition( )
            case 2:
                cal.Subtraction()
            case 3:
                cal.Multiplication()
            case 3:
                cal.Division()
            case _:
                    print("Enter correct choice ")
    else:
        print("ok you are quit ")
        break;
    
