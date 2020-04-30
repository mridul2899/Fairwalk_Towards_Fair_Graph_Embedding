Implementation of **[Fairwalk: Towards Fair Graph Embedding](https://www.ijcai.org/Proceedings/2019/456)**

# Fairwalk_Towards_Fair_Graph_Embedding
This implementation has been done as a part of the Term Project for the course CS60016 - AI and Ethics, taught by Professor Animesh Mukherjee at IIT Kharagpur in Spring Semester 2020.

# Summary
In this project, I have tried to generate Fairwalk embeddings for nodes in Facebook ego-networks. <br>
The [Social Circles: Facebook](http://snap.stanford.edu/data/ego-Facebook.html) ego-networks dataset has been taken from [Stanford Network Analysis Project(SNAP)](http://snap.stanford.edu/index.html). <br>
Fairwalks are done on nodes instead of regular random walks. Embeddings are generated from the traces obtained, just in the way [node2vec](https://arxiv.org/abs/1607.00653) accomplishes that. <br>
From these embeddings, we are supposed to predict friendship recommendations for Facebook users.

# Requirements
The following packages have been used in the implementation: <br>
- Python 3.7.7
- numpy 1.18.1
- scipy 1.4.1
- gensim 3.8.0
- scikit-learn 0.22.1

# Results
No results have been produced yet.

# Remaining
Implementation of Random Forest Classifier with 100 trees for predicting friendship recommendations. <br>
Generation of results and evaluation of the fairness metrics - Statistical Parity, Equality of Representation (User Level and Network Level). <br>
Implementation of graph embeddings with regular random walks for comparing results.

# NOTE
The original Instagram dataset could not be used as the authors refused to share it. As per their suggestion, we used Social Circles: Facebook dataset from SNAP. <br>
It was unclear from the research paper about the data on which Random Forest Classifier has been trained by the authors. As far as we could understand, the inputs were hadamard vectors for all the node pairs in the graph, and the output was supposed to be whether they should be recommended or not. However, in doing this, we faced a problem of data imbalance - number of false cases was much larger than true cases.

## Contributors
- [Mridul Agarwal](https://github.com/mridul2899), 17QE30008 - Third-year Undergraduate Student