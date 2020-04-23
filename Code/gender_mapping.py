def map_nodes_gender(nodes, adjacency_lists, ego_nodes, gender_featnum, features, dataset_directory = '../Dataset/facebook/'):
    """
    map_nodes_gender(nodes, adjacency_lists, ego_nodes, gender_featnum, features, dataset_directory) maps all the nodes in the network to their respective gender
    It takes dictionary of nodes, dictionary of adjacency lists, list of ego nodes, list of gender feature numbers, dictionary of features of ego nodes and dataset directory as arguments.
    It returns dictionaries gender_1, gender_2, which tells whether a node has positive for gender_1, gender_2.
    It also returns a gender wise adjacency list for all the nodes in the network.
    It scrapes .egofeat and .feat files for all the ego nodes for this purpose.
    """

    if dataset_directory[-1] != '/':
        dataset_directory = dataset_directory + '/'

    gender_1 = {}
    gender_2 = {}
    for ego_node in ego_nodes:
        egofeat = open(dataset_directory + str(ego_node) + '.egofeat')
        feat = open(dataset_directory + str(ego_node) + '.feat')
        index_gender_1 = features[ego_node].index(gender_featnum[0])
        index_gender_2 = features[ego_node].index(gender_featnum[1])

        for line in egofeat:
            if int(line.split()[index_gender_1]) == 1:
                gender_1[ego_node] = 1
            else:
                gender_1[ego_node] = 0
            if int(line.split()[index_gender_2]) == 1:
                gender_2[ego_node] = 1
            else:
                gender_2[ego_node] = 0

        for line in feat:
            if int(line.split()[index_gender_1 + 1]) == 1:
                gender_1[int(line.split()[0])] = 1
            else:
                gender_1[int(line.split()[0])] = 0
            if int(line.split()[index_gender_2 + 1]) == 1:
                gender_2[int(line.split()[0])] = 1
            else:
                gender_2[int(line.split()[0])] = 0

        egofeat.close()
        feat.close()

    gender_wise_adjacency_lists = {}
    for ego_node in ego_nodes:
        gender_wise_adjacency_list = {}
        for node in adjacency_lists[ego_node].keys():
            gender_wise_adjacency_list[node] = []
            gender_1_list = [n for n in adjacency_lists[ego_node][node] if gender_1[n] == 1]
            gender_2_list = [n for n in adjacency_lists[ego_node][node] if gender_2[n] == 1]
            gender_3_list = [n for n in adjacency_lists[ego_node][node] if (gender_1[n] == 0 and gender_2[n] == 0)]
            gender_wise_adjacency_list[node].append(gender_1_list)
            gender_wise_adjacency_list[node].append(gender_2_list)
            gender_wise_adjacency_list[node].append(gender_3_list)
        gender_wise_adjacency_lists[ego_node] = gender_wise_adjacency_list

    return gender_1, gender_2, gender_wise_adjacency_lists

if __name__ == '__main__':
    from adjacency_list import generate_adjacency_list
    from feature_extraction import generate_features
    nodes, adjacency_lists, ego_nodes = generate_adjacency_list()
    features, gender_featnum = generate_features(ego_nodes)
    gender_1, gender_2, gender_wise_adjacency_lists = map_nodes_gender(nodes, adjacency_lists, ego_nodes, gender_featnum, features)
    print(gender_1)
    print(gender_2)
    print(gender_wise_adjacency_lists[0])