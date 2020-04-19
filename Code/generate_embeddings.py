import os
from gensim.models import Word2Vec
import multiprocessing as mp

def generate_embeddings(fair_walks, nodes, ndims = 128, window_size = 10, directory = '../Embeddings'):
    """
    generate_embeddings(fair_walks, nodes, ndims, window_size, directory) generates vector embeddings for all the nodes in the network
    It uses a similar method as node2vec for generating embeddings from the fairwalk traces
    It takes dictionary of fairwalk traces, a list of non-isolated nodes as arguments
    Additionally, it takes the dimensions for embeddings and window size for the ngram model and directory for output file as arguments
    It returns path for the file containing generated embeddings
    """
    num_walks = len(fair_walks[nodes[0]])

    all_walks = [[] for walk in range(num_walks)]
    for walk in range(num_walks):
        for node in nodes:
            all_walks[walk].append(fair_walks[node][walk])

    walks = []
    for all_walk in all_walks:
        for node in range(len(nodes)):
            walk = [str(element) for element in all_walk[node]]
            walk_reversed = walk[::-1]
            walks.append(walk)
            walks.append(walk_reversed)


    model = Word2Vec(walks, size = ndims, window = window_size, min_count = 0, sg = 1, workers = mp.cpu_count(), iter = 1)

    try:
        os.mkdir(directory)
    except:
        pass

    filename = 'generated.emb'
    if directory[-1] != '/':
        path = directory + '/' + filename
    else:
        path = directory + filename

    model.wv.save_word2vec_format(path)

    return path

if __name__ == '__main__':
    from adjacency_list import generate_adjacency_list
    from feature_extraction import generate_features
    from gender_mapping import map_nodes_gender
    from fairwalk import generate_fairwalks
    nodes, adjacency_list, ego_nodes = generate_adjacency_list()
    features, gender_featnum = generate_features(ego_nodes)
    gender_1, gender_2, gender_wise_adjacency_list = map_nodes_gender(nodes, adjacency_list, ego_nodes, gender_featnum, features)
    fair_walks = generate_fairwalks(nodes, gender_wise_adjacency_list)
    path = generate_embeddings(fair_walks, nodes)
    file = open(path, 'r')
    for i in range(5):
        print(file.readline())