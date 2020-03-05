import os

def generate_adjacency_list(dataset_directory = "../Dataset/facebook/"):
    """
    generate_adjacency_list(dataset_directory) generates adjacency list for all the nodes in the network
    It takes path to dataset as the argument
    It returns a list of all the non-isolated nodes in the network, a 2-D adjacency list for all nodes in the network and a list of ego nodes
    It scrapes .circles and .edges files for all the ego nodes for this purpose
    """
    
    if dataset_directory[-1] != '/':
        dataset_directory = dataset_directory + '/'
    
    all_files = os.listdir(dataset_directory)
    egofeat_files = [file for file in all_files if (file.split('.')[1] == 'egofeat')]
    ego_nodes = [int(file.split('.')[0]) for file in egofeat_files]
    
    ego_nodes.sort()

    nodes = []
    for node in ego_nodes:
        if node not in nodes:
            nodes.append(node)
        circles = open(dataset_directory + str(node) + '.circles', 'r')
        for line in circles:
            line = line.split()
            for n in line[1:]:
                if int(n) not in nodes:
                    nodes.append(int(n))
        circles.close()
        
        edges = open(dataset_directory + str(node) + '.edges', 'r')
        for line in edges:
            line = line.split()
            for n in line:
                if int(n) not in nodes:
                    nodes.append(int(n))
        edges.close()

    adjacency_list = [[] for i in range(max(nodes) + 1)]
    for node in ego_nodes:
        circles = open(dataset_directory + str(node) + '.circles', 'r')
        for line in circles:
            line = line.split()
            for n in line[1:]:
                if int(n) not in adjacency_list[node]:
                    adjacency_list[node].append(int(n))
                    adjacency_list[int(n)].append(node)
        circles.close()

        edges = open(dataset_directory + str(node) + '.edges', 'r')
        for line in edges:
            line = line.split()
            one = int(line[0])
            two = int(line[1])
            if two not in adjacency_list[one]:
                adjacency_list[one].append(two)
                adjacency_list[two].append(one)
        edges.close()
    
    for node in nodes:
        adjacency_list[node].sort()
    
    return nodes, adjacency_list, ego_nodes

if __name__ == '__main__':
    nodes, adjacency_list, ego_nodes = generate_adjacency_list()
    print(adjacency_list)
    print(ego_nodes)