def generate_features(ego_nodes, dataset_directory = '../Dataset/facebook/'):
    """
    generate_features(ego_nodes, dataset_directory) generates a list of feature numbers for all the ego nodes in the network
    It also finds the feature number for the sensitive attribute - gender
    It takes list of ego nodes and dataset directory as arguments
    It returns a dictionary features and a list gender_featnum, which tell list of feature numbers for ego nodes and feature numbers for genders respectively
    It scrapes .featnames files for all the ego nodes for this purpose
    """

    if dataset_directory[-1] != '/':
        dataset_directory = dataset_directory + '/'

    features = {}
    gender_featnum = []
    for ego_node in ego_nodes:
        featnames = open(dataset_directory + str(ego_node) + '.featnames')
        features_node = []
        for line in featnames:
            features_node.append(int(line.split(';')[-1].split()[-1]))
            if line.split(';')[0].split()[1] == 'gender':
                if int(line.split(';')[-1].split()[-1]) not in gender_featnum:
                    gender_featnum.append(int(line.split(';')[-1].split()[-1]))
        features[ego_node] = features_node
        featnames.close()
    gender_featnum.sort()
    return features, gender_featnum