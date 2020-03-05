from adjacency_list import generate_adjacency_list

if __name__ == '__main__':
    dataset_directory = "../Dataset/facebook/"
    adjacency_list = generate_adjacency_list(dataset_directory)
    print(adjacency_list)