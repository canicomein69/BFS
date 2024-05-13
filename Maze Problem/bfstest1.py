from pyamaze import maze,agent,COLOR
from collections import deque

#def BFS(m):
    #start =(m.rows,m.cols)
    #frontier=[start]
    #explored=[start]
    #bfsPath={}

def BFS(m,start=None):
    if start is None:
        dtart=(m.rows,m.cols)
        frontier = deque()
        frontier.append(start)
        bfsPath = {}
        explored = [start]
        bSearch =[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d== 'E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
                bSearch.append(childCell)
    print(f'{bfsPath}')
    fwdpath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdpath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdpath

if __name__=='__namin__':
    m=maze(5,5)
    m.CreateMaze(5,4,loopPercent=100)
    bSearch,bfsPath,fwdpath=BFS(m)
    a=agent(m,footprints=True,color=COLOR.green,shape='square')
    b=agent(m,footpritns=True,color=COLOR.cyan,shape='square',filled=False)
    c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:bSearch},delay=300)
    m.tracePath({c:bfsPath})
    m.tracePath({b:fwdpath})

    m.run()
    