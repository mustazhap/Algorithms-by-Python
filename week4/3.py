dist = []

def bfs():
    
    queue = [1,3,5,2,2,5,2,4]
    print("Input:  " ,*queue)
    
    while len(queue):        
        if len(queue) != 1:
            a = queue[0]
            b = queue[1]
            queue.pop(0)
                        
            if a < b:
                dist.append(b)
            if a >= b:
                for i in queue:
                    if a>=i and a >= max(queue):
                        dist.append(0)
                        break;
                        
                        
                    if a < i:
                        dist.append(i)
                        break;
                    
        if len(queue) == 1:
            dist.append(0)
            print("Output: ", *dist)
            return
          
            

bfs()
