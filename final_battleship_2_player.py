import random

def ai_user_input(player_tips=None): #need of checking the already guessed values
  
    isItGuessed=True# init
    while isItGuessed==True:

        row_input = True
        col_input = True
        while col_input:
            try:
                col = int(input("Column: "))
                if col >= 10 or col < 1:
                    raise Exception
                col_input = False
            except:
                print("Input numbers between 1 and 9")
                continue
        while row_input:
            try:
                row = int(input("Row: "))
                if row >= 10 or row < 1:
                    raise Exception
                row_input = False
            except:
                print("Input numbers between 1 and 9")
                continue
        
        isItGuessed=is_it_guessed(player_tips,row,col)

        if isItGuessed==True:
            print("You already guessed the filed",col,row,)
    store_tips(player_tips,row,col) #store the guessed numbers in pairs
    
    return row, col

def user_input(): #need of checking the already guessed values
 
    row_input = True
    col_input = True
    while col_input:
        try:
            col = int(input("Column: "))
            if col >= 10 or col < 1:
                raise Exception
            col_input = False
        except:
            print("Input numbers between 1 and 9")
            continue
    while row_input:
        try:
            row = int(input("Row: "))
            if row >= 10 or row < 1:
                raise Exception
            row_input = False
        except:
            print("Input numbers between 1 and 9")
            continue
    
    return row, col

def create_table():
 i=0
 my_array = [] #tömböt row-ra
 table = []
 while i < 9:
     j = 0
     my_array = []
     while j < 9:
         my_array.append(0)
         j+=1
     table.append(my_array)
     i += 1
 return table

def print_table(table):
 mytable=table
 i = 0
 print("  1 2 3 4 5 6 7 8 9")
 while i < 9:
     print(i+1, *mytable[i])
     i+=1

def check_for_hit(background_map,row,col):
   if background_map[row-1][col-1] != 0: 
       return True
       print("its a hit")
   else:
       return False
  
def ai_value_change(main_map, background_map, row,col,list_hits):
   checkForHit = check_for_hit(background_map, row, col)
   if checkForHit == True:
       main_map[row-1][col-1]="x" #strig literal kimehet akár globális változóba
       win_condition_change(list_hits,background_map[row-1][col-1])
       print("Hit")
   elif checkForHit == False:
       main_map[row-1][col-1]="M"
       print("Miss")
   return main_map #nem feltétlenül kell

def value_change(main_map, background_map, row,col,player_hits):
    checkForHit = check_for_hit(background_map, row, col)
    if checkForHit == True:
        main_map[row-1][col-1]="x" #strig literal kimehet akár globális változóba
        player_hits += 1
        print("You've hit the ship")
    elif checkForHit == False:
        main_map[row-1][col-1]="M"
        print("You missed")
    return main_map #nem feltétlenül kell

def random_generator(size):
   rotation = random.randint(0, 1)
   if rotation == 0 and size == 3:
       positionH = random.randint(0, 6)
       positionV = random.randint(0, 8)
   elif rotation == 0 and size == 4:
       positionH = random.randint(0, 5)
       positionV = random.randint(0, 8)
   elif rotation == 1 and size == 3:
       positionH = random.randint(0, 8)
       positionV = random.randint(0, 6)
   elif rotation == 1 and size == 4:
       positionH = random.randint(0, 8)
       positionV = random.randint(0, 5) #sizeot fel lehet használni a tiltáshoz
   
   return rotation,positionH,positionV

def check_for_ships(shipParameter,backgroundList): #randomshipposition
    placable = True
    j=0
    while j < shipParameter[1]:
        if shipParameter[2]==0:
            if backgroundList[shipParameter[3]+j][shipParameter[4]]!=0:
                placable=False
        elif shipParameter[2]==1:
            if backgroundList[shipParameter[3]][shipParameter[4]+j]!=0:
                placable=False
        j+=1
    return placable

def place_ships(shipParameter,backgroundList): #randomshipposition
    k=0
    while k < shipParameter[1]:
        if shipParameter[2]==0:
            backgroundList[shipParameter[3]+k][shipParameter[4]]=shipParameter[0]  # ez írja át a 0-t IDra
        elif shipParameter[2]==1:
            backgroundList[shipParameter[3]][shipParameter[4]+k]=shipParameter[0]
        k+=1
                
def ship_parameter(id, size):
   rotation,positionH,positionV=random_generator(size)
   shipList = [id, size, rotation, positionH, positionV]
   return shipList

def random_ship_position():
    backgroundList = create_table()
    i=0
    while i < 4:
        shipParameter=[]
        if i < 2:
            size=3
            shipParameter = ship_parameter(i+1,size)
        else:
            size=4
            shipParameter = ship_parameter(i+1,size)
        
        if check_for_ships(shipParameter,backgroundList)==True:
            place_ships(shipParameter,backgroundList)
        else:
            i-=1
        i+=1
    return backgroundList

def win_condition(hits_list,win_condition_numbers,winner):
    sorted_list = sorted(hits_list)
    if sorted_list==win_condition_numbers:
        print(winner," won the game")
        return True
    else:
        return False

def whose_turn_is_it(current_turn):
    if current_turn%2==0:
        return "Player"
    else:
        return "AI"
  
def turns(whose_turn_is_it, player_tips, main_map, background_map, player_hits):#PhaseTwo(The player or the AI guess a coordinate based on whose turn is it)
    if whose_turn_is_it == "Player":
        print("Players Turn")
        row, col = ai_user_input(player_tips)
        print_table(ai_value_change(main_map, background_map, row, col, player_hits))
    elif whose_turn_is_it == "AI":
        print("AI-s turn")
        row=random.randint(1,9)
        col=random.randint(1,9)
        print_table(ai_value_change(main_map, background_map, row, col, player_hits))
                
