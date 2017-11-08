dist = {}

def bfs():
    start = 0,0
    end = 3,3

    steps = [(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(-1,2),(-2,1),(2,-1)]
    queue = [start]
    dist[start] = 0
    
    while len(queue):
        a = queue[0]
        queue.pop(0)
        if a == end:
            print ("reached goal in %d moves"%(dist[a]))
            return

        for move in steps:
            next_pos = a[0]+move[0], a[1]+move[1]
            if next_pos[0] > end[0] or next_pos[1] > end[1] or next_pos[0] < 1 or next_pos[1] < 1:
                
                continue
           
            if next_pos not in dist:
                
                dist[next_pos] = dist[a]+1
                
                queue.append(next_pos)
               

bfs()
