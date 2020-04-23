import os
from gensim.models import Word2Vec
import multiprocessing as mp

def generate_embeddings(ego_nodes, fair_walks, nodes, ndims = 128, window_size = 10, directory = '../Embeddings'):
    """
    generate_embeddings(ego_nodes, fair_walks, nodes, ndims, window_size, directory) generates vector embeddings for all the nodes in the network
    It uses a similar method as node2vec for generating embeddings from the fairwalk traces.
    It takes list of ego nodes, dictionary of fairwalk traces, a dictionary of nodes corresponding to each ego node as arguments
    Additionally, it takes the dimensions for embeddings and window size for the ngram model and directory for output file as arguments
    It returns path for directory containing the files having generated embeddings
    """
    num_walks = len(fair_walks[ego_nodes[0]][0])

    all_walks = {}
    for ego_node in ego_nodes:
        all_walk = [[] for walk in range(num_walks)]
        for walk in range(num_walks):
            all_walk[walk].append(fair_walks[ego_node][ego_node][walk])
            for node in nodes[ego_node]:
                all_walk[walk].append(fair_walks[ego_node][node][walk])
        all_walks[ego_node] = all_walk

    all_walks_2 = {}
    for ego_node in ego_nodes:
        all_walk_2 = []
        for all_walk in all_walks[ego_node]:
            walk = [str(element) for element in all_walk[0]]
            walk_reversed = walk[::-1]
            all_walk_2.append(walk)
            all_walk_2.append(walk_reversed)
            for i in range(len(nodes[ego_node])):
                walk = [str(element) for element in all_walk[i + 1]]
                walk_reversed = walk[::-1]
                all_walk_2.append(walk)
                all_walk_2.append(walk_reversed)
        all_walks_2[ego_node] = all_walk_2

    try:
        os.mkdir(directory)
    except:
        pass

    if directory[-1] != '/':
        directory = directory + '/'

    for ego_node in ego_nodes:
        print(ego_node)
        model = Word2Vec(all_walks_2[ego_node], size = 128, window = 10, min_count = 0, sg = 1, workers = mp.cpu_count(), iter = 1)
        model.wv.save_word2vec_format(directory + str(ego_node) + '.emb')

    return directory

if __name__ == '__main__':
    from adjacency_list import generate_adjacency_list
    from feature_extraction import generate_features
    from gender_mapping import map_nodes_gender
    from fairwalk import generate_fairwalks
    nodes, adjacency_lists, ego_nodes = generate_adjacency_list()
    features, gender_featnum = generate_features(ego_nodes)
    gender_1, gender_2, gender_wise_adjacency_lists = map_nodes_gender(nodes, adjacency_lists, ego_nodes, gender_featnum, features)
    fair_walks = generate_fairwalks(ego_nodes, nodes, gender_wise_adjacency_lists)
    directory = generate_embeddings(ego_nodes, fair_walks, nodes)
    file = open(directory + str(ego_nodes[0]) + '.emb', 'r')
    for i in range(5):
        print(file.readline())