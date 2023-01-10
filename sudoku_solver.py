import numpy as np
board=[[0,0,8,0,0,0,1,0,0],
        [0,0,0,1,8,0,0,7,0],
        [0,6,9,0,5,0,0,0,0],
        [0,0,0,0,3,6,0,0,9],
        [0,2,0,0,7,0,0,0,0],
        [0,0,0,0,0,4,2,0,0],
        [7,0,0,0,0,0,0,6,0],
        [2,1,3,8,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,5]]


def chhapimaar(b):
    for i in range(len(b)):
        if i%3==0:
            print("---------------------------")
        for j in range(len(b[0])):
            if j%3==0 :
                print(" | ",end="")   
            print(str(b[i][j])+" ",end="")    
        print()

def sachu6e(b,val,ind):
    for i in range (len (b [0])) :
        if b [ind [0]] [i]== val and ind[1]!=i:
            return False
    
    for i in range (len (b)):
        if b[i] [ind [1]]==val and ind[0]!=i:
            return False

    x=3* (ind[0]//3)
    y=3* (ind[1]//3)

    for i in range (x,x+3):
        for j in range (y,y+3):
            if b[i][j]== val and (i,j)!=ind:
                return False
                

    return True

def khali_jagya_aap(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)
    return None        

def jawab_aap(b):
    khli=khali_jagya_aap(b)
    if not khli:
        return True
    
    r,c=khli
    for i in range(1,10):
        if sachu6e(board,i,(r,c)):
            b[r][c]=i

            if(jawab_aap(board)):
                return True
            board[r][c]=0
    return False        


jawab_aap(board)
chhapimaar(board)