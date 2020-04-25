import os

def map_nodes_gender(ego_nodes, gender_featnum, features, dataset_directory = '../Dataset/facebook/'):
    """
    map_nodes_gender(ego_nodes, gender_featnum, features, dataset_directory) maps all the nodes in the network to their respective gender
    It takes list of ego nodes, list of gender feature numbers, dictionary of features of ego nodes and dataset directory as arguments.
    It saves gender wise adjacency list for all the nodes for each instance of all ego networks in ../Gender_Adjacency_Lists/
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

    try:
        os.mkdir('../Gender_Adjacency_Lists/')
    except:
        pass

    for ego_node in ego_nodes:
        for i in range(5):
            gender_wise_adjacency_list = {}
            file = open('../Adjacency_Lists/adjacency_list_{}_{}.txt'.format(ego_node, i), 'r')
            for line in file:
                if len(line) == 0:
                    continue
                line = line.split()
                gender_wise_adjacency_list[int(line[0])] = []
                gender_1_list = [int(n) for n in line[1:] if gender_1[int(n)] == 1]
                gender_2_list = [int(n) for n in line[1:] if gender_2[int(n)] == 1]
                gender_3_list = [int(n) for n in line[1:] if (gender_1[int(n)] == 0 and gender_2[int(n)] == 0)]
                gender_wise_adjacency_list[int(line[0])].append(gender_1_list)
                gender_wise_adjacency_list[int(line[0])].append(gender_2_list)
                gender_wise_adjacency_list[int(line[0])].append(gender_3_list)
            file.close()
            keys = list(gender_wise_adjacency_list.keys())
            keys.sort()
            file = open('../Gender_Adjacency_Lists/gender_wise_adjacency_list_{}_{}.txt'.format(ego_node, i), 'w')
            for key in keys:
                file.write('{}\n'.format(key))
                for elements in gender_wise_adjacency_list[key]:
                    line = ''
                    for element in elements:
                        line = line + str(element) + ' '
                    file.write(line.strip() + '\n')
            file.close()