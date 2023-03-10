from main import HumanPlayer,RandomComputerPlayer
class TicTac:

    def __init__(self):
        self.board = [' 'for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3:(1+i)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + '|')


    @staticmethod
    def print_board_numbers():
       #0 1 2 etc (tell us what correspond to what board)
       number_board=[[str(i) for i  in range(j*3, (j+1)*3)] for j in range(3)]
       for row in number_board:
           print('| ' + ' | '.join(row) + '|')

    def availabeMove(self):
        return[i for i,spot in enumerate(self.board) if spot == ' ']
       # move=[]
       # for (i,spot) in enumerate(self.board):
       #     if spot== ' ':
       #         move.append(i)
       # return move
         ####['x','x',0,0]->[(0,'x'),(1,'x'),(2,'o')] etc
    def empty_square(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')
# return len(self.availabeMove())
    def makeMove(self,square,letter):
        if self.board[square]== ' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    def winner(self,square,letter):
        row_index=square//3
        row=self.board[row_index*3:(row_index+1)*3]
        if all([spot ==letter for spot in row]):
            return True
        col_index = square % 3
        column = [self.board[col_index +i* 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square %2 ==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player,o_player, print_game=True):
    if print_game:
        game.print_board_numbers()

    letter = 'X'
    while game.empty_square():
        if letter == 'o':
            square=o_player.getMove(game)
        else:
            square=x_player.getMove(game)
        #get thr move from the approptriate player

        if game.makeMove(square,letter):
            if print_game:
                print(letter+f'Make a move to {square}')
                game.print_board()
                print(' ')
                letter = 'o' if letter == 'x' else 'x'
              #  if letter == 'x':
               #     letter='o'
                #else:
                    #letter = 'x'
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                    return letter

        if print_game:
            print('It is a tie')

    if __name__ == '__main__':
        x_player=HumanPlayer('X')
        o_player=RandomComputerPlayer('o')
        t=TicTac()
        play(t,x_player,o_player,print_game=True)

