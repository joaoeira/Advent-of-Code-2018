input = open('day2_input.txt','r')

lines = input.readlines()

for index, line in enumerate(lines):
    lines[index] = line.strip()

# PART 1

doubles = 0 
triplets = 0

for line in lines:

    hasDouble = False
    hasTriplet = False
    for i in set(line):
        if line.count(i) == 2 and hasDouble == False:
            doubles += 1
            hasDouble = True
        if line.count(i) == 3 and hasTriplet == False:
            triplets+=1
            hasTriplet = True


print(doubles*triplets)

# PART 2

def unionDiff(array1,array2):
  
    # set(array) gives an unordered list of uniques
    # thus if the intersection of the sets of the two arrays
    # has a length difference of more or equal than 2 that means
    # there is at least a 2 character difference between the sets
    # and we can discard that pair of arrays for comparison
     
     
    if len(set(array1) | set(array2)) - len(array1) >= 2 or len(set(array1) | set(array2)) - len(array2) >= 2:
        return False
    else:
        return True


pairs = []

for i in range(len(lines)-1):
    for j in range(i+1,len(lines)):
        if unionDiff(lines[i],lines[j]) == True:
            pairs.append([lines[i],lines[j]])

for pair in pairs:
    isDiff = 0
    for i in range(len(pair[0])):
        if pair[0][i] != pair[1][i]:
            isDiff +=1
    if isDiff <= 1:
        print(pair) #you can eyeball the answer with this