def solution(park, routes):
    route_list = []
    garo = len(park[0])
    sero = len(park)
    row = 0
    col = 0
    # 시작점 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                row, col = [i,j]
    
    # 문자열 -> 리스트화
    for route in routes:
        direction, step = route.split()
        route_list.append([direction,int(step)])
        

    for route in route_list:
        if(is_movable(park,route[0],route[1],row,col,garo, sero) and route[0] == "E"):
            col += route[1]
        elif(is_movable(park,route[0],route[1],row,col,garo, sero) and route[0] == "W"):
            col -= route[1]
        elif(is_movable(park,route[0],route[1],row,col,garo, sero) and route[0] == "S"):
            row += route[1]
        elif(is_movable(park,route[0],route[1],row,col,garo, sero) and route[0] == "N"):
            row -= route[1]      
    return [row,col]

def is_movable(park, direction, step, row, col, garo, sero):
    # 공원 넘는지 확인
    if (direction == "E"):
        if(col + step > garo - 1):
            return False
    elif(direction == "W"):
        if(col - step < 0):
            return False
    elif(direction == "S"):
        if(row + step > sero - 1):
            return False
    elif(direction == "N"):
        if(row - step < 0):
            return False
    # 장애물 있는지 확인
    if (direction == "E"):
        for i in range(1, step + 1):
            if(park[row][col+i] == "X"):
                return False
    elif (direction == "W"):
        for i in range(1, step + 1):
            if(park[row][col-i] == "X"):
                return False
    elif (direction == "S"):
        for i in range(1,step + 1):
            if(park[row+i][col] == "X"):
                return False
    elif (direction == "N"):
        for i in range(1,step + 1):
            if(park[row-i][col] == "X"):
                return False
    return True