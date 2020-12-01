input = open("day1/expense_report.txt","r")
expenses = []

for line in input:
    expenses.append(int(line.strip("\n")));

def first():
    for i in expenses:
        for j in expenses:
            if (i + j) == 2020:
                print("Double Result: " + str(i*j))
                return

def second():
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if (i + j + k) == 2020:
                    print("Triple Result: " + str(i*j*k))
                    return

first()
second()