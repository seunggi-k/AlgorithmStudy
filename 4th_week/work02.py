from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 이를 위해서 북, 동, 남, 서 순서를 정의해보겠습니다!
#        r    c
# 북   -1  0
# 동   0    1
# 남   1    0
# 서   0  -1
#
# 이 정보를 아래와 같이 배열에 담아둡니다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 북쪽이면 0 번째 인덱스이므로 dr[0], dc[0] 을 사용해 이동하면 -1, 0 을 이동합니다.
# 동쪽이면 1 번째 인덱스이므로 dr[1], dc[1] 을 사용해 이동하면 0, 1 을 이동합니다.
# 이런식으로 방향 개념을 정의할 수 있습니다!
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


def get_d_index_when_go_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = deque([[r, c, d]])
    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)  # 북 -> 서
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            ## a
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            ## c
            elif i == 3:
                temp_d=get_d_index_when_go_back(d)
                new_r, new_c = r + dr[temp_d], c + dc[temp_d]
                queue.append([new_r,new_c,d])
                # d
                if room_map[new_r][new_c]==1:
                    return count_of_departments_cleaned
    return count_of_departments_cleaned


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
