# Creating temporary filled board
board=[[0,0,2,2],[2,2,2,0],[4,0,0,4],[0,2,0,0]]
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

display()
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



merge_left(board)
display()