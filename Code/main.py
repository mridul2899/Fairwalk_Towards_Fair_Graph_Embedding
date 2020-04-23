from adjacency_list import generate_adjacency_list
from feature_extraction import generate_features
from gender_mapping import map_nodes_gender
from fairwalk import generate_fairwalks
from generate_embeddings import generate_embeddings
from hadamard_vectors import generate_hadamard_vectors

if __name__ == '__main__':
    dataset_directory = "../Dataset/facebook/"
    nodes, adjacency_lists, ego_nodes = generate_adjacency_list(dataset_directory)
    features, gender_featnum = generate_features(ego_nodes, dataset_directory)
    gender_1, gender_2, gender_wise_adjacency_lists = map_nodes_gender(nodes, adjacency_lists, ego_nodes, gender_featnum, features, dataset_directory)

    num_walks = 20
    walk_len = 80
    fair_walks = generate_fairwalks(ego_nodes, nodes, gender_wise_adjacency_lists, num_walks, walk_len)

    ndims = 128
    window_size = 10
    directory = '../Embeddings/'
    directory = generate_embeddings(ego_nodes, fair_walks, nodes, ndims, window_size, directory)

    directory = generate_hadamard_vectors(ego_nodes)

    file = open(directory + 'hadamard_' + str(ego_nodes[0]) + '.txt', 'r')
    for i in range(5):
        print(file.readline())