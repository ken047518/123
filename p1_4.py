# -*- coding: utf-8 -*-
"""P1_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1awDCqs3Q1JccJ2LF-2D8GRFdrq0fhK4u
"""



now=input().split(" ")
now_x=int(now[0])
now_y=int(now[1])
nextp=input().split(" ")
next_x=int(nextp[0])
next_y=int(nextp[1])

# checkerboard=[[0]*8 for i in range(8)]
# checkerboard=[ [1, 0, 0, 0, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0] ]
checkerboard[now_x][now_y]=1

temp_x=abs(next_x-now_x)
temp_y=abs(next_y-now_y)



if temp_x==2 and temp_y==1:
    if next_x>now_x and next_y>now_y:
        if checkerboard[now_x+2][now_y+1]==1:
            print("No")
        else:
            print("Yes")
    elif next_x<now_x and next_y>now_y:
        if checkerboard[now_x-2][now_y+1]==1:
            print("No")
        else:
            print("Yes")
    elif next_x<now_x and next_y<now_y:
        if checkerboard[now_x-2][now_y-1]==1:
            print("No")
        else:
            print("Yes")
    elif next_x>now_x and next_y<now_y:
        if checkerboard[now_x+2][now_y-1]==1:
            print("No")
        else:
            print("Yes")
elif temp_x==1 and temp_y==2:
    if next_x>now_x and next_y>now_y:
            if checkerboard[now_x+1][now_y+2]==1:
                print("No")
            else:
                print("Yes")
    elif next_x<now_x and next_y>now_y:
        if checkerboard[now_x-1][now_y+2]==1:
            print("No")
        else:
            print("Yes")
    elif next_x<now_x and next_y<now_y:
        if checkerboard[now_x-1][now_y-2]==1:
            print("No")
        else:
            print("Yes")
    elif next_x>now_x and next_y<now_y:
        if checkerboard[now_x+1][now_y-2]==1:
            print("No")
        else:
            print("Yes")
else:
    print("No")