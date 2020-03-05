def map_nodes_gender(ego_nodes, gender_featnum, features, dataset_directory = '../Dataset/facebook/'):
    """
    map_nodes_gender(ego_nodes, gender_featnum, features, dataset_directory) maps all the nodes in the network to their respective gender
    It takes list of ego nodes, list of gender feature numbers, dictionary of features of ego nodes and dataset directory as arguments
    It returns dictionaries gender_1 and gender_2, which tells whether a node has positive for gender_1, gender_2
    It scrapes .egofeat and .feat files for all the ego nodes for this purpose
    """

    if dataset_directory[-1] != '/':
        dataset_directory = dataset_directory + '/'

    gender_1 = {}
    gender_2 = {}

    for node in ego_nodes:
        egofeat = open(dataset_directory + str(node) + '.egofeat')
        feat = open(dataset_directory + str(node) + '.feat')
        
        index_gender_1 = features[node].index(gender_featnum[0])
        index_gender_2 = features[node].index(gender_featnum[1])
        
        for line in egofeat:
            if int(line.split()[index_gender_1]) == 1:
                gender_1[node] = 1
            else:
                gender_1[node] = 0
            if int(line.split()[index_gender_2]) == 1:
                gender_2[node] = 1
            else:
                gender_2[node] = 0
        
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
    
    return gender_1, gender_2

if __name__ == '__main__':
    from adjacency_list import generate_adjacency_list
    from feature_extraction import generate_features
    adjacency_list, ego_nodes = generate_adjacency_list()
    features, gender_featnum = generate_features(ego_nodes)
    gender_1, gender_2 = map_nodes_gender(ego_nodes, gender_featnum, features)
    print(gender_1)
    print(gender_2)