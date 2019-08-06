import random

def user_input(): #exitet ne felejtsd el
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
 tomb = [] #tömböt row-ra
 table = []
 while i < 9:
     j = 0
     tomb = []
     while j < 9:
         tomb.append(0)
         j+=1
     table.append(tomb)
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
  
def value_change(main_map, background_map, row,col):
   checkForHit = check_for_hit(background_map, row, col)
   if checkForHit == True:
       main_map[row-1][col-1]="x" #strig literal kimehet akár globális változóba
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
       j=0
       placable=True
       while j < shipParameter[1]:
           if shipParameter[2]==0:
               if backgroundList[shipParameter[3]+j][shipParameter[4]]!=0:
                   placable=False
           elif shipParameter[2]==1:
               if backgroundList[shipParameter[3]][shipParameter[4]+j]!=0:
                   placable=False
           j+=1
       if placable==True:
           k=0
           while k < shipParameter[1]:
               if shipParameter[2]==0:
                   backgroundList[shipParameter[3]+k][shipParameter[4]]=shipParameter[0]  # ez írja át a 0-t IDra
               elif shipParameter[2]==1:
                   backgroundList[shipParameter[3]][shipParameter[4]+k]=shipParameter[0]
               k+=1
       else:
           i-=1
       i+=1
   return backgroundList

  
def win_condition(hit_count):
   if hit_count==14:
       return True
   else:
       return False




def main():
    hit_count=0
    main_map = create_table()
    backgound_map= random_ship_position()
    print_table(main_map)
    while win_condition(hit_count) == False:
        row, col = user_input()
        print_table(backgound_map)
        print_table(value_change(main_map, backgound_map, row, col))
        if check_for_hit(backgound_map, row, col) == True:
            hit_count += 1

    print("Congratulations, You've won!")

main()
#test
