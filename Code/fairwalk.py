import random
import os

def generate_fairwalks(ego_nodes, num_walks = 20, walk_len = 80):
    """
    generate_fairwalks(ego_nodes) generates fairwalks for all the nodes in all of the ego-networks
    It takes list of ego nodes, number of walks and length of each walk as its arguments.
    It saves the Fairwalk traces, which contain num_walks iterations of fairwalks for all the nodes of each instance of all the ego-networks, each of length walk_len
    The directory for the output Fairwalk traces is ../Fairwalks/
    """

    try:
        os.mkdir('../Fairwalks/')
    except:
        pass

    gender_choices = [0, 1, 2]
    gender_choices_not_0 = [1, 2]
    gender_choices_not_1 = [0, 2]
    gender_choices_not_2 = [0, 1]

    for ego_node in ego_nodes:
        for i in range(5):
            file = open('../Gender_Adjacency_Lists/gender_wise_adjacency_list_{}_{}.txt'.format(ego_node, i), 'r')
            gender_wise_adjacency_list = {}
            lines = file.readlines()
            j = 0
            while j < len(lines) and len(lines[j].strip()) != 0:
                node = int(lines[j].strip())
                gender_wise_adjacency_list[node] = []
                for k in range(3):
                    j += 1
                    gender_wise_adjacency_list[node].append([int(n) for n in lines[j].strip().split()])
                j += 1
            nodes = [int(n.strip()) for n in lines[::4]]
            file.close()
            file = open('../Fairwalks/fairwalks_{}_{}.txt'.format(ego_node, i), 'w')
            for walk in range(num_walks):
                for node in nodes:
                    prev_node = -1
                    trace = []
                    current_node = node
                    for covered_len in range(walk_len):
                        trace.append(current_node)
                        if len(gender_wise_adjacency_list[current_node][0]) == 0 and len(gender_wise_adjacency_list[current_node][1]) == 0:
                            gender_choice = 2
                        elif len(gender_wise_adjacency_list[current_node][0]) == 0 and len(gender_wise_adjacency_list[current_node][2]) == 0:
                            gender_choice = 1
                        elif len(gender_wise_adjacency_list[current_node][1]) == 0 and len(gender_wise_adjacency_list[current_node][2]) == 0:
                            gender_choice = 0
                        elif len(gender_wise_adjacency_list[current_node][2]) == 0:
                            gender_choice = random.choice(gender_choices_not_2)
                        elif len(gender_wise_adjacency_list[current_node][1]) == 0:
                            gender_choice = random.choice(gender_choices_not_1)
                        elif len(gender_wise_adjacency_list[current_node][0]) == 0:
                            gender_choice = random.choice(gender_choices_not_0)
                        else:
                            gender_choice = random.choice(gender_choices)
                        next_node = random.choice(gender_wise_adjacency_list[current_node][gender_choice])
                        prev_node = current_node
                        current_node = next_node
                    line = ''
                    for step in trace:
                        line = line + str(step) + ' '
                    file.write(line.strip() + '\n')
                    line = ''
                    for step in trace[::-1]:
                        line = line + str(step) + ' '
                    file.write(line.strip() + '\n')
            file.close()