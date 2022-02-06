# Creating temporary filled board
board=[[0,0,2,2],[2,2,2,0],[4,0,0,4],[0,2,0,0]]
#display the board
def display():
    for row in board:
        currentRow="|"
        for elem in row:
            if not elem:
                currentRow+=" |"

            else:
                currentRow+=str(elem)+"|"
        print(currentRow)
    print()
display()
