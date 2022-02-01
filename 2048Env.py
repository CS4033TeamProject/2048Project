import random

class TwentyFourtyEight:
    def __init__(self, length = 4):
        self.length = length
        self.board = []

        for r in range(0, self.length):
            temp = []
            for c in range(0, self.length):
                temp.append(0)
            self.board.append(temp)
        
        self.insertTile()
        
    def printBoard(self):
        for r in range(0, self.length):
            for c in range(0, self.length):
                print(str(self.board[r][c]) + " ", end = '')
            
            print()
    
    def insertTile(self):
        noSpaceFound = True

        while noSpaceFound:
            r = random.randint(0, self.length-1)
            c = random.randint(0, self.length-1)

            if self.board[r][c] == 0:
                self.board[r][c] = 2
                noSpaceFound = False

    def step(self, action):
        if action == "u":
            return self.stepUp()
        elif action == "d":
            return self.stepDown()
        elif action == "l":
            return self.stepLeft()
        elif action == "r":
            return self.stepRight()
        else:
            return None

    def stepLeft(self) -> list:
        insert = False

        for r in range(0, self.length):
            newRow = self.moveRow(self.combineRow(self.board[r]))
            
            if self.board[r] != newRow:
                self.board[r] = newRow
                insert = True
        
        if insert:
            self.insertTile()

        return self.board
    
    # Spawning tiles when it shouldnt fix later
    def stepRight(self) -> list:
        insert = False

        for r in range(0, self.length):
            self.board[r].reverse()
            combined = self.combineRow(self.board[r])
            combined.reverse()
            combined.reverse()
            newRow = self.moveRow(combined)
            newRow.reverse()
            
            if self.board[r] != newRow:
                self.board[r] = newRow
                insert = True
        
        if insert:
            self.insertTile()

        return self.board
    
    def stepUp(self) -> list:
        # RowColumn
        # Row traversal: 00 01 02 03 10 11
        # Column traversal: 00 10 20 30 10
        insert = False

        for c in range(0, self.length):
            tempRow = []

            for r in range(0, self.length):
                tempRow.append(self.board[r][c])
            
            print("Temp row: ", end = '')
            print(tempRow)
            
            newRow = self.moveRow(self.combineRow(tempRow))

            print("New row: ", end = '')
            print(newRow)

            for rr in range(0, self.length):
                self.board[rr][c] = newRow[rr]
            
            if self.board[r] != newRow:
                self.board[r] = newRow
                insert = True
        
        if insert:
            self.insertTile()

        return self.board

    def combineRow(self, origionalRow: list) -> list:
        # Create copy of origionalRow
        row = []
        for i in range(0, self.length):
            row.append(origionalRow[i])

        # Loop thru the columns in row
        for c in range(0, self.length-1):
            if row[c] != 0 and row[c] == row[c+1]:
                row[c] = row[c] * 2
                row[c+1] = 0
            if row[c] != 0 and row[c+1] == 0:
                d = c + 1
                while d < self.length:
                    if row[d] == 0:
                        d += 1
                    elif row[d] == row[c]:
                        row[c] = row[c] * 2
                        row[d] = 0
                        d = self.length + 1
                    else:
                        d = self.length + 1
        
        return row
    
    def moveRow(self, origionalRow: list) -> list:
        row = []
        for i in range(0, self.length):
            row.append(origionalRow[i])

        for c in range(1, self.length):
            if row[c] != 0:
                d = c
                while d > 0:
                    if row[d-1] == 0:
                        row[d-1] = row[d]
                        row[d] = 0
                    d += -1

        return row

if __name__ == "__main__":
    test = TwentyFourtyEight(4)
    
    stillPlaying = True

    while stillPlaying:
        test.printBoard()
        move = input("Move: ")
        
        if move == "x":
            stillPlaying = False
            
        test.step(move)
