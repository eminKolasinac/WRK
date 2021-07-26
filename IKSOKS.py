
# pravimo tablu pomocu dictonary

theBoard = {'7': ' ','8':' ','9': ' ',
           '4': ' ','5': ' ','6': ' ',
            '1': ' ','2': ' ','3': ' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)

# printanje table

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Glavna funkcija igrice

def igrica():

    turn = 'X'
    count = 0
    
# mesto je input korisnika koji bira poziciju 
  
    for i in range(10):
        printBoard(theBoard)
        print("na tebe je red" + turn + ".Izaberi mesto?")
        move = input()
        
        if move.isdigit() == False:
            print('broj aloooo')
            continue
        else:
            if int(move) not in range(10):
                print('broj izmedju 1 i 9')
                continue
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('Izaberi drugo mesto')
            continue
            
        # funkcija ispod cisti output i printa samo jednu tablu za igru

        from IPython.display import clear_output
        clear_output(wait=True)

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] !=' ':
                printBoard(theBoard)
                print("kraj!"+ turn + " je pobedio")
                break
            
        if count == 9:
            print("Nereseno!")
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        
        
    restart = input('igrate li opet(y\n)')
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
            
        igrica()
if __name__ == "__main__":
    igrica() 