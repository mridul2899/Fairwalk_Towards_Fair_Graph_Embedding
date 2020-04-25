import os
import random

def generate_adjacency_list(dataset_directory = "../Dataset/facebook/"):
    """
    generate_adjacency_list(dataset_directory) generates adjacencys list for all the nodes in all the ego networks.
    It takes path to dataset as the argument.
    The edges are extracted and split into 80% and 20%, five times for each ego-network, and saved in ../Edges directory.
    The training edges (80%) are then used to form adjacency lists for all the nodes in the training edges file.
    These adjacency lists are saved in ../Adjacency_Lists directory.
    It returns the list of ego nodes.
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

    edges_list = {}
    for ego_node in ego_nodes:
        edge_list = set()

        circles = open(dataset_directory + str(ego_node) + '.circles', 'r')
        for line in circles:
            line = line.split()
            for n in line[1:]:
                edge_list.add((min(ego_node, int(n)), max(ego_node, int(n))))
        circles.close()

        edges = open(dataset_directory + str(ego_node) + '.edges', 'r')
        for line in edges:
            line = line.split()
            one = int(line[0])
            two = int(line[1])
            edge_list.add((min(one, two), max(one, two)))
        edges.close()
        edges_list[ego_node] = edge_list

    try:
        os.mkdir('../Edges/')
    except:
        pass

    for ego_node in ego_nodes:
        edges = list(edges_list[ego_node])
        random.shuffle(edges)
        size = len(edges)
        for i in range(5):
            edges_20 = edges[i * (size // 5):(i + 1) * (size // 5)]
            edges_80 = edges[:i * (size // 5)] + edges[(i + 1) * (size // 5):]

            file = open('../Edges/edges_20_{}_{}.txt'.format(ego_node, i), 'w')
            for edge in edges_20:
                file.write('{} {}\n'.format(edge[0], edge[1]))
            file.close()

            file = open('../Edges/edges_80_{}_{}.txt'.format(ego_node, i), 'w')
            for edge in edges_80:
                file.write('{} {}\n'.format(edge[0], edge[1]))
            file.close()

    try:
        os.mkdir('../Adjacency_Lists/')
    except:
        pass

    for ego_node in ego_nodes:
        for i in range(5):
            file = open('../Edges/edges_80_{}_{}.txt'.format(ego_node, i), 'r')
            adjacency_list = {}
            for line in file:
                if len(line) == 0:
                    continue
                line = line.split()
                node1, node2 = int(line[0]), int(line[1])
                if node1 not in adjacency_list.keys():
                    adjacency_list[node1] = set()
                if node2 not in adjacency_list.keys():
                    adjacency_list[node2] = set()
                adjacency_list[node1].add(node2)
                adjacency_list[node2].add(node1)
            file.close()
            keys = list(adjacency_list.keys())
            keys.sort()

            file = open('../Adjacency_Lists/adjacency_list_{}_{}.txt'.format(ego_node, i), 'w')
            for key in keys:
                file.write('{}'.format(key))
                for node in adjacency_list[key]:
                    file.write(' {}'.format(node))
                file.write('\n')
            file.close()

    return ego_nodes