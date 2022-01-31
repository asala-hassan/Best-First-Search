class Graph:
   
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
    
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors 
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # list of nodes 
    def nodes(self):
        n1 = set([k for k in self.graph_dict.keys()])
        n2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = n1.union(n2)
        return list(nodes)

class Node:

    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance 
        self.h = 0 # heuristic

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.h < other.h
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.h))

def greedy(graph, heuristics, start, goal):
    
    # lists for open nodes and expanded nodes
    open = []
    expanded = []
    start_node = Node(start, None)
    goal_node = Node(goal, None)
    open.append(start_node)
    
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        expanded.append(current_node)
        
        if current_node == goal_node:
            path = []

            print('Number of expanded nodes:',len(expanded))
            distance= (current_node.g)
            print('Distance:',distance)
            
            while current_node != start_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.append(start_node.name)
            return path[::-1]
     
        neighbors = graph.get(current_node.name)
      
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)
            if(neighbor in expanded):
                continue
            
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            
            if(add_to_open(open, neighbor) == True):
                
                open.append(neighbor)
    
    return None

   
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.h >= node.h):
            return False
    return True

def main():
    graph = Graph()
    
    graph.connect('Alexandria', 'Cairo',112 )
    graph.connect('Alexandria', 'Matruh', 159)
    graph.connect('Alexandria', 'Nekhel', 245)
    graph.connect('Cairo', 'Alexandria', 112)
    graph.connect('Cairo', 'Asyut',198)
    graph.connect('Cairo', 'Bawiti', 186)
    graph.connect('Matruh', 'Alexandria', 159)
    graph.connect('Matruh', 'Siwa', 181)
    graph.connect('Nekhel', 'Alexandria', 245)
    graph.connect('Nekhel', 'Quseir',265 )
    graph.connect('Nekhel', 'Suez', 72)
    graph.connect('Siwa', 'Bawiti', 210)
    graph.connect('Siwa', 'Matruh',181)
    graph.connect('Bawiti', 'Cairo', 186)
    graph.connect('Bawiti', 'Qasr Farafra', 104)
    graph.connect('Bawiti', 'Siwa', 210)
    graph.connect('Asyut', 'Cairo', 198)
    graph.connect('Qasr Farafra', 'Bawiti', 104)
    graph.connect('Qasr Farafra', 'Mut', 126)
    graph.connect('Sohag', 'Mut', 184)
    graph.connect('Sohag', 'Qena', 69)
    graph.connect('Sohag', 'Quseir', 163)
    graph.connect('Quseir', 'Nekhel', 265)
    graph.connect('Quseir', 'Sohag', 163)
    graph.connect('Suez', 'Nekhel',72)
    graph.connect('Mut', 'Qasr Farafra', 126)
    graph.connect('Mut', 'Sohag', 184)
    graph.connect('Mut', 'Kharga', 98)
    graph.connect('Kharga','Mut', 98)
    graph.connect('Qena', 'Luxor',33 )
    graph.connect('Luxor', 'Qena',33 )
    

    heuristics = {}#h2
    heuristics['Cairo'] = 139
    heuristics['Matruh'] = 189
    heuristics['Nekhel'] = 145
    heuristics['Siwa'] = 148
    heuristics['Bawiti'] = 118
    heuristics['Asyut'] = 67
    heuristics['Qasr Farafra'] = 77
    heuristics['Sohag'] = 36
    heuristics['Quseir'] = 59
    heuristics['Mut'] = 65
    heuristics['Qena'] = 19
    heuristics['Suez'] = 136
    heuristics['Kharga'] = 38
    heuristics['Luxor'] = 0
    
    path = greedy(graph, heuristics, 'Alexandria', 'Luxor')
    print('Path:',path)
    
    
if __name__ == "__main__": main()