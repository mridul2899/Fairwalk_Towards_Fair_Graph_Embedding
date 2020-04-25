from adjacency_list import generate_adjacency_list
from feature_extraction import generate_features
from gender_mapping import map_nodes_gender
from fairwalk import generate_fairwalks
from generate_embeddings import generate_embeddings
from find_similar_non_friends import find_similar_non_friends
from map_similar_nodes import map_similar_nodes
from not_connected_samples import find_not_connected_samples

# from hadamard_vectors import generate_hadamard_vectors

if __name__ == '__main__':
    dataset_directory = "../Dataset/facebook/"
    ego_nodes = generate_adjacency_list(dataset_directory)

    features, gender_featnum = generate_features(ego_nodes, dataset_directory)

    map_nodes_gender(ego_nodes, gender_featnum, features, dataset_directory)

    num_walks = 20
    walk_len = 80
    generate_fairwalks(ego_nodes, num_walks, walk_len)

    ndims = 128
    window_size = 10
    generate_embeddings(ego_nodes, ndims, window_size)

    find_similar_non_friends(ego_nodes)

    map_similar_nodes(ego_nodes)

    find_not_connected_samples(ego_nodes)

    # directory = generate_hadamard_vectors(ego_nodes)


    # file = open(directory + 'hadamard_' + str(ego_nodes[0]) + '.txt', 'r')
    # for i in range(5):
    #     print(file.readline())