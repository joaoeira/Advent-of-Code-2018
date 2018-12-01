#part 1
input = open('day1_input.txt','r')

lines = input.readlines()
result = 0
for i in lines:
    result += int(i)

print(result)

#part2

frequency = [0]
index = 0
finalState = False

while True:    
    for i in lines:
        if(frequency[index] + int(i) in frequency):
            print(frequency[index] + int(i))
            finalState = True
            break
        else:
            #print(frequency[index])
            frequency.append(frequency[index] + int(i))
            index +=1
    if(finalState == True):
        break
