class Node:
    def __init__(self,state,action,cost,parent):
        self.state=state
        self.action=action
        self.cost=cost
        self.parent=parent

input_list=list()
actions=list()
state_description=list()
transition_table=list()
tests=list()


def inputFromFile():
    for number in input().replace('\n',''):
        if(number==' '):
            continue
        input_list.append(int(number))
    
    input()#skip nextline
    for _ in range(0,input_list[0]):
        state_description.append(input().strip('\n'))

    input()
    for _ in range(0,input_list[1]):
        actions.append(input().strip('\n'))

    input()
    for _ in range(0,input_list[0]):
        line = input().strip('\n')
        row=list()
        for number in line.strip(' ').replace('\n',''):
            if(number==' '):
                continue
            row.append(int(number))
        transition_table.append(row)

    input()
    for _ in range(0,input_list[2]):
        tests.append(input().strip('\n'))



def goalTest(state,final):
    if state==final:
        return True
    return False



def Graph_Search(problem):
    initial,final = problem.split('\t') 
    initial_Node = Node(state_description.index(initial),-1,0,None)
    final_state = state_description.index(final)

    if goalTest(initial_Node.state,final_state):
        return Solution(initial_Node)
    Frontier = list()

    explore = set()
    Frontier.append(initial_Node)     
    while True:
        if len(Frontier)==0:
            return None
        node = Frontier.pop(0)        
        explore.add(node.state)
    
        for action in range(len(actions)):
            child = Node(transition_table[node.state][action],action,node.cost+1,node)
            if not(child.state in explore) or not(child.state in [item.state for item in Frontier]):
                if goalTest(child.state,final_state):
                    return Solution(child)
                Frontier.append(child)
 
    
def Solution(node):
    if node is None: return None
    path =[]
    while True:
        path.append(actions[node.action])
        node = node.parent
        if (node.parent is None):
            break
    path.reverse()
    return path

def start():
    inputFromFile()
    
    for test in tests:
        path_string=""
        path = Graph_Search(test)
        if path is None:
            print("Failure")
        else:
            for step in path:
                path_string += step+'->'
            print(path_string[:-2])

start()
