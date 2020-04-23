import random

def generate_fairwalks(ego_nodes, nodes, gender_wise_adjacency_lists, num_walks = 20, walk_len = 80):
    """
    generate_fairwalks(nodes, gender_wise_adjacency_list) generates fairwalks for all the non-isolated nodes in the network
    It takes list of nodes, a gender wise adjacency list for all the nodes in the network, number of walks and lenght of each walk as its arguments
    It returns a dictionary fair_walks, which contains num_walks iterations of fairwalks for all the nodes, each of length walk_len
    """

    fair_walks = {}
    gender_choices = [0, 1, 2]
    gender_choices_not_0 = [1, 2]
    gender_choices_not_1 = [0, 2]
    gender_choices_not_2 = [0, 1]

    for ego_node in ego_nodes:
        fair_walk = {}

        walks = []
        for walk in range(num_walks):
            prev_node = -1
            current_node = ego_node
            trace = []

            for covered_len in range(walk_len):
                trace.append(current_node)
                if len(gender_wise_adjacency_lists[ego_node][current_node][0]) == 0 and len(gender_wise_adjacency_lists[ego_node][current_node][1]) == 0:
                    gender_choice = 2
                elif len(gender_wise_adjacency_lists[ego_node][current_node][0]) == 0 and len(gender_wise_adjacency_lists[ego_node][current_node][2]) == 0:
                    gender_choice = 1
                elif len(gender_wise_adjacency_lists[ego_node][current_node][1]) == 0 and len(gender_wise_adjacency_lists[ego_node][current_node][2]) == 0:
                    gender_choice = 0
                elif len(gender_wise_adjacency_lists[ego_node][current_node][2]) == 0:
                    gender_choice = random.choice(gender_choices_not_2)
                elif len(gender_wise_adjacency_lists[ego_node][current_node][1]) == 0:
                    gender_choice = random.choice(gender_choices_not_1)
                elif len(gender_wise_adjacency_lists[ego_node][current_node][0]) == 0:
                    gender_choice = random.choice(gender_choices_not_0)
                else:
                    gender_choice = random.choice(gender_choices)

                next_node = random.choice(gender_wise_adjacency_lists[ego_node][current_node][gender_choice])
                prev_node = current_node
                current_node = next_node

            walks.append(trace)
        fair_walk[ego_node] = walks

        for node in nodes[ego_node]:
            walks = []
            for walk in range(num_walks):
                prev_node = -1
                current_node = node
                trace = []

                for covered_len in range(walk_len):
                    trace.append(current_node)
                    if len(gender_wise_adjacency_lists[ego_node][current_node][0]) == 0 and len(gender_wise_adjacency_lists[ego_node][current_node][1]) == 0:
                        gender_choice = 2
                    elif len(gender_wise_adjacency_lists[ego_node][current_node][0]) == 0 and len(gender_wise_adjacency_lists[ego_node][current_node][2]) == 0:
                        gender_choice = 1
                    elif len(gender_wise_adjacency_lists[ego_node][current_node][1]) == 0 and len(gender_wise_adjacency_lists[ego_node][current_node][2]) == 0:
                        gender_choice = 0
                    elif len(gender_wise_adjacency_lists[ego_node][current_node][2]) == 0:
                        gender_choice = random.choice(gender_choices_not_2)
                    elif len(gender_wise_adjacency_lists[ego_node][current_node][1]) == 0:
                        gender_choice = random.choice(gender_choices_not_1)
                    elif len(gender_wise_adjacency_lists[ego_node][current_node][0]) == 0:
                        gender_choice = random.choice(gender_choices_not_0)
                    else:
                        gender_choice = random.choice(gender_choices)

                    next_node = random.choice(gender_wise_adjacency_lists[ego_node][current_node][gender_choice])
                    prev_node = current_node
                    current_node = next_node

                walks.append(trace)
            fair_walk[node] = walks
        fair_walks[ego_node] = fair_walk

    return fair_walks

if __name__ == '__main__':
    from adjacency_list import generate_adjacency_list
    from feature_extraction import generate_features
    from gender_mapping import map_nodes_gender
    nodes, adjacency_lists, ego_nodes = generate_adjacency_list()
    features, gender_featnum = generate_features(ego_nodes)
    gender_1, gender_2, gender_wise_adjacency_lists = map_nodes_gender(nodes, adjacency_lists, ego_nodes, gender_featnum, features)
    fair_walks = generate_fairwalks(ego_nodes, nodes, gender_wise_adjacency_lists)
    print(fair_walks[0][0])