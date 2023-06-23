import random
l=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
def Rcheck(a):
    for x in range(0,len(mat)):
        u=0
        c=0
        mt=0
        for y in range(0,len(mat[x])):
            if(mat[x][y]==xo):
                u+=1
            elif(mat[x][y]==com):
                c+=1
            else:
                mt+=1
                xi=x
                yi=y
        if(c==3 and a==3):
            return "c"
        elif(u==3 and a==3):
            return "u"
        elif(c==2 and mt==1 and u!=1 and a==0):
            return [xi,yi]
        elif(u==2 and mt==1 and a==1):
            return [xi,yi]
    else:
        return "none"
def Ccheck(a):
    for x in range(0,len(mat)):
        u=0
        c=0
        mt=0
        for y in range(0,len(mat[x])):
            if(mat[y][x]==xo):
                u+=1
            elif(mat[y][x]==com):
                c+=1
            else:
                mt+=1
                xi=y
                yi=x
        if(c==3 and a==3):
            return "c"
        elif(u==3 and a==3):
            return "u"
        elif(c==2 and mt==1 and u!=1 and a==0):
            return [xi,yi]
        elif(u==2 and mt==1 and a==1):
            return [xi,yi]
    else:
        return "none"
def dia1(a):
    u=0
    mt=0
    c=0
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            if(x==y):
                if(mat[x][y]==xo):
                    u+=1
                elif(mat[x][y]==com):
                    c+=1
                else:
                    mt+=1
                    xi=x
                    yi=y
    if(c==3 and a==3):
            return "c"
    elif(u==3 and a==3):
            return "u"
    elif(c==2 and mt==1 and u!=1 and a==0):
        return [xi,yi]
    elif(u==2 and c!=1 and mt==1 and a==1):
        return [xi,yi]
    else:
        return "none"
def dia2(a):
    u=0
    mt=0
    c=0
    m=len(mat)
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            if(y==m-1):
                m-=1
                if(mat[x][y]==xo):
                    u+=1
                elif(mat[x][y]==com):
                    c+=1
                else:
                    mt=mt+1
                    xi=x
                    yi=y
    if(c==3 and a==3):
            return "c"
    elif(u==3 and a==3):
            return "u"
    elif(c==2 and mt==1 and u!=1 and a==0):
        return [xi,yi]
    elif(u==2 and c!=1 and mt==1 and a==1):
        return [xi,yi]
    else:
        return "none"
mat=[['-','-','-'],['-','-','-'],['-','-','-']]
cho=int(input("enter 1 for user vs user \nenter 2 for user vs computer"))
if(cho==2):
    first="u1"
    for i in range(0,len(mat)):
        for j in range(0,len(mat[i])):
            print(mat[i][j],end=" ")
        print("\n")
    if(first=="u1"):
        print("user choice")
        xo=input("enter X or O")
        if(xo=='X'):
            com='O'
        else:
            com='X'
        print("user :",xo,"\ncomputer :",com)
        while(True):
            print("user turn")
            row=int(input("enter the row number:"))
            col=int(input("enter the column number:"))
            if(mat[row][col]=='-'):
                mat[row][col]=xo
            else:
                while(True):
                    row=int(input("enter the row number:"))
                    col=int(input("enter the column number:"))
                    if(mat[row][col]=='-'):
                        mat[row][col]=xo
                        break
                    else:
                        continue
            for i in range(0,len(mat)):
                for j in range(0,len(mat[i])):
                    print(mat[i][j],end=" ")
                print("\n")
            ul=[row,col]
            l.remove(ul)
            if(len(l)>=1):
                
                c5=dia1(1)
                c6=dia2(1)
                c7=Rcheck(1)
                c8=Ccheck(1)
                c1=dia1(0)
                c2=dia2(0)
                c3=Rcheck(0)
                c4=Ccheck(0)
                if(c1!="none" and c1!="c" and c1!="u" ):
                    comch=c1
                    crow=comch[0]
                    ccol=comch[1]
                elif(c2!="none" and c2!="c" and c2!="u" ):
                    comch=c2
                    crow=comch[0]
                    ccol=comch[1]
                elif(c3!="none" and c3!="c" and c3!="u"):
                    comch=c3
                    crow=comch[0]
                    ccol=comch[1]
                elif(c4!="none" and c4!="c" and c4!="u" ):
                    comch=c4
                    crow=comch[0]
                    ccol=comch[1]
                elif(c5!="none" and c5!="c" and c5!="u" ):
                    comch=c5
                    crow=comch[0]
                    ccol=comch[1]
                elif(c6!="none" and c6!="c" and c6!="u" ):
                    comch=c6
                    crow=comch[0]
                    ccol=comch[1]
                elif(c7!="none" and c7!="c" and c7!="u"):
                    comch=c7
                    crow=comch[0]
                    ccol=comch[1]
                elif(c8!="none" and c8!="c" and c8!="u"):
                    comch=c8
                    crow=comch[0]
                    ccol=comch[1]           
                else:
                    comch=random.choice(l)
                    crow=comch[0]
                    ccol=comch[1]
                if(Rcheck(3)=="c" or Ccheck(3)=="c" or dia1(3)=="c" or dia2(3)=="c"):
                    print("computer wins")
                    break
                elif(Rcheck(3)=="u" or Ccheck(3)=="u" or dia1(3)=="u" or dia2(3)=="u"):
                    print("user wins")
                    break
                if(mat[crow][ccol]=='-'):
                    mat[crow][ccol]=com
                ul=[crow,ccol]
                l.remove(ul)
            if(len(l)==0):
                print("tie")
                break
            for i in range(0,len(mat)):
                for j in range(0,len(mat[i])):
                    print(mat[i][j],end=" ")
                print("\n")
            if(Rcheck(3)=="c" or Ccheck(3)=="c" or dia1(3)=="c" or dia2(3)=="c"):
                    print("computer wins")
                    break
            elif(Rcheck(3)=="u" or Ccheck(3)=="u" or dia1(3)=="u" or dia2(3)=="u"):
                    print("user wins")
                    break
