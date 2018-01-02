import random
import time

def game():
    
    print('WELCOME to [The Coins] ')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    
    level = ''
    while level not in ['b', 'p']:
        level = input('b for beginner, p for professional: ')
    seq = input( 'Type c if you wish the computer to play first: ')
    
    if seq =='c':
        turnMarker = False
    
    else:
        turnMarker = True
    
    start = int(input("how many coins do you wish to start: "))
    
    while start < 10:
        start = int(input("try again, the start value must be greater than 10："))

    cur_value = start
    
    time.sleep(1)
    
    print('On your turn, you may remove 1 to 3 coins until there are no coins left')
    
    if turnMarker == True:
        
        print('Current total: %d; next player: p1\n'%cur_value) 
    
    else:
        
        print('Current total: %d; next player: p2\n'%cur_value) 
    
    while True:
        if turnMarker:
            while True:
                time.sleep(2)
                remove_value = int(input('Remove how many? '))
                if is_legal(remove_value) and remove_value <= cur_value:
                    cur_value = cur_value - remove_value
                    turnMarker = False
                    time.sleep(1)
                    print('You choose: Remove %d'%remove_value)
                    time.sleep(2)
                    print('New game state: Current total: %d; next player: p2\n'%(cur_value))
                    break
                else:
                    
                    print('Illegal move: Remove %d'%remove_value)   
                    print('Please try again.\n')  
                    print('On your turn, you may remove 1 to 3 coins until there are no coins left')
                    print('Current total: %d; next player: p1'%cur_value) 
                    
        else:
            strategy = {'b':random_move(cur_value) ,'p':optimal_move(cur_value)}
            remove_value = strategy[level]
            cur_value = cur_value - remove_value;
            time.sleep(2)
            print('The computer chooses: Remove %d'%remove_value)
            time.sleep(2)
            print('New game state: Current total: %d; next player: p1\n'%cur_value)
            turnMarker=True
        if cur_value==0:
            if turnMarker==False:
                print('Beat ya!')
            else:
                print('Congrats -- you won!!')
            break
        
        
def is_legal(value):
    if value in [1,2,3]:
        return True
    else:
        return False
    
def random_move(cur_value):
    if cur_value >= 3:
        return random.randint(1,3)
    else:
        return random.randint(1,cur_value)
    
def optimal_move(cur_value):
    if  (cur_value % 4) != 1 and (cur_value -1) % 4 != 0:
        return (cur_value -1) %4 
    else:
        return 1
       
if __name__ == '__main__':
    game()