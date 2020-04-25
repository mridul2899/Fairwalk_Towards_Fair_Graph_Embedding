import os
import random

def find_not_connected_samples(ego_nodes):
    """
    find_not_connected_samples(ego_nodes) finds non-friend nodes as per complete edge data (both training and testing combined) for all the nodes.
    It takes the list of ego nodes as its argument.
    For each node in the ego network, it tries to find as many not connected nodes as the connected nodes for that node, in the testing (20%) edges data.
    It saves the found not connected nodes in the directory ../Not_Connected_Samples/
    """

    try:
        os.mkdir('../Not_Connected_Samples/')
    except:
        pass

    for ego_node in ego_nodes:
        for i in range(5):
            nodes = set()
            adjacency_list = {}

            file = open('../Edges/edges_20_{}_{}.txt'.format(ego_node, i))
            lines = file.readlines()
            file.close()

            for line in lines:
                if len(lines) == 0:
                    continue
                line = line.strip().split()
                one, two = int(line[0]), int(line[1])
                nodes.add(one)
                nodes.add(two)
                if one not in adjacency_list.keys():
                    adjacency_list[one] = set()
                if two not in adjacency_list.keys():
                    adjacency_list[two] = set()
                adjacency_list[one].add(two)
                adjacency_list[two].add(one)

            counts = {}
            for key in adjacency_list.keys():
                counts[key] = len(adjacency_list[key])

            file = open('../Edges/edges_80_{}_{}.txt'.format(ego_node, i))
            lines = file.readlines()
            file.close()

            for line in lines:
                if len(lines) == 0:
                    continue
                line = line.strip().split()
                one, two = int(line[0]), int(line[1])
                nodes.add(one)
                nodes.add(two)
                if one not in adjacency_list.keys():
                    adjacency_list[one] = set()
                if two not in adjacency_list.keys():
                    adjacency_list[two] = set()
                adjacency_list[one].add(two)
                adjacency_list[two].add(one)

            not_connected = {}
            nodes = list(nodes)
            for j in range(len(nodes)):
                node1 = nodes[j]
                for node2 in nodes[j + 1:]:
                    if node2 in adjacency_list[node1]:
                        continue
                    if node1 not in not_connected.keys():
                        not_connected[node1] = set()
                    if node2 not in not_connected.keys():
                        not_connected[node2] = set()
                    not_connected[node1].add(node2)
                    not_connected[node2].add(node1)

            for node in nodes:
                if node not in counts.keys():
                    counts[node] = 0
                if node not in not_connected.keys():
                    not_connected[node] = set()

            sample = {}
            for node in nodes:
                sample[node] = [node]
                for j in range(min(counts[node], len(not_connected[node]))):
                    node2 = node
                    while node2 in sample[node]:
                        node2 = random.choice(list(not_connected[node]))
                    not_connected[node].remove(node2)
                    sample[node].append(node2)

            file = open('../Not_Connected_Samples/sample_{}_{}.txt'.format(ego_node, i), 'w')
            for node in nodes:
                for element in sample[node]:
                    file.write('{} '.format(element))
                file.write('\n')
            file.close()