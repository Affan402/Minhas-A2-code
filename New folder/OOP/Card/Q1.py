StackPointer = 0
StackData = [0] *10

def printArray():
    global StackPointer, StackData
    print("StackPointer:",StackPointer)
    
    for x in range(0, 10):
        print(StackData[x])

def Push(item):
    global StackPointer, StackData
    if StackPointer == 10:
        return False
    else:
        
        StackData[StackPointer] = item
        StackPointer += 1
        return True

for x in range(0, 11):
    num = int(9)
    if Push(num) == True:
        print("Item added")
    else:
        print("Item not added")
                   

def Pop():
    global StackData, StackPointer
    
    if StackPointer == 0:
        return -1
    else:
        
        StackData[StackPointer-1] =0
        StackPointer -= 1
        
Pop()
Pop()
printArray()        