def player_placement_input(id, size): # return shiplist with 5 items
    row_input = True
    col_input = True
    pos_input = True
    ship_list = [id, size, 0, 0, 0,]
    print("Insert your ship coordinates!")
    while pos_input:
        try:
            ship_list[2] = int(input("H = 1, V = 0: "))
            if ship_list[2] == 0 or ship_list[2] == 1:
                pos_input = False
            else:
                raise Exception
        except:
            print("Type 0 or 1")
    while col_input:
        try:
            ship_list[4] = int(input("Column: "))
            if ship_list[2]==0:#
                if ship_list[4] >= 10 or ship_list[4] < 1:
                    raise Exception
                ship_list[4] = ship_list[4] -1
                col_input = False
            elif ship_list[2]==1:#
                if ship_list[4] >= 10-ship_list[1]+1 or ship_list[4] < 1:
                    raise Exception
                ship_list[4] = ship_list[4] -1
                col_input = False
        except:
            if ship_list[2]==0:
                print("Input numbers between 1 and 9")
                continue
            elif ship_list[2]==1:
                print("Input numbers between 1 and ",10-ship_list[1])
    while row_input:
        try:
            if ship_list[2]==0:#
                ship_list[3] = int(input("Row: "))
                if ship_list[3] >= 10-ship_list[1]+1 or ship_list[3] < 1:
                    raise Exception
                ship_list[3] = ship_list[3] -1
                row_input = False
            elif ship_list[2]==1:#
                ship_list[3] = int(input("Row: "))
                if ship_list[3] >= 10 or ship_list[3] < 1:
                    raise Exception
                ship_list[3] = ship_list[3] -1
                row_input = False    
        except:
            if ship_list[2]==0:
                print("Input numbers between 1 and ",10-ship_list[1])
                continue
            if ship_list[2]==1:
                print("Input numbers between 1 and 9" )
                continue

            
    return ship_list

def player_ship_placement(): # Bug = merge

    backgroundList = create_table()

    i=0
    while i < 4:
        shipParameter=[]
        if i < 2:
            size=3
            shipParameter = player_placement_input(i+1, size)
            place_ships(shipParameter,backgroundList)
        else:
            size=4
            shipParameter = player_placement_input(i+1, size)
            place_ships(shipParameter,backgroundList)
        i += 1
        print_table(backgroundList) 
    return backgroundList       

def is_it_guessed(list_tips,col,row):#Check if the coordinates are guessed already
    guessed_pair=(col,row)
    isItGuessed=False
    i=0
    while i < len(list_tips):
        if guessed_pair==list_tips[i]:
            isItGuessed=True           
        i+=1
    return isItGuessed
        
def store_tips(list_tips,col,row):#Store the guessed values in pairs
    tmp_pair=(col,row)
    if tmp_pair not in list_tips:
        list_tips.append(tmp_pair)
    
def win_condition_change(list_hits,id_of_ship):
    list_hits.append(id_of_ship)
    print(list_hits)

def player_vs_ai():
    current_turn = 0
    win_condition_numbers = [1,1,1,2,2,2,3,3,3,3,4,4,4,4]
    player_tips = []
    player_hits = [1,1,1,2,2,2,3,3,3,3,4,4,4]
    ai_tips = []
    ai_hits = []
   
    main_map = create_table()
    background_map = random_ship_position()
    ai_map = create_table()
    ai_background = player_ship_placement()

    print("Background table test")
    print("AI's table")

    print_table(background_map)
    print("Player's table")
    print_table(ai_background)
    print("\n")
    someone_win=False
    while someone_win== False:
        turns(whose_turn_is_it(current_turn), player_tips, main_map, background_map, player_hits)
        someone_win=win_condition(player_hits,win_condition_numbers,"Player")
        if someone_win==True:
            break
        current_turn += 1
        turns(whose_turn_is_it(current_turn),ai_tips,ai_map,ai_background,ai_hits)
        someone_win=win_condition(ai_hits,win_condition_numbers,"Enemy")
        if someone_win==True:
            break
        current_turn += 1

        print("")
     
def player_vs_player():
        player_n_hits = 0
        player2_n_hits = 0
        main_map = create_table()
        player2_main_map = create_table()
        print("Player 1! Place your ships")
        player2_background_map = player_ship_placement()
        print("Player 2! Place your ships")
        background_map = player_ship_placement()
        print_table(main_map)
        while True:
            print("Player 1's turn")
            row, col = user_input()
            print_table(value_change(main_map, player2_background_map, row, col, player_n_hits))
            if check_for_hit(player2_background_map, row, col) == True:
                player_n_hits += 1
            if player_n_hits == 14:
                print("Player1 won the game!")
                break
            print("Player 2's turn")
            row2, col2 = user_input()
            print_table(value_change(player2_main_map, player2_background_map, row2, col2, player2_n_hits))
            if check_for_hit(background_map, row2, col2) == True:
                player2_n_hits += 1
            if player2_n_hits == 14:
                print("Player 2 won the game!")
                break
                  
def menu():
    choose = True
    answer=""
    while choose:
        print("1. PvP mode\n2. PvE mode\n3. Exit") 
        press = int(input())
        if press == 1:
            player_vs_player()
        elif press == 2:
            player_vs_ai()
        elif press == 3:   
            while answer!= "yes" or answer!="no":
                answer = input("Are you sure you quit? yes/no \n")
                if answer == "yes":
                    print("Good Bye!")
                    exit()   
                elif answer == "no":
                    break
        else:
            print("Please enter a number between 1 and 3")

def main():
    while True:
        menu()
        
main()