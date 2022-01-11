# © author : riishiiraz

import Calculator as calc


operations = ["Addition", "Subtraction", "Multiplication", "Division", "Quotient", "Remainder",
              "FactAdd", "Power", "Natural-Log", "Log10", "Log2", "Square-Root", "Factorial", "Exit"]

def showMsg(operations = operations):
    

    nums = iter(range(1,len(operations)+1))

    msg = "\n".join(["Enter %d for %s"%(next(nums) , x) for x in operations])

    msg="\n"+msg
    print (msg , end = "\n\n")

    option = int(input ("Enter Option : "))

    return option

def askForInput (option):
    
    operation = operations[option-1]

    noOfInput = 1 if operation in ["FactAdd", "Natural-Log", "Log10", "Log2", "Factorial"] else 2

    if (noOfInput==1):
        inp = ( int(input("Enter The Input for %s : "%(operation))) ,)
    else:
        inp = (int(input("Enter A For %s : "%operation)) ,
               int(input("Enter B For %s : "%operation)) )

    print()

    return inp

def getResult(option ,inputs):

    dict_funcs = {1:calc.sum_, 2:calc.subtrac, 3:calc.multi, 4:calc.divi, 5:calc.quotient, 6:calc.remainder, 7:calc.factadd, 8:calc.power, 9:calc.naturalog,
                  10:calc.logb10, 11:calc.logb2, 12:calc.squareroots, 13:calc.factr}
    

    function = dict_funcs [option]

    print()
    return function(*inputs)
    

option = None
while option != len(operations) :

    option = showMsg()

    inputs = (askForInput(option))

    result = getResult(option , inputs)

    askForAgain = input("\nWant to use again [Y/N] : ")

    if (askForAgain.upper() != "Y"):
        break

    
    

        


    
