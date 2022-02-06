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
