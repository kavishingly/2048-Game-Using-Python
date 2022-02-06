# Creating temporary filled board
import random
from unicodedata import numeric


board=[]
n=4 #size of n X n
#display the board
def display():
    #print correctly, adding spaces equal to the len of largest number
    mx=board[0][0]
    #finding max elem
    for i in board:
        for  element in i:
            mx=max(mx,element)
    spaces=len(str(mx))

    for row in board:
        currentRow="|"
        for elem in row:
            #if element is 0 then print space, else the number itself
            if not elem:
                currentRow+=" "*spaces +"|"

            else:
                currentRow+=" "*(spaces-len(str(elem)))+str(elem)+"|"
        print(currentRow)
    print()

# display()
# Merging function 
def mergeOneRowLeft(row):
    #move elements
    for j in range(n-1):
        for i in range(n-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    #now combining the element of same value
    for i in range(n-1):
        if row[i]==row[i+1]:
            row[i] *=2;
            row[i+1]=0
    #moving to left once again
    for i in range(n-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
    return row

def merge_left(currBoard):
    for i in range(n):
        currBoard[i]=mergeOneRowLeft(currBoard[i])
    return currBoard

def merge_right(currBoard):
    for i in range(n):
        currBoard[i]=currBoard[i][::-1]
        currBoard[i]=mergeOneRowLeft(currBoard[i])
        currBoard[i]=currBoard[i][::-1]
    return currBoard

def transpose(currB):
    for i in range(n):
        for j in range(i,n):
            if not i==j:
                temp=currB[i][j]
                currB[i][j]=currB[j][i]
                currB[j][i]=temp
    return currB

def merge_up(currBoard):
    currBoard=transpose(currBoard)
    currBoard=merge_left(currBoard)
    currBoard=transpose(currBoard)
    return currBoard

def merge_down(currBoard):
    currBoard=transpose(currBoard)
    currBoard=merge_right(currBoard)
    currBoard=transpose(currBoard)
    return currBoard


#function to return 2 or 4 randomly such that 1/8 return 4 and 7/8 return 2
def newVal():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2


#creating blank board
board=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    board.append(row)

#fill two spots
numReq=2
while numReq > 0:
    rowNum = random.randint(0,n-1)
    colNum = random.randint(0, n-1)
     
    if board[rowNum][colNum] == 0:
        board[rowNum][colNum]=newVal();
        numReq -=1

print("\n\nWelcome to 2048. Type '1' to merge left, '2' to merge right, '3' to merge up and '4' to merge down.\n\nHere is the starting board:")

display()

    
gameOver = False
 
while not gameOver:
    move = input("Which you want to move? ")

    validMove =True

    if move =="1":
        board = merge_left(board)
    elif move =="2":
        board = merge_right(board)
    elif move =="3":
        board = merge_up(board)
    elif move =="4":
        board = merge_down(board)
    else:
        validMove=False
    if not validMove:
        print("Enter valid input!")
    else:
        display()
