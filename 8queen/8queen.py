def create_check():
    return [[0]*8 for _ in range(8)]

def examine(row,col,check):
    move = [(-1,1),(0,1),(1,1),
            (-1,0),(0,0),(1,0),
            (-1,-1),(0,-1),(1,-1)]
    available = []
    for (a, b) in move:
        for i in range(8):
            if 0 <= col + b*i < 8 and 0 <= row + a*i < 8:
                available.append(check[row + a*i][col + b*i])
    if 1 in available:
        return False
    else:
        return True

def solve(check, row, count):
    if row == 8:
        count[0] += 1
        return
    for col in range(8):
        if examine(row, col, check):
            check[row][col] = 1
            solve(check, row + 1, count)
            check[row][col] = 0

def main():
    count = [0]
    check = create_check()
    solve(check,0,count)
    print(count)

if __name__ == "__main__":
    main()