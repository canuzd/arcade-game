x = int(input())
y = int(input())
g = int(input())

matrix = []
shipindex = 0
shiplineindex = x + g
totalasteroids = x * y
time = 0
score = 0
clash = 0

for i in range(x):
    clusterlines = "*" * y
    matrix.append(list(clusterlines))
for j in range(g):
    spacelines = " " * y
    matrix.append(list(spacelines))

if y % 2 != 0:
    s = (" " * (y//2) + "@" + " " * (y//2))
    shipline = list(s)
    matrix.append(shipline)
    shipindex = (y//2)
else:
    s = (" " * ((y//2)-1) + "@" + " " * (y//2))
    shipline = list(s)
    matrix.append(shipline)
    shipindex = (y // 2) -1

if x != 0 and y != 0:
    for lines in matrix:
        print("".join(lines))
    print("-" * 72)

elif x == 0 or y == 0:
    print("YOU WON!")
    for lines in matrix:
        print("".join(lines))
    print("-" * 72)
    print("YOUR SCORE:",score)


while x != 0 and y != 0:
    command = input("Choose your action!\n").lower()

    if command == "left":
        if shipindex > 0:
            matrix[shiplineindex].pop(shipindex)
            shipindex -= 1
            matrix[shiplineindex].insert(shipindex,"@")
            time += 1
        elif shipindex == 0:
            time += 1
        if time % 5 != 0:
            for lines in matrix:
                print("".join(lines))
            print("-" * 72)
    elif command == "right":
        if shipindex < y-1:
            matrix[shiplineindex].pop(shipindex)
            shipindex += 1
            matrix[shiplineindex].insert(shipindex,"@")
            time += 1
        elif shipindex == y-1:
            time += 1
        if time % 5 != 0:
            for lines in matrix:
                print("".join(lines))
            print("-" * 72)
    elif command == "fire":
        for b in range(shiplineindex):
            if matrix[shiplineindex-1-b][shipindex] == " ":
                matrix[shiplineindex-1-b][shipindex] = "|"
                for lines in matrix:
                    print("".join(lines))
                print("-" * 72)
                matrix[shiplineindex - 1 - b][shipindex] = " "
                if b == shiplineindex-1 :
                    matrix[shiplineindex - 1 - b][shipindex] = " "
                    time += 1
                    if time % 5 != 0:
                        for lines in matrix:
                            print("".join(lines))
                        print("-" * 72)
            elif matrix[shiplineindex-1-b][shipindex] == "*":
                matrix[shiplineindex - 1 - b][shipindex] = " "
                score += 1
                time += 1
                if time % 5 != 0 and score != totalasteroids:
                    for lines in matrix:
                        print("".join(lines))
                    print("-" * 72)
                break
    elif command == "exit":
        for lines in matrix:
            print("".join(lines))
        print("-" * 72)
        print("YOUR SCORE:",score)
        break
    else:
        time += 1
        if time % 5 != 0:
            for lines in matrix:
                print("".join(lines))
            print("-" * 72)


    if time % 5 == 0:
        for k in range(len(matrix)-1,-1,-1):
            if ("*" in matrix[k]) and ("@" not in matrix[k+1]):
                matrix[k+1] = matrix[k]
                matrix[k] = list((" " * y))
                clash = 0
            elif ("*" in matrix[k]) and ("@" in matrix[k+1]):
                clash = 1
                break
            else:
                continue

    if clash == 1:
        print("GAME OVER")
        for lines in matrix:
            print("".join(lines))
        print("-" * 72)
        print("YOUR SCORE:",score)
        break
    elif time % 5 == 0 and clash == 0 and score != totalasteroids:
        for lines in matrix:
            print("".join(lines))
        print("-" * 72)


    if score == totalasteroids :
        print("YOU WON!")
        for lines in matrix:
            print("".join(lines))
        print("-" * 72)
        print("YOUR SCORE:",score)
        break