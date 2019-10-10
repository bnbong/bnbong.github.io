def get_integer(message,i,j): #숫자입력하는 함수
    number = input(message)
    while not (i <= int(number) <= j): # 괄호 안에 조건식을 채운다.
        if (int(number) == False):
            number = input(message)
        number = input(message)
    return int(number)


import random
def create_board(): #정답보드1 만드는 함수
    seed = [1,2,3,4,5,6]
    ns = seed[:]
    solution = [ns]
    while(len(solution) != 6) :
        count = 0
        random.shuffle(seed)
        ns = seed[:]
        for x in range(0, len(seed)) :
            for s in solution :
                if (ns[x] != s[x]) :
                    count += 1
        if (count == len(seed)*len(solution)) :
            solution += [ns]
    return solution

def show_board(board): #입력창에 보드창 띄워주는 함수
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    iboard = board[:]
    for row in iboard:
        for j in range(len(row)):
            if row[j] == 0:
                row[j] = '.'
        print(i,'|',row[0],row[1],row[2],row[3],row[4],row[5])
            
        i = i + 1
            
    print()

def create_solution_board(): #정답보드 만드는 함수
    transposed = []
    board = create_board()
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        for i in range(len(board)):
            transposed[i].append(row[i])
            
    return transposed

    
def get_level(): #레벨선택함수
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    
    if level == "상":
        return 10
    if level == "중":
        return 8
    if level == "하":
        return 6
    # level 이 '하' 이면  return  6
    # level 이 '중' 이면  return  8
    # level 이 '상' 이면  return  10
    
def make_holes(puzzle,no_of_holes): #빈칸만드는함수
    holeset = set()
    import random
    while no_of_holes > 0:
        i = random.randint(0,5)
        j = random.randint(0,5)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
        else:
            continue
        no_of_holes = int(no_of_holes) - 1
        holeset.add((i,j))
    return (puzzle, holeset)

def sudokmini(): #본함수
    import copy
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy.deepcopy(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_integer("가로줄번호(1~6): ",1,6) - 1
        j = get_integer("세로줄번호(1~6): ",1,6) - 1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~6): ",1,6)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")

sudokmini()