else:
    import random

    def check(a):
        u1=0
        u2=0
        for x in range(0,len(mat)):
            for y in range(0,len(mat[x])):
                colc=x
                cold=y
                if(a!=0):
                    colc=y
                    cold=x
                if(mat[colc][cold]==xo1):
                    u1+=1
                elif(mat[colc][cold]==xo2):
                    u2+=1
            if(u2==3):
                return "u2"
            elif(u1==3):
                return "u1"
        return "none"
    def dia1():
        u1=0
        u2=0
        for x in range(0,len(mat)):
            for y in range(0,len(mat[x])):
                if(x==y):
                    if(mat[x][y]==xo1):
                        u1+=1
                    elif(mat[x][y]==xo2):
                        u2+=1
        if(u2==3):
            return "u2"
        elif(u1==3):
            return "u1"
        else:
            return "none"
    def dia2():
        u1=0
        u2=0
        m=len(mat)
        for x in range(0,len(mat)):
            for y in range(0,len(mat[x])):
                if(y==m-1):
                    m-=1
                    if(mat[x][y]==xo1):
                        u1+=1
                    elif(mat[x][y]==xo2):
                        u2+=1
        if(u2==3):
            return "u2"
        elif(u1==3):
            return "u1"
        else:
            return "none"
    mat=[['-','-','-'],['-','-','-'],['-','-','-']]
    for i in range(0,len(mat)):
        for j in range(0,len(mat[i])):
            print(mat[i][j],end=" ")
        print("\n")
    xo1=input("user 1 \nenter X or O")
    print("user 1:",xo1)
    if(xo1=='X'):
        xo2='O'
    else:
        xo2='X'
    print("user 2:",xo2)
    tie=0
    while(True):
        print("user 1 turn")
        row=int(input("enter the row number:"))
        col=int(input("enter the column number:"))
        if(mat[row][col]=='-'):
            mat[row][col]=xo1
            tie+=1
        else:
            while(True):
                row=int(input("enter the row number:"))
                col=int(input("enter the column number:"))
                
                if(mat[row][col]=='-'):
                    mat[row][col]=xo1
                    tie+=1
                    break
                else:
                    continue
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                print(mat[i][j],end=" ")
            print("\n")
        if(check(0)=="u2" or check(1)=="u2" or dia1()=="u2" or dia2()=="u2"):
            print("user 2 wins")
            break
        elif(check(0)=="u1" or check(1)=="u1" or dia1()=="u1" or dia2()=="u1"):
            print("user 1 wins")
            break
        if(tie==9):
            print("tie")
            break
        print("user 2 turn")
        row=int(input("enter the row number:"))
        col=int(input("enter the column number:"))
        if(mat[row][col]=='-'):
            mat[row][col]=xo2
            tie+=1
        else:
            while(True):
                row=int(input("enter the row number:"))
                col=int(input("enter the column number:"))
                if(mat[row][col]=='-'):
                    mat[row][col]=xo2
                    tie+=1
                    break
                else:
                    continue
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                print(mat[i][j],end=" ")
            print("\n")
        if(check(0)=="u2" or check(1)=="u2" or dia1()=="u2" or dia2()=="u2"):
            print("user 2 wins")
            break
        elif(check(0)=="u1" or check(1)=="u1" or dia1()=="u1" or dia2()=="u1"):
            print("user 1 wins")
            break