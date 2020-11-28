# Databricks notebook source
# MAGIC %md ###Graph

# COMMAND ----------

class Graph:
  def __init__(self):
    #dictionary contains key and mapping of corresponding vertex object
    self.vertices = {}
    
  def add_vertex(self,key):
    vertex = Vertex(key)
    self.vertices[key] = vertex
    
  def get_vertex(self,key):
    return self.vertices[key]
  
  def __contain__(self,key):
    return key in self.vertices
  
  def add_edge(self,src_key,dest_key,weight =1):
    self.vertices[src_key].add_neighbour(self.vertices[dest_key],weight)
    
  def does_edge_exit(self,src_key,dest_key):
    return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
  
  def add_undirected_edge(self,v1_key,v2_key,weight =1):
    self.add_edge(v1_key,v2_key,weight)
    self.add_edge(v2_key,v1_key,weight)
    
  def does_undirected_edge_exist(self,v1_key,v2_key):
    return self.does_edge_exit(v1_key,v2_key) and self.does_edge_exit(v2_key,v1_key)
  
  def __iter__(self):
    return iter(self.vertices.values())
    
class Vertex:
  def __init__(self,key):
    self.key = key
    self.point_to = {}
    
    
  def get_key(self):
    return self.key
  
  def add_neighbour(self,dest,weight):
    self.point_to[dest] = weight
    
  def get_neighbours(self):
    return self.point_to.keys()
  
  def get_weight(self,dest):
    return self.point_to[dest]
  
  def does_it_point_to(self,dest):
    return dest in self.point_to
    
    

# COMMAND ----------

g= Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A','B',300)
g.add_edge('A','C',500)
g.add_edge('A','D',300)
g.add_edge('B','C',350)
g.add_edge('C','D',306)
g.add_edge('C','F',330)
g.add_edge('D','F',200)
g.add_edge('D','A',100)




# COMMAND ----------

for v in g:
  for dest in v.get_neighbours():
    w = v.get_weight(dest)
    print('(src={}, dest={}, weight={}) '.format(v.get_key(),dest.get_key(), w))

# COMMAND ----------

# MAGIC %md ###Python Program to Implement Breadth-First Search on a Graph

# COMMAND ----------

#Graph and Vertex class is create above
class Queue:
  def __init__(self):
    self.items = []
    
  def enqueue(self,key):
    self.items.append(key)
   
  def dequeue(self):
    return self.items.pop(0)
  
  def isEmpty(self):
    return self.items == []

# COMMAND ----------

def display_bfs(vertex):
  visited = set()
  q = Queue()
  q.enqueue(vertex)
  visited.add(vertex)
  while not q.isEmpty():
    current = q.dequeue()
    print(current.get_key(),end=' ')
    for dest in current.get_neighbours():
      if dest not in visited:
        visited.add(dest)
        q.enqueue(dest)
  
  

# COMMAND ----------

g= Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1,2,300)
g.add_edge(1,3,500)
g.add_edge(1,4,300)
g.add_edge(2,3,350)
g.add_edge(3,4,306)
g.add_edge(3,6,330)
g.add_edge(4,6,200)
g.add_edge(4,1,100)

# COMMAND ----------

vertex = g.get_vertex(1)
display_bfs(vertex)

# COMMAND ----------

g= Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A','B',300)
g.add_edge('A','C',500)
g.add_edge('A','D',300)
g.add_edge('B','C',350)
g.add_edge('C','D',306)
g.add_edge('C','F',330)
g.add_edge('D','F',200)
g.add_edge('D','A',100)


vertex = g.get_vertex('A')
display_bfs(vertex)

# COMMAND ----------

def find_all_reachable_node(vertex):
  visited = set()
  q = Queue()
  q.enqueue(vertex)
  visited.add(vertex)
  while not q.isEmpty():
    current = q.dequeue()
    for dest in current.get_neighbours():
      if dest not in visited:
        visited.add(dest)
        q.enqueue(dest)
  
  return visited

# COMMAND ----------

key = 'A'
vertex = g.get_vertex(key)
reachable = find_all_reachable_node(vertex)
print('All nodes reachable from {}:'.format(key),[v.get_key() for v in reachable])

# COMMAND ----------



# COMMAND ----------

def label_all_reachable(vertex,component,label):
  visited = set()
  q = Queue()
  q.enqueue(vertex)
  visited.add(vertex)
  
  while not q.isEmpty():
    current = q.dequeue()
    component[current] = label
    for dest in current.get_neighbours():
      if dest not in visited:
        visited.add(dest)
        q.enqueue(dest)
    
  

