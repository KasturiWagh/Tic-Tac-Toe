theBoard = { '1' : ' ' , '2' : ' ' , '3' : ' ',
             '4' : ' ' , '5' : ' ' , '6' : ' ',
             '7' : ' ' , '8' : ' ' , '9' : ' ' }

def printBoard(board):
    print(board['1'] + ' |' + board['2'] + '  |' + board['3'])
    print('- + - +-')
    print(board['4'] + ' |' + board['5'] + '  |' + board['6'])
    print('- + - + -')
    print(board['7'] + ' |' + board['8'] + '  |' + board['9'])

turn = 'x'

def o(board):
    won = False
    if(board['1'] == board['2'] == board['3'] and board['1'] != ' ' and board['2'] != ' ' and  board['3'] != ' '):
        won = True

    if(board['4'] == board['5'] == board['6'] and board['4'] != ' ' and board['5'] != ' ' and  board['6'] != ' '):
        won = True 

    if(board['7'] == board['8'] == board['9'] and board['7'] != ' ' and board['8'] != ' ' and  board['9'] != ' '):
        won = True

    if(board['1'] == board['5'] == board['9'] and board['1'] != ' ' and board['5'] != ' ' and  board['9'] != ' '):
        won = True

    if(board['3'] == board['5'] == board['7'] and board['3'] != ' ' and board['5'] != ' ' and  board['7'] != ' '):
        won = True

    if(board['1'] == board['4'] == board['7'] and board['1'] != ' ' and board['4'] != ' ' and  board['7'] != ' '):
        won = True
    
    if(board['2'] == board['5'] == board['8'] and board['2'] != ' ' and board['5'] != ' ' and  board['8'] != ' '):
        won = True

    if(board['3'] == board['6'] == board['9'] and board['3'] != ' ' and board['6'] != ' ' and  board['9'] != ' '):
        won = True

    return won

def game():
    turn = 'x'
    for i in range(9): 
        printBoard(theBoard)
        print("its turn of " + turn )
        place = input("You want which place :: ")

        while not theBoard[place] == ' ':
            print("enter properly ")
            place = input()

        theBoard[place] = turn

        won = o(theBoard)
        if won :
            print('\n***********' + turn + ' won **********\n')
            break
        elif turn == 'x' :
            turn = 'o'
        elif turn == 'o':
            turn = 'x'
    if not won :
        print("*******no one wins********")

    printBoard(theBoard)
    print("********************************")

def restart():
    for i in theBoard.keys():
        theBoard[i] = ' '
    game()
        
def menu():
    print("play tic tac toe")
    game()
    flag = False

    while not flag:
        print("do you want to play again :: ")
        ans = input()
        if(ans == 'y'):
            restart()
            continue
        else:
            break

menu()
