from adjacency_list import generate_adjacency_list
from feature_extraction import generate_features
from gender_mapping import map_nodes_gender
from fairwalk import generate_fairwalks

if __name__ == '__main__':
    dataset_directory = "../Dataset/facebook/"
    nodes, adjacency_list, ego_nodes = generate_adjacency_list(dataset_directory)
    features, gender_featnum = generate_features(ego_nodes, dataset_directory)
    gender_1, gender_2, gender_wise_adjacency_list = map_nodes_gender(nodes, adjacency_list, ego_nodes, gender_featnum, features, dataset_directory)
    
    num_walks = 20
    walk_len = 80
    fair_walks = generate_fairwalks(nodes, gender_wise_adjacency_list, num_walks, walk_len)
    print(fair_walks[0])