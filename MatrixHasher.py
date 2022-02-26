class MatrixHasher:
    def __init__(self) -> None:
        pass

    def matrixToString(self, matrix: list) -> str:
        return str(matrix)
    
    def stringToMatrix(self, s: str) -> list:
        matrix = []

        # To chop off [ and ]
        x = 1
        while x < len(s)-1:
            # Row var
            if s[x] == "[":
                temp = []

            if s[x].isdigit():
                temp_s = s[x]

                # For more than 1 digit
                y = 1
                while s[x+y].isdigit():
                    temp_s += s[x+y]
                    y += 1
                
                # If number is more than one digit skip next chars
                if y > 1:
                    x = x + y
                
                temp.append(int(temp_s))

            # If end of row
            if s[x] == "]":
                matrix.append(temp)

            x += 1
        
        return matrix



if __name__ == "__main__":
    test = MatrixHasher()
    sm = test.matrixToString([[13,4,5],[89,8,6],[7,5,3]])
    print(sm)
    sm = test.stringToMatrix(sm)
    print(sm)