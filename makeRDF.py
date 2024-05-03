import csv

with open('nodes.csv', newline='') as f:
    reader = csv.reader(f)
    nodes = list(reader)

with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edges = list(reader)

print('<?xml version="1.0"?>')
print('<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/metadata/dublin_core#">') 

for index, node in enumerate(nodes):
  if index > 0:
    node_id = node[1]
    print('  <rdf:Description rdf:about="'+node[4]+'">')
    print('    <dc:title>'+node[3]+'</dc:title>')
    for edge in edges:
      if edge[2] == node_id:
        print('    <dc:relation rdf:resource="https://digitalzibaldone.net/'+edge[3]+'/'+edge[4]+'" />')
    print('  </rdf:Description>')
print('</rdf:RDF>')
