import csv

with open('nodes.csv', newline='') as f:
    reader = csv.reader(f)
    nodes = list(reader)
    
with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edges = list(reader)   
    
print('<?xml version="1.0" encoding="UTF-8"?>')
print('<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">')
print('<key id="d0" for="node" attr.name="color" attr.type="string">')
print('<default>yellow</default>')
print('</key>')
print('<key id="d1" for="edge" attr.name="weight" attr.type="double"/>')
print('<graph id="G" edgedefault="undirected">')


for index, node in enumerate(nodes):
  if index > 0:

    node_id = node[1]
    node_type = node[2]
    print('  <node id="'+node_id+'">')
    print('     <data key="type">'+node_type+'</data>')
    print('  </node>')


for index, edge in enumerate(edges):
  if index > 0:
    source = edge[2]
    target = edge[4]
    print('  <edge source="'+source+'" target="'+target+'"></edge>')

print('</graph>')
print('</graphml>')
