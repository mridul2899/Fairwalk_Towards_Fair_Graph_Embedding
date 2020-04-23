import os

def generate_adjacency_list(dataset_directory = "../Dataset/facebook/"):
    """
    generate_adjacency_list(dataset_directory) generates adjacency list for all the nodes in the network
    It takes path to dataset as the argument
    It returns dictionary of all the nodes for each ego-network, dictionary having adjacency lists for all nodes in all the ego-networks and list of ego nodes
    It scrapes .circles and .edges files for all the ego nodes for this purpose
    """

    if dataset_directory[-1] != '/':
        dataset_directory = dataset_directory + '/'

    all_files = os.listdir(dataset_directory)
    egofeat_files = [file for file in all_files if (file.split('.')[1] == 'egofeat')]
    ego_nodes = [int(file.split('.')[0]) for file in egofeat_files]

    nodes = {}
    for ego_node in ego_nodes:
        nodes[ego_node] = set()
        circles = open(dataset_directory + str(ego_node) + '.circles', 'r')
        for line in circles:
            line = line.split()
            for n in line[1:]:
                nodes[ego_node].add(int(n))
        circles.close()

        edges = open(dataset_directory + str(ego_node) + '.edges', 'r')
        for line in edges:
            line = line.split()
            for n in line:
                nodes[ego_node].add(int(n))
        edges.close()

    adjacency_lists = {}
    for ego_node in ego_nodes:
        adjacency_list = {}
        adjacency_list[ego_node] = set()

        circles = open(dataset_directory + str(ego_node) + '.circles', 'r')
        for line in circles:
            line = line.split()
            for n in line[1:]:
                if int(n) not in adjacency_list.keys():
                    adjacency_list[int(n)] = set()
                adjacency_list[ego_node].add(int(n))
                adjacency_list[int(n)].add(ego_node)
        circles.close()

        edges = open(dataset_directory + str(ego_node) + '.edges', 'r')
        for line in edges:
            line = line.split()
            one = int(line[0])
            two = int(line[1])
            if one not in adjacency_list.keys():
                adjacency_list[one] = set()
            if two not in adjacency_list.keys():
                adjacency_list[two] = set()
            adjacency_list[one].add(two)
            adjacency_list[two].add(one)
        edges.close()

        adjacency_lists[ego_node] = adjacency_list

    return nodes, adjacency_lists, ego_nodes

if __name__ == '__main__':
    nodes, adjacency_lists, ego_nodes = generate_adjacency_list()
    print(adjacency_lists[0])
    print(ego_nodes)