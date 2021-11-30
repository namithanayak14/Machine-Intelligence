def search_q(front, path):
    for index in range(len(front)):
        if front[index][1] == path:
            return index

def A_star_Traversal(cost, heuristic, start_point, goals):

    explored = []
    path = [start_point]
    front = [[0+heuristic[start_point], path]]
    while len(front) > 0:
        curr_cost, curr_path = front.pop(0)
        n = curr_path[-1]
        curr_cost -= heuristic[n]
        if n in goals:
            return curr_path
        explored.append(n)
        children = [i for i in range(len(cost[0]))
                    if cost[n][i] not in [0, -1]]
        for i in children:
            new_curr_path = curr_path + [i]
            new_path_cost = curr_cost + cost[n][i] + heuristic[i]
            if i not in explored and new_curr_path not in [i[1] for i in front]:
                front.append((new_path_cost, new_curr_path))
                front = sorted(front, key=lambda x: (x[0], x[1]))
            elif new_curr_path in [i[1] for i in front]:
                index = search_q(front, new_curr_path)
                front[index][0] = min(front[index][0], new_path_cost)
                front = sorted(front, key=lambda x: (x[0], x[1]))
    return path



def DFS_Traversal(cost, start_point, goals):

    path=[]
    visited = [False]*(len(cost[0]))
    help(cost, start_point, path, visited, goals)
    return path

def help(cost, start_point, path, visited, goals):

    visited[start_point] = True
    path.append(start_point)
    if (start_point not in goals):
        temp = cost[start_point]
        for i in range(len(temp)):
            if ((visited[i] == False) and (temp[i] > 0)):
                r = help(cost, i, path, visited, goals)
                if r == -1:
                    return -1
                path.pop()
    else:
        return -1
