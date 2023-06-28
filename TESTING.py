import numpy as np

class Piece:
    def __init__(self, color, piecename):
        self.piece = piecename
        if color == "White":
            self.color = 1
        else:
            self.color = 0
        self.values = {
        "Empty": 0,
        "King": 1,
        "Pawn": 2,
        "Knight": 3,
        "Bishop": 4,
        "Rook": 5,
        "Queen": 6,
        }
    
    def create(self):
        return int(f"{self.color}{self.values[self.piece]}")
class Board:
    def __init__(self) :
        oneDboard = np.array([0]*8,)
        self.board = np.tile(oneDboard, (8,1))
    
    def place(self, color, piece, coords):
        self.board[coords[0]][coords[1]] = Piece(color, piece).create()  
        return self.board
    
    def moveproto(self, move):
        pieceTypeFromSymbol = {
        "k": "King", "p": "Pawn", "n": "Knight", 
        "b": "Bishop", "r": "Rook", "q": "Queen"
        }
        
        if move[0].lower() in pieceTypeFromSymbol.keys():
            piece = pieceTypeFromSymbol[move[0].lower()]
        else:
            piece = "Pawn"  
        rank = int(ord(move[1])-97)
        file = int(move[2])-1 
    
    def move(self, where, location, piece="2"):
        vert_sliders = [5,6, 15, 16]
        pawn = [2, 12]
        location = [int(location[1])-1, ord(str(location[0]))-97]
        where = [int(where[1])-1, ord(str(where[0]))-97]
        if int(piece) in vert_sliders:
            if location[0] == where[0] or location[1] == where[1]:
                if location[1] == where[1]:
                    values = [where[0], location[0]]
                    values = sorted(values)
                    possibleMoves = np.arange(values[0], values[1], 1).tolist()
                    for move in possibleMoves:
                        if int(self.board[move][where[1]]) == int(piece):
                            continue
                        elif int(self.board[move][where[1]]) == 0:
                            continue
                        elif len(str(self.board[move][where[1]])) == len(str(piece)):
                            return "Not legal move."
                            break 
                if location[0] == where[0]:
                    values = [where[1], location[1]]
                    values = sorted(values)
                    possibleMoves = np.arange(values[0], values[1], 1).tolist() 
                    for move in possibleMoves:
                        if int(self.board[where[0]][move]) == int(piece):
                            continue
                        elif int(self.board[where[0]][move]) == 0:
                            continue
                        elif len(str(self.board[where[0]][move])) == len(str(piece)):
                            return "Not legal move."
                            break    
                if int(self.board[where[0]][where[1]]) == int(piece):
                    self.board[location[0]][location[1]] = int(piece)
                    self.board[where[0]][where[1]] = 0
                else:
                    return "Piece not found"
            else:
                return "Not a legal move."
        
        if int(piece) in pawn:
            legalMove = False
            if where[0] == 6 or where[0] == 1:
                if location[1] == where[1] and -3 < int(location[0])-int(where[0]) < 3:
                    legalMove = True
                else:
                    return "Not legal move."
            else:
                if location[1] == where[1] and -2 < int(location[0])-int(where[0]) < 2:
                    legalMove = True
                else:
                    return "Not legal move."
            if legalMove:
                values = [where[0], location[0]]
                values = sorted(values)
                possibleMoves = np.arange(values[0], values[1], 1).tolist()
                for move in possibleMoves:
                    if int(self.board[move][where[1]]) == int(piece):
                        continue
                    elif int(self.board[move][where[1]]) == 0:
                            continue
                    elif len(str(self.board[move][where[1]])) == len(str(piece)):
                        return "Not legal move."
                        break
                if int(self.board[where[0]][where[1]]) == int(piece):
                    self.board[location[0]][location[1]] = int(piece)
                    self.board[where[0]][where[1]] = 0
                else:
                    return "Piece not found"
                    


        return self.board

    def on_board(self, loc):
        loc1, loc2 = [int(loc[1])-1, ord(str(loc[0]))-97]
        return self.board[loc1][loc2]        

def loadposfromfen(boardCmds, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQ"):
    pieceTypeFromSymbol = {
        "k": "King", "p": "Pawn", "n": "Knight", 
        "b": "Bishop", "r": "Rook", "q": "Queen"
    }
    fenBoard = fen.split(" ")[0]
    file = 0
    rank = 7
    for char in fenBoard:
        if char == "/":
            file = 0
            rank -= 1
        else:
            if char.isdigit():
                file+=int(char)
            else:
                if char.islower():
                    color = "Black"
                elif char.isupper():
                    color = "White"
                pieceType=pieceTypeFromSymbol[char.lower()]
                board = boardCmds.place(color, pieceType, [rank, file])
                file +=1
    return board

boardCmds = Board()
board = loadposfromfen(boardCmds)
board = boardCmds.move("e7", "e6", "2")
board = boardCmds.move("a7", "a5", "2")
board = boardCmds.move("d2", "d4", "12")
board = boardCmds.move("a8", "a6", "5")
print(board)
