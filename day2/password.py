input = open("day2/passwords.txt","r")
counter = 0

for line in input:
    line = line.strip("\n")
    scopeChar = line [line.find(':')-1:line.find(':')]
    apperance = line.count(scopeChar) - 1
    
    minimum = ""
    for c in line[:line.find('-')]:
        minimum += c;
    maximum = ""
    for c in line[line.find("-")+1:]:
        if c.isdigit():
            maximum += c
        else:
            break;
    
    #For part one
    # if apperance >= int(minimum) and apperance <= int(maximum):
    #     print("Approves with guidelines: " + line)
    #     counter +=1

    #For part two
    password = line.split(" ")
    password = password[len(password)-1]
    if bool(password[int(minimum)-1] == scopeChar) != bool(password[int(maximum)-1] == scopeChar):
        print(line)
        counter +=1


print("Fitting passwords: " + str(counter))
            
