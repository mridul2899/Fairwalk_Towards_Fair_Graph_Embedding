import numpy as np

def generate_hadamard_vectors(ego_nodes, directory = '../Embeddings/'):
    """
    generate_hadamard_vectors(ego_nodes) creates hadamard vectors for all the pairs of nodes in each ego network
    It takes a list of ego nodes and location of the directory where the <ego_node>.emb files are located as its arguments.
    It stores the hadamard vectors in files 'hadamard_<ego_node>.txt' in the directory specified, and returns the path to the directory.
    """

    if directory[-1] != '/':
        directory = directory + '/'

    for ego_node in ego_nodes:
        file = open(directory + str(ego_node) + '.emb')
        lines = file.readlines()
        num_nodes, ndims = int(lines[0].strip().split()[0]), int(lines[0].strip().split()[1])

        embeddings = {}
        for line in lines[1:]:
            line = line.strip()
            if len(line) == 0:
                continue
            line = line.split()
            node = int(line[0])
            embeddings[node] = np.asarray([float(element) for element in line[1:]], dtype = np.float32)

        nodes = list(embeddings.keys())
        nodes.sort()

        hadamard_vectors = {}
        for i in range(len(nodes)):
            node1 = nodes[i]
            for node2 in nodes[i + 1:]:
                hadamard_vectors[(node1, node2)] = np.multiply(embeddings[node1], embeddings[node2])

        file2 = open(directory + 'hadamard_' + str(ego_node) + '.txt', 'w')
        for i in range(len(nodes)):
            node1 = nodes[i]
            for node2 in nodes[i + 1:]:
                file2.write(str(node1) + ' ' + str(node2) + ' ')
                string = ''
                for element in hadamard_vectors[(node1, node2)]:
                    string = string + str(element) + ' '
                file2.write(string)
                file2.write('\n')
        file2.close()

    return directory

if __name__ == '__main__':
    from adjacency_list import generate_adjacency_list
    nodes, adjacency_lists, ego_nodes = generate_adjacency_list()
    directory = generate_hadamard_vectors(ego_nodes)

    file = open(directory + 'hadamard_' + str(ego_nodes[0]) + '.txt', 'r')
    for i in range(5):
        print(file.readline())