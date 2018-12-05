file = open('day3_input.txt','r')

lines = file.readlines()
# PART 1

def readLine(line):
    line = line.split()
    #[id,'@','initColumn,initRow','spanColumnxspanRow']

    commaPos = line[2].index(',')
    xPos = line[3].index('x')

    initColumn = line[2][:commaPos]
    initRow = line[2][commaPos+1:-1]

    spanColumn = line[3][:xPos]
    spanRow = line[3][xPos+1:]

    return[int(initColumn),int(initRow),int(spanColumn),int(spanRow)]

#lines = ['1 @ 1,3: 4x4','2 @ 3,1: 4x4', '3 @ 5,5: 2x2']

for index, line in enumerate(lines):
    lines[index] = readLine(line.strip())


import numpy as np
matrix = np.zeros((1000,1000))

for line in lines:
    for column in range(line[0]-1,line[0]+line[2]-1):
        for row in range(line[1]-1,line[1]+line[3]-1):
            matrix[row][column] +=1

count = 0
for row in matrix:
    count += len(list(filter(lambda x: x > 1, row)))
print(count)


# PART 2

for index, line in enumerate(lines):
    isDiff = 0
    for column in range(line[0]-1,line[0]+line[2]-1):
        for row in range(line[1]-1,line[1]+line[3]-1):
            if matrix[row][column] > 1:
                isDiff += 1
                break
        if isDiff != 0:
            break
    if isDiff ==0:
        print(index+1) #0-index in Python but not real-life
        
