import os
from gensim.models import Word2Vec
import multiprocessing as mp
import random

def generate_embeddings(ego_nodes, ndims = 128, window_size = 10):
    """
    generate_embeddings(ego_nodes, ndims, window_size, directory) generates vector embeddings for all the nodes in the network
    It uses a similar method as node2vec for generating embeddings from the fairwalk traces.
    It takes list of ego nodes as argument.
    Additionally, it takes the dimensions for embeddings and window size for the ngram model as arguments.
    It saves embeddings for all the nodes for each instance of all the ego networks in the directory ../Embeddings/
    It also saves the respective word2vec models trained in the directory ../Embeddings_Model/
    """

    try:
        os.mkdir('../Embeddings')
    except:
        pass

    try:
        os.mkdir('../Embeddings_Model/')
    except:
        pass

    for ego_node in ego_nodes:
        for i in range(5):
            file = open('../Fairwalks/fairwalks_{}_{}.txt'.format(ego_node, i), 'r')
            walks = []
            lines = file.readlines()
            for line in lines:
                if len(line) == 0:
                    continue
                walk = [element for element in line.strip().split()]
                walks.append(walk)
            random.shuffle(walks)
            model = Word2Vec(walks, size = 128, window = 10, min_count = 10, sg = 1, workers = mp.cpu_count())
            model.wv.save_word2vec_format('../Embeddings/embeddings_{}_{}.emb'.format(ego_node, i))
            model.wv.save('../Embeddings_Model/embeddings_model_{}_{}.model'.format(ego_node, i))
            file.close()