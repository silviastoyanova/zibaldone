import csv, sys

if len(sys.argv) > 1:
  myinput = sys.argv[1]
else:
  myinput = "2,1"
  

node_id = ""
nodesLookup = {}
nodes = []
edges = []
mynodes = []
myedges = []


def getEdges(node_id):
  neighbors = []
  for index, e in enumerate(edges):
    if index > 0:
      if e[2] == node_id:
        neighbors.append(e)
  for index, e in enumerate(edges):
    if index > 0:
      if e[4] == node_id:
        neighbors.append(e)
  return neighbors


def colors(node_type):
    if node_type == "paragraph":
        return '<viz:color r="29" g="168" b="29"></viz:color>'
    elif node_type == "theme":
        return '<viz:color r="29" g="29" b="168"></viz:color>'
    elif node_type == "person":
        return '<viz:color r="168" g="29" b="29"></viz:color>'
    elif node_type == "place":
        return '<viz:color r="29" g="168" b="29"></viz:color>'
    elif node_type == "bibl":
        return '<viz:color r="168" g="29" b="168"></viz:color>'
    return '<viz:color r="0" g="0" b="0"></viz:color>'
 
#************************************************       
        

with open('nodes.csv', newline='') as f:
    reader = csv.reader(f)
    nodes = list(reader)
    
# make a dictionary of the nodes

for index, n in enumerate(nodes):
  if index > 0:
    nodesLookup[n[1]] = n 
  if n[3] == myinput:
    node_id = n[1]   
    
    
with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edges = list(reader)


generations = {}


mynodes.append(node_id)
  

# get neighbors of root node
generations[0] = getEdges(node_id)


for gen in range(1,1):
  generations[gen] = []
  for x in generations[gen-1]:
    if x[2] == node_id:
      generations[gen] += getEdges(x[4])
    else:
      generations[gen] += getEdges(x[2])


for x in generations:
  for y in generations[x]:
    myedges.append({"source": y[2], "target": y[4]})
    if(y[2] != node_id):
      mynodes.append(y[2])
    if(y[4] != node_id):
      mynodes.append(y[4])  

mynodes = set(mynodes)


print('<?xml version="1.0" encoding="UTF-8"?>')
print('<gexf xmlns="http://www.gexf.net/1.1draft" version="1.1" xmlns:viz="http://www.gexf.net/1.1draft/viz" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.1draft http://www.gexf.net/1.1draft/gexf.xsd">')
print('<graph defaultedgetype="undirected" timeformat="double" mode="dynamic">')

print('<nodes>')

for z in mynodes:
  n = nodesLookup[z]
  print('  <node id="'+z+'" label="'+n[3]+'">')
  print('    <attvalues>')
  print('      <attvalue for="type" value="'+n[2]+'"></attvalue>')
  print('      <attvalue for="uri" value="'+n[4]+'"></attvalue>')
  print('    </attvalues>')
  print('    <viz:size value="160"></viz:size>') 
  print('    '+colors(n[2]))
  print('  </node>')

print('</nodes>')
print('<edges>')

for z in myedges:
  print('  <edge source="'+z['source']+'" target="'+z['target']+'">')
  print('    <viz:color r="200" g="200" b="200"></viz:color>')
  print('  </edge>')

print('    </edges>')
print('  </graph>')
print('</gexf>')
  
  
