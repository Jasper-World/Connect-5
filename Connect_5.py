#connect 5 game
import sys

# functions 
grid = [["." for _ in range(10)] for _ in range(10)]
move =0

def Paint():
  #print out the map
  print("")
  for i in range(10):
    print(" ---------------------------------------")
    for j in range(10):
      print("|",grid[i][j],"", end="")
    print("|")
  print(" ---------------------------------------")
  print("")

def display():
  global move
#function for displaying & checking users input 
  while True:
    #stop you from typing gibberish
    try:
      x1 = int(input("First player's x coordinate"))
    except ValueError:
      print("Please pick a NUMBER from 1 to 10")
      continue
    
    try:
      y1 = int(input("First player's y coordinate"))
    except ValueError:
      print("Please pick a NUMBER from 1 to 10")
      continue

    if x1 < 1 or x1 > 10 or y1 < 1 or y1 > 10:
      print("Out of bounds, choose a number from 1 to 10")
      continue
    
    #test is player cheating 
    if grid[10-y1][x1-1] != ".":
      print("Why are you cheating!!!!!!!!!!!")
      sys.exit()
    
    grid[10-y1][x1-1] = "O"
    move +=1
    Paint()
    if check(10-y1, x1-1, "O"):
      print("player 1 won YAYAYAYAYAAAAY")
      countP(1)
      retry()
    elif move >= 100:
      print("It's a tie, the board is full")
      retry() 
    
    try:
      x2 = int(input("Second player's x coordinate"))
    except ValueError:
      print("Please pick a NUMBER from 1 to 10")
      continue

    #stop you from typing gibberish
    try:
      y2 = int(input("Second player's y coordinate"))
    except ValueError:
      print("Please pick a NUMBER from 1 to 10")
      continue

    if x2 < 1 or x2 > 10 or y2 < 1 or y2 > 10:
      print("Out of bounds, choose a number from 1 to 10")
      continue

    #test is player cheating 
    if grid[10-y2][x2-1] != ".":
      print("Why are you cheating!!!!!!!!!!!")
      sys.exit()
    
    grid[10-y2][x2-1] = "X"
    move +=1
    Paint()
    if check(10-y2, x2-1, "X"):
      print("player 2 won YAYAYAYAYAAAAY")
      countP(2)
      retry()
    elif move >= 310:
      print("It's a tie, the board is full")
      retry() 

def check(x,y,piece):
  #using the actual x and y + the directions to find pieces without using a lot of grid[][] 
  direction =[(0,1), (1,0), (1,1), (1,-1)]
  for dx, dy in direction:
    count = 1 
    nx = x + dx 
    ny=y + dy 
    #the while loop only start when the requirement is meet
    while 0<=nx<10 and 0<=ny<10 and grid[nx][ny] == piece:
      count +=1
      nx +=dx
      ny +=dy
    nx = x - dx 
    ny=y - dy 
    while 0<=nx<10 and 0<=ny<10 and grid[nx][ny] == piece:
      count +=1
      nx -=dx
      ny -=dy
    if count >=5:
      return True 
  return False
    

def countP(player):
  global counta 
  global countb 
  if player == 1:
    counta = counta + 1
  elif player == 2:
    countb = countb + 1

def retry():
  global grid
  global ans 
  global move
  while True:
    ans = str(input("Do you want to retry (y/n): "))
    if ans == "y" or ans == "n":
      break
    else:
      print("Please type y or n (Lowercase) ")

  if ans == "y":
    grid = [["." for _ in range(10)] for _ in range(10)]
    move =0
    display()
  if ans == "n":
    if counta > countb:
      print("Player 1 won with", counta, "points")
    elif counta < countb:
      print("player 2 won with", countb, "points")
    else:
      print("Thats a tie")
    sys.exit()

# actually code that start the game 
print("Welcome to Connect 5")
ans = 0
counta = 0
countb = 0 
display() 