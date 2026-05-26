def solution(record):
    answer = []
    # uid와 nickname 매핑하는 해시
    id_map = {}
    for i in range(len(record)):
        data = record[i].split()
        action = data[0]
        uid = data[1]
        if action == "Enter" or action == "Change":
            nickname = data[2]
            
        if action == "Enter" and uid in id_map:
            id_map[uid] = nickname
        elif action == "Enter" and uid not in id_map:
            id_map[uid] = nickname
        elif action == "Change":
            id_map[uid] = nickname
        elif action == "Leave":
            pass
        
    for i in range(len(record)):
        data = record[i].split()
        action = data[0]
        uid = data[1]
        if action == "Enter" or action == "Change":
            nickname = data[2]
            
        if action == "Enter":
            answer.append(f"{id_map[uid]}님이 들어왔습니다.") 
        elif action == "Change":
            pass
        elif action == "Leave":
            answer.append(f"{id_map[uid]}님이 나갔습니다.")
    return answer