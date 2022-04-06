#!/usr/bin/env python
# coding: utf-8

# In[1]:


graph = {
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Zerind': {'Arad': 75,'Oradea': 71},
    'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
    'Timisoara': {'Arad': 118, 'Lugos': 111},
    'Lugos': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Drobeta': 75, 'Lugos': 70},
    'Drobeta': {'Craiova': 120, 'Mehadia':75},
    'Sibiu': {'RimnicuVilcea': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'RimnicuVilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Pitesti': {'Craiova': 138, 'Bucarest': 101,'RimnicuVilcea': 97},
    'Fagaras': {'Bucarest': 211,'Sibiu':99},
    'Bucarest': {'Giurgiu': 90, 'Urziceni': 85, 'Pitesti': 101, 'Fagaras': 211},
    'Urziceni': {'Vaslui': 142, 'Hirsova': 98, 'Bucarest': 85},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Neamt': {'Iasi':87}
}

path = list()


def DFS(currentNode, destination, graph, maxDepth, curList):
    print("Checking for destination", currentNode)
    curList.append(currentNode)
    if currentNode == destination:
        return True
    if maxDepth <= 0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth - 1, curList):
            return True
        else:
            curList.pop()
    return False


def iterativeDDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode, destination, graph, i, curList):
            return True
    return False

if iterativeDDFS('Arad', 'Bucarest', graph, 17):
    print(".......................................................")
    print(path.pop())
    print("Goal Path exists")
    print(".......................................................")

else:
    print(".......................................................")
    print("Goal Path is not available")
    print(".......................................................")


# In[ ]:




