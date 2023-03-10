
total_vertex = int(input("Enter no of vertex: "))
graph = {}  # dictionary
flag = True  # true initial value
# visited and queue are list
visited=[]
queue=[]

def BFS(graph,temp):     #root node=temp
    queue.append(temp)
    visited.append(temp)

    while queue:    #loop cholbe queue emty na hya pojonto
        #print krar age pop krte hbe left element so (0)
        node = queue.pop(0)
        print(node,end=' ')
        #child gula graph a store kra ache,sekhan theke access krte hbe
        # child gula visited and queue modde rekhe dilam and agula age theke thakle r insert dorker nei tai loop chalabo
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)


for i in range(total_vertex):
    vertex = input("Enter vertex: ")  # input vertex as a key
    graph[vertex] = list()  # insert to vertex as a key in dictionary,,list means input only key value
    while flag:
        child = input(
            f'Enter child of {vertex} (-1 for exist): ')  # input child value,there are no child if given -1 as a input
        if child != '-1':  # if child not equal -1 then append adjacency under that vertex
            graph[vertex].append(child)
        else:
            flag = False  # if given -1,so there are no child,then come out from loop
    flag = True  # for next loop so true flag
print(graph)
BFS(graph,'A')