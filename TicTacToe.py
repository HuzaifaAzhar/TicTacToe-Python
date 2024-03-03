import random
board=[['1','2','3'],['4','5','6'],['7','8','9']]

def display_board():
        print("",board[0][0],'|',board[0][1],'|',board[0][2])
        print("",board[1][0],'|',board[1][1],'|',board[1][2])
        print("",board[2][0],'|',board[2][1],'|',board[2][2])

def check_position(pos):
      if(pos=='1'):
            if(board[0][0]=='1'):
                  return True
            else:
                  return False
      if(pos=="2"):
            if(board[0][1]=='2'):
                  return True
            else:
                  return False
      if(pos=="3"):
            if(board[0][2]=='3'):
                  return True
            else:
                  return False
      if(pos=="4"):
            if(board[1][0]=='4'):
                  return True
            else:
                  return False
      if(pos=="5"):
            if(board[1][1]=='5'):
                  return True
            else:
                  return False
      if(pos=="6"):
            if(board[1][2]=='6'):
                  return True
            else:
                  return False
      if(pos=="7"):
            if(board[2][0]=='7'):
                  return True
            else:
                  return False
      if(pos=="8"):
            if(board[2][1]=='8'):
                  return True
            else:
                  return False
      if(pos=="9"):
            if(board[2][2]=='9'):
                  return True
            else:
                  return False
      return False

def place_position(pos,choice):
      if(pos=='1'):
            board[0][0]=choice
      if(pos=="2"):
            board[0][1]=choice
      if(pos=='3'):
            board[0][2]=choice
      if(pos=="4"):
            board[1][0]=choice
      if(pos=='5'):
            board[1][1]=choice
      if(pos=="6"):
            board[1][2]=choice
      if(pos=='7'):
            board[2][0]=choice
      if(pos=="8"):
            board[2][1]=choice
      if(pos=='9'):
            board[2][2]=choice
            
def get_choice():
      global user_choice
      user_choice=""
      global ai_choice
      ai_choice=""
      while(user_choice.lower()!='x' and user_choice.lower()!='o'):
            print("Choose 'x' or 'o': ",end="")
            user_choice=input()
      user_choice = user_choice.lower()
      if(user_choice=='x'):
        ai_choice='o'
      else:
        ai_choice='x'

def user_input():
      #display_board()
      print("Enter where to place your position: ",end="")
      check = False
      while(check == False):
            input_choice=input()
            check = check_position(input_choice)
            if(check==True):
                  place_position(input_choice,user_choice)
            else:
                  print("Invalid Move! Try Again:",end='')
      #display_board()

def ai_input():
    #print(user_choice)
    available_positions = [str(i) for i in range(1, 10) if check_position(str(i))]
    if(available_positions==[]):
        print("No Moves Left. It's a draw!")
        return False
    
    print("AI's turn:")
    ai_move = random.choice(available_positions)
    place_position(ai_move, ai_choice)
    #display_board()
    return True

def check_won():
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    return False

get_choice()
while (check_won()==False):
      display_board()
      user_input()
      if(check_won()!=False):
            display_board()
            print(check_won(),' Won')
            break
      display_board()
      if(ai_input()==False):
            break
      if(check_won()!=False):
            display_board()
            print(check_won(),' Won')
            break
