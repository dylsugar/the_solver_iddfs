import math
import os
import sys
import time

class Board:
    def __init__(self,tiles):
        self.size = int(math.sqrt(len(tiles)))
        self.tiles = tiles

    def execute_action(self,action):
        new_tiles = self.tiles[:]
        empty_index = new_tiles.index('0')
        if action=='L':
            if empty_index%self.size>0:
                new_tiles[empty_index-1],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index-1]
        if action=='R':
            if empty_index%self.size < (self.size-1):
                new_tiles[empty_index+1],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index+1]  
        if action=='U':
            if empty_index - self.size >= 0:
                new_tiles[empty_index-self.size],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index-self.size]  
        if action=='D':
            if empty_index + self.size < self.size*self.size:
                new_tiles[empty_index+self.size],new_tiles[empty_index] = new_tiles[empty_index],new_tiles[empty_index+self.size] 
        return Board(new_tiles)

class Node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self):
        return str(self.state.tiles)

    def __eq__(self,other):
        return self.state.tiles == other.state.tiles

    def __hash__(self):
        return hash(self.state)


def get_children(parent_node):
    children = []
    actions = ['L','R','U','D']
    for action in actions:
        child_state = parent_node.state.execute_action(action)
        child_node = Node(child_state,parent_node,action)
        children.append(child_node)
    return children


def find_path(node):
    path = []
    while(node.parent is not None):
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path


def goal_test():
        return ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']


def IDDFS(src,target,max_depth):
    start_time = time.time()
    count = 0
    for limit in range(max_depth):
        if DLS(src,target,limit,count) == True:
            end_time = time.time()
            print("Time Taken: " + str(end_time - start_time))
            return True

    return False


def DLS(src,target,limit,count):
    count+=1
    if(src.state.tiles == target):
        print("Moves: " + str(' '.join(find_path(src))))
        print("Number of Nodes Expanded: " + str(count)) 
        return True
    if limit <= 0:
        return False
    
    for child in get_children(src):
        if DLS(child,goal_test(),limit-1,count) == True:
            return True
    return False


def main(argv):
    max_depth = 10
    root = Node(Board(argv),None,None)
    x = IDDFS(root,goal_test(),max_depth)
    

if __name__=="__main__":
    main(sys.argv[1:])
