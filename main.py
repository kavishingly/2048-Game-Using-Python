# Creating temporary filled board
import random
import copy


board=[]
score=0
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
            global score
            score+=2*row[i]
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
#function to add a value to the board
def addVal():
    rowNum = random.randint(0,n-1)
    colNum = random.randint(0, n-1)

    while not board[rowNum][colNum] ==0:
        rowNum = random.randint(0,n-1)
        colNum = random.randint(0, n-1)

    board[rowNum][colNum]=newVal()

def won():
    for row in board:
        if 2048 in row:
            return True
    return False


def noMoves():
    b1=copy.deepcopy(board)
    b2=copy.deepcopy(board)
    
    b1=merge_left(b1)
    if b1 == b2:
        b1=merge_right(b1)
        if b1 == b2:
            b1=merge_up(b1)
            if b1==b2:
                b1=merge_down(b1)
                if b1 == b2:
                    return True
    return False
                
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
print(f"Score: {score}")
display()

    
gameOver = False
 
while not gameOver:
    move = input("Which you want to move? ")

    validMove =True
    #creating a copy to check if board didnt changed after the move
    tempBoard=copy.deepcopy(board)
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
        if board== tempBoard:
            print("Try a different direction!")
        else:
            if won():
                print(f"Score: {score}")

                display()
                print("You Won!!!")
                gameOver=True
            else:
                addVal()
                print(f"Score: {score}")

                display()

                if noMoves():
                    print("No moves possible. You loose!")
                    gameOver=True
