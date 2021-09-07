from chapter1 import ch1
def start(): 
    print("Blackshirts & Reds... The Game\n")
    startVar = int(input("START: 1"))
    if startVar == 1:
        ch1()
    else:
        start()