from adjacency_list import generate_adjacency_list
from feature_extraction import generate_features
from gender_mapping import map_nodes_gender

if __name__ == '__main__':
    dataset_directory = "../Dataset/facebook/"

    adjacency_list, ego_nodes = generate_adjacency_list(dataset_directory)
    features, gender_featnum = generate_features(ego_nodes, dataset_directory)
    gender_1, gender_2 = map_nodes_gender(ego_nodes, gender_featnum, features, dataset_directory)
    print(gender_1)
    print(gender_2)