forest = []

def append_forest():
    input_reader = open("day3/trees.txt","r")
    line_counter = 0
    for line in input_reader:
        line = line.strip("\n")
        row = []
        for c in line:
            row.append(c)
        
        try:
            forest[line_counter] = forest[line_counter] + row
        except IndexError:
            forest.append(row)

        line_counter += 1

def ride_the_slope(right, down):
    tree_counter = 0
    col = 0
    append_forest()
    for row in range(0,len(forest),down):
        try:
            if forest[row][col] == "#":
                tree_counter += 1
        except IndexError:
            append_forest()
            if forest[row][col] == "#":
                tree_counter += 1
        col += right
    return tree_counter

print(ride_the_slope(1,1) * ride_the_slope(3,1) * ride_the_slope(5,1) * ride_the_slope(7,1) * ride_the_slope(1,2))

def print_forest():
    for i in forest:
        print(str(i) + " " + str(len(i)))
    print(len(forest)) 