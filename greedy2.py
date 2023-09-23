import numpy as np


if __name__ == "__main__":


    TopLabel=""
    TopWrite=""
    TopShow=""
    TopF=""
    for i in range(5):
        #create input file name
        namefile = "0"+ str(i) + ".txt"
    #open input file
        with open(namefile, "r") as f:
            #read first 3 integers
            C, R, S = map(int, f.readline().split())
            #read next line and convert to list of integers
            snakeLenghts = list(map(int, f.readline().split()))
            #print snake lenghts
    
            #create output file
            out = open("output"+ namefile, "w")
            #create empty matrix
            matrix = []
            for i in range(R):
                #read next line and convert to list of characters not counting spaces
                row = list(f.readline().replace("\n", "").split(" "))
                
                #add row to matrix
                matrix.append(row)
            

            #explore matrix and save wormholes positions
            wormholes = []
            for i in range(R):
                for j in range(C):
                    if matrix[i][j] == '*':
                        wormholes.append([i, j])


            
            
            
            #for every snake
            for i in range(S):
                #get snake length
                snakeLenght = snakeLenghts[i]
                #get row and column of maximum value
                HeadRow, HeadCol = np.unravel_index(np.argmax(matrix), (R, C))
                #write row and column to output file
                #out.write(str(HeadCol) + " " + str(HeadRow) + " ")
                path = str(HeadCol) + " " + str(HeadRow) + " "
                #set snake head to -
                matrix[HeadRow][HeadCol] = '-'
                takeHole = -1
                #rWorm = -1
                #cWorm = -1
                #for snake lenght
                skip = False
                for j in range(snakeLenght):
                    if skip:
                        skip = False
                        continue
                    #search the maximum value adjacent to the current snake head

                    #exploring wormholes
                    if (matrix[(HeadRow - 1)%R][HeadCol] !='*' and matrix[(HeadRow - 1)%R][HeadCol] != '-'):
                        top = matrix[(HeadRow - 1)%R][HeadCol]
                    elif (matrix[(HeadRow - 1)%R][HeadCol] == '*'):
                        #explore wormhole
                        wormRow = (HeadRow - 1)%R
                        wormCol = HeadCol
                        maxs = -10001
                        for worm in wormholes:
                            #if worm[0] != wormRow and worm[1] != wormCol:
                            topW = matrix[(worm[0] - 1)%R][worm[1]] if (matrix[(worm[0] - 1)%R][worm[1]] !='*' and matrix[(worm[0] - 1)%R][worm[1]] != '-')  else -10001
                            bottomW = matrix[(worm[0] + 1)%R][worm[1]] if (matrix[(worm[0] + 1)%R][worm[1]] !='*' and matrix[(worm[0] + 1)%R][worm[1]] != '-') else -10001
                            leftW = matrix[worm[0]][(worm[1] - 1)%C] if (matrix[worm[0]][(worm[1] - 1)%C] !='*' and matrix[worm[0]][(worm[1] - 1)%C] != '-') else -10001
                            rightW = matrix[worm[0]][(worm[1] + 1)%C] if (matrix[worm[0]][(worm[1] + 1)%C] !='*' and matrix[worm[0]][(worm[1] + 1)%C] != '-') else -10001
                            #get the maximum value
                            maximum = max(int(topW), int(bottomW), int(leftW), int(rightW))/2
                        if maximum > maxs:
                            maxs = maximum
                            rWormU = worm[0]
                            cWormU = worm[1]
                            if maximum == int(topW)/2: 
                                TopLabel = "U "
                            elif maximum == int(bottomW)/2:
                                TopLabel = "D "
                            elif maximum == int(leftW)/2:
                                TopLabel = "L "
                            elif maximum == int(rightW)/2:
                                TopLabel = "R "
                            
                                

                        top = maxs
                        takeHole = 1
                    else:
                        top = -10001
                    

                    if (matrix[(HeadRow + 1)%R][HeadCol] !='*' and matrix[(HeadRow + 1)%R][HeadCol] != '-'):
                        bottom = matrix[(HeadRow + 1)%R][HeadCol]
                    elif (matrix[(HeadRow + 1)%R][HeadCol] == '*'):
                        #explore wormhole
                        wormRow = (HeadRow + 1)%R
                        wormCol = HeadCol
                        maxs = -10001
                        for worm in wormholes:
                            if worm[0] != wormRow and worm[1] != wormCol:
                                topW = matrix[(worm[0] - 1)%R][worm[1]] if (matrix[(worm[0] - 1)%R][worm[1]] !='*' and matrix[(worm[0] - 1)%R][worm[1]] != '-')  else -10001
                                bottomW = matrix[(worm[0] + 1)%R][worm[1]] if (matrix[(worm[0] + 1)%R][worm[1]] !='*' and matrix[(worm[0] + 1)%R][worm[1]] != '-') else -10001
                                leftW = matrix[worm[0]][(worm[1] - 1)%C] if (matrix[worm[0]][(worm[1] - 1)%C] !='*' and matrix[worm[0]][(worm[1] - 1)%C] != '-') else -10001
                                rightW = matrix[worm[0]][(worm[1] + 1)%C] if (matrix[worm[0]][(worm[1] + 1)%C] !='*' and matrix[worm[0]][(worm[1] + 1)%C] != '-') else -10001
                                #get the maximum value
                                maximum = max(int(topW), int(bottomW), int(leftW), int(rightW))/2
                            if maximum > maxs:
                                maxs = maximum
                                rWormD = worm[0]
                                cWormD = worm[1]
                                if maximum == int(topW)/2:
                                    TopWrite = "U "
                                elif maximum == int(bottomW)/2:
                                    TopWrite = "D "
                                elif maximum == int(leftW)/2:
                                    TopWrite = "L "
                                elif maximum == int(rightW)/2:
                                    TopWrite = "R "
                                    

                                    
                        bottom = maxs
                        takeHole = 2
                    else:
                        bottom = -10001

                    if (matrix[HeadRow][(HeadCol - 1)%C] !='*' and matrix[HeadRow][(HeadCol - 1)%C] != '-'):
                        left = matrix[HeadRow][(HeadCol - 1)%C]
                    elif (matrix[HeadRow][(HeadCol - 1)%C] == '*'):
                        #explore wormhole
                        wormRow = HeadRow
                        wormCol = (HeadCol-1)%C
                        maxs = -10001
                        for worm in wormholes:
                            if worm[0] != wormRow and worm[1] != wormCol:
                                topW = matrix[(worm[0] - 1)%R][worm[1]] if (matrix[(worm[0] - 1)%R][worm[1]] !='*' and matrix[(worm[0] - 1)%R][worm[1]] != '-')  else -10001
                                bottomW = matrix[(worm[0] + 1)%R][worm[1]] if (matrix[(worm[0] + 1)%R][worm[1]] !='*' and matrix[(worm[0] + 1)%R][worm[1]] != '-') else -10001
                                leftW = matrix[worm[0]][(worm[1] - 1)%C] if (matrix[worm[0]][(worm[1] - 1)%C] !='*' and matrix[worm[0]][(worm[1] - 1)%C] != '-') else -10001
                                rightW = matrix[worm[0]][(worm[1] + 1)%C] if (matrix[worm[0]][(worm[1] + 1)%C] !='*' and matrix[worm[0]][(worm[1] + 1)%C] != '-') else -10001
                                #get the maximum value
                                maximum = max(int(topW), int(bottomW), int(leftW), int(rightW))/2
                            if maximum > maxs:
                                maxs = maximum
                                rWormL = worm[0]
                                cWormL = worm[1]
                                if maximum == int(topW)/2:
                                    TopShow = "U "
                                elif maximum == int(bottomW)/2:
                                    TopShow = "D "
                                elif maximum == int(leftW)/2:
                                    TopShow = "L "
                                elif maximum == int(rightW)/2:
                                    TopShow = "R "
                                
                        left = maxs
                        takeHole = 3
                    else:
                        left = -10001

                    if (matrix[HeadRow][(HeadCol + 1)%C] !='*' and matrix[HeadRow][(HeadCol + 1)%C] != '-'):
                        right = matrix[HeadRow][(HeadCol + 1)%C]
                    elif (matrix[HeadRow][(HeadCol + 1)%C] == '*'):
                        #explore wormhole
                        wormRow = HeadRow
                        wormCol = (HeadCol + 1)%C
                        maxs = -10001
                        for worm in wormholes:
                            if worm[0] != wormRow and worm[1] != wormCol:
                                topW = matrix[(worm[0] - 1)%R][worm[1]] if (matrix[(worm[0] - 1)%R][worm[1]] !='*' and matrix[(worm[0] - 1)%R][worm[1]] != '-')  else -10001
                                bottomW = matrix[(worm[0] + 1)%R][worm[1]] if (matrix[(worm[0] + 1)%R][worm[1]] !='*' and matrix[(worm[0] + 1)%R][worm[1]] != '-') else -10001
                                leftW = matrix[worm[0]][(worm[1] - 1)%C] if (matrix[worm[0]][(worm[1] - 1)%C] !='*' and matrix[worm[0]][(worm[1] - 1)%C] != '-') else -10001
                                rightW = matrix[worm[0]][(worm[1] + 1)%C] if (matrix[worm[0]][(worm[1] + 1)%C] !='*' and matrix[worm[0]][(worm[1] + 1)%C] != '-') else -10001
                                #get the maximum value
                                maximum = max(int(topW), int(bottomW), int(leftW), int(rightW))/2
                            if maximum > maxs:
                                maxs = maximum
                                rWormR = worm[0]
                                cWormR = worm[1]
                                if maximum == int(topW)/2:
                                    TopF = "U "
                                elif maximum == int(bottomW)/2:
                                    TopF = "D "
                                elif maximum ==int(leftW)/2:
                                    TopF = "L "
                                elif maximum == int(rightW)/2:
                                    TopF = "R "
                                
                        right = maxs
                        takeHole = 4
                    else:
                        right = -10001





                    #get the maximum value
                    maxVal = max(int(top), int(bottom), int(left), int(right))
                    #if maxval is - 
                    if maxVal == -10001:
                        #out.write("\n")
                        path = ""
                        break

                    #if the maximum value is the top
                    if maxVal == int(top):
                        if takeHole != 1:
                            #move the snake head to the top
                            HeadRow = (HeadRow - 1)%R
                            #replace the value of the new snake head with -
                            matrix[HeadRow][HeadCol] = '-'
                            #wrote on output file
                            #out.write("U ")
                            path = path + "U "
                        else:
                            HeadRow = rWormU
                            HeadCol = cWormU
                            path = path + str(cWormU) + " " + str(rWormU) + " " + str(TopLabel)
                            if TopLabel == "U ":
                                HeadRow = (HeadRow - 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopLabel == "D ":
                                HeadRow = (HeadRow + 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopLabel == "L ":
                                HeadCol = (HeadCol - 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopLabel == "R ":
                                HeadCol = (HeadCol + 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            skip = True

                    #if the maximum value is the bottom
                    elif maxVal == int(bottom):

                        if takeHole != 2:
                            #move the snake head to the bottom
                            HeadRow = (HeadRow + 1)%R
                            #replace the value of the new snake head with -
                            matrix[HeadRow][HeadCol] = '-'
                            #wrote on output file
                            #out.write("D ")
                            path = path + "D "
                        else:
                            HeadRow = rWormD
                            HeadCol = cWormD
                            path = path + str(cWormD) + " " + str(rWormD) + " " + str(TopWrite)
                            if TopWrite == "U ":
                                HeadRow = (HeadRow - 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopWrite == "D ":
                                HeadRow = (HeadRow + 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopWrite == "L ":
                                HeadCol = (HeadCol - 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopWrite == "R ":
                                HeadCol = (HeadCol + 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            skip = True

                    #if the maximum value is the left
                    elif maxVal == int(left):
                        if takeHole != 3:
                            #move the snake head to the left
                            HeadCol = (HeadCol - 1)%C
                            #replace the value of the new snake head with -
                            matrix[HeadRow][HeadCol] = '-'
                            #wrote on output file
                            #out.write("L ")
                            path = path + "L "
                        else:
                            HeadRow = rWormL
                            HeadCol = cWormL
                            path = path + str(cWormL) + " " + str(rWormL) + " " + str(TopShow)
                            if TopShow == "U ":
                                HeadRow = (HeadRow - 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopShow == "D ":
                                HeadRow = (HeadRow + 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopShow == "L ":
                                HeadCol = (HeadCol - 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopShow == "R ":
                                HeadCol = (HeadCol + 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            skip = True

                    #if the maximum value is the right
                    elif maxVal == int(right):
                        if takeHole != 4:
                            #move the snake head to the right
                            HeadCol = (HeadCol + 1)%C
                            #replace the value of the new snake head with -
                            matrix[HeadRow][HeadCol] = '-'
                            #wrote on output file
                            #out.write("R ")
                            path = path + "R "
                        else:
                            HeadRow = rWormR
                            HeadCol = cWormR
                            path = path + str(cWormR) + " " + str(rWormR) + " " + str(TopF)
                            if TopF == "U ":
                                HeadRow = (HeadRow - 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopF == "D ":
                                HeadRow = (HeadRow + 1)%R
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopF == "L ":
                                HeadCol = (HeadCol - 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            elif TopF == "R ":
                                HeadCol = (HeadCol + 1)%C
                                matrix[HeadRow][HeadCol] = '-'
                            skip = True

                #write new line on output file
                out.write(path + "\n")
            #close output file
            out.close()