# COMMAND ----------

g= Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A','B',300)
g.add_edge('A','C',500)
g.add_edge('A','D',300)
g.add_edge('B','C',350)
g.add_edge('C','D',306)
g.add_edge('C','F',330)
g.add_edge('D','F',200)
g.add_edge('D','A',100)



# COMMAND ----------

component = dict.fromkeys(g, None)
label = 1

for v in g:
    if component[v] is None:
        label_all_reachable(v, component, label)
        label += 1

max_label = label
for label in range(1, max_label):
    component_vertices = [v.get_key() for v in component
                          if component[v] == label]
    print('Component {}:'.format(label), component_vertices)
 
 

# COMMAND ----------

# MAGIC %md ###Python Program to Find Shortest Path From a Vertex using BFS in an Unweighted Graph

# COMMAND ----------

def find_shortest_paths(src):
    """Returns tuple of two dictionaries: (parent, distance)
 
    parent contains vertices mapped to their parent vertex in the shortest
    path from src to that vertex.
    distance contains vertices mapped to their shortest distance from src.
    """
    parent = {src: None}
    distance = {src: 0}
 
    visited = set()
    q = Queue()
    q.enqueue(src)
    visited.add(src)
    while not q.isEmpty():
        current = q.dequeue()
        for dest in current.get_neighbours():
            if dest not in visited:
                visited.add(dest)
                parent[dest] = current
                distance[dest] = distance[current] + 1
                q.enqueue(dest)
    return (parent, distance)

# COMMAND ----------

g= Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A','B',300)
g.add_edge('A','C',500)
g.add_edge('A','D',300)
g.add_edge('B','C',350)
g.add_edge('C','D',306)
g.add_edge('C','F',330)
g.add_edge('D','F',200)
g.add_edge('D','A',100)



# COMMAND ----------


key = "A"
src = g.get_vertex(key)
parent, distance = find_shortest_paths(src)

print('Path from destination vertices to source vertex {}:'.format(key))
for v in parent:
    print('Vertex {} (distance {}): '.format(v.get_key(), distance[v]),
          end='')
    while parent[v] is not None:
        print(v.get_key(), end = ' ')
        v = parent[v]
    print(src.get_key()) # print source vertex

# COMMAND ----------

# MAGIC %md ###Python Program to Find if Undirected Graph contains Cycle using BFS

# COMMAND ----------

def is_cycle_present(vertex,visited):
  parent = {vertex:None}
  q=Queue()
  q.enqueue(vertex)
  visited.add(vertex)
  while not q.isEmpty():
    current = q.dequeue()
    for dest in current.get_neighbours():
      if dest not in visited:
        visited.add(dest)
        parent[dest] = current
        q.enqueue(dest)
      else:
        print("parent current",parent[current].get_key())
        print("dest",dest.get_key())
        if parent[current] is not  dest:
          return True
        
  return False      
  

# COMMAND ----------

g= Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A','B',300)
g.add_edge('B','C',500)
g.add_edge('C','D',300)
g.add_edge('D','F',350)
g.add_edge('F','E',306)



# COMMAND ----------

present = False
visited = set()
for v in g:
    if v not in visited:
        if is_cycle_present(v,visited):
            present = True
            break

if present:
    print('Cycle present.')
else:
    print('Cycle not present.')

# COMMAND ----------

# MAGIC %md ###Python Program to Find if Undirected Graph is Bipartite using BFS

# COMMAND ----------

def is_bipartite(vertex,visited):
  color = {vertex:0}
  q = Queue()
  q.enqueue(vertex)
  visited.add(vertex)
  while not q.isEmpty():
    current = q.dequeue()
    next_color = 1 - color[current]
    for dest in current.get_neighbours():
      if dest not in visited:
        print("dest",dest.get_key(),"__",next_color)
        visited.add(dest)
        color[dest] = next_color
        q.enqueue(dest)
      else:
        print("current ",current.get_key(),"Cureent Value ",color[current],"dest ",dest.get_key(),"next",next_color)
        if color[current] != next_color:
          return False
  return True

# COMMAND ----------

g= Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A','B',300)
g.add_edge('B','C',500)
g.add_edge('C','D',300)
g.add_edge('D','F',350)
g.add_edge('E','A',306)



# COMMAND ----------

bipartite = True
visited = set()
for v in g:
  if v not in visited:
    print("Ourside",v.get_key())
    if not is_bipartite(v,visited):
      bipartite = False
      break
      
      
if bipartite:
  print("Graph is bipartite.")
else:
  print("Graph is not bipartite.")
      
      
