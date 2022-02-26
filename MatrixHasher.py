class MatrixHasher:
    def __init__(self) -> None:
        pass

    def matrixToString(self, matrix: list) -> str:
        return str(matrix)
    
    def stringToMatrix(self, string: str) -> list:
        matrix = []

        s = string.split("[")

        for i in range(0, len(s)):
            if s[i] != "":
                temp = s[i].split(",")
                tempRow = []

                for j in range(0, len(temp)):
                    # If its a number but not the last number
                    if temp[j].isnumeric() and not "]" in temp[j]:
                        tempRow.append(int(temp[j]))
                    elif temp[j][0].isnumeric():
                        tempRow.append(int(temp[j][0]))
                        break
                
                matrix.append(tempRow)
        
        return matrix
                

if __name__ == "__main__":
    test = MatrixHasher()
    print(test.stringToMatrix("[[1,2,3],[45,6,7]]"))
    print(test.stringToMatrix("[[13,4,5],[89,8],[7,5,3]]"))