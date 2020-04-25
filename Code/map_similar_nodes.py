def map_similar_nodes(ego_nodes):
    """
    map_similar_nodes(ego_nodes) scrapes the test edges (20%) data, and maps similar non-friend nodes as friends and non-friends.
    It takes the list of ego nodes as its argument.
    The similar non-friend nodes were generated on the basis of training edges (80%) data.
    It is possible that the similar nodes found were actually connected, but were in test edges (20%) data.
    Therefore, this function maps the similar non-friend nodes as friends and non-friends and saves the information in the directory ../Similar_nodes/
    """

    for ego_node in ego_nodes:
        for i in range(5):
            file = open('../Similar_Nodes/similar_nodes_{}_{}.txt'.format(ego_node, i), 'r')
            lines = file.readlines()
            file.close()

            similar = {}
            for line in lines:
                if len(line) == 0:
                    continue
                line = line.strip().split()
                similar[int(line[0])] = [int(word) for word in line[1:]]

            file = open('../Edges/edges_20_{}_{}.txt'.format(ego_node, i), 'r')
            lines = file.readlines()
            file.close()

            adjacent_test = {}
            for line in lines:
                if len(lines) == 0:
                    continue
                line = line.strip().split()
                one, two = int(line[0]), int(line[1])
                if one not in adjacent_test.keys():
                    adjacent_test[one] = set()
                if two not in adjacent_test.keys():
                    adjacent_test[two] = set()
                adjacent_test[one].add(two)
                adjacent_test[two].add(one)

            keys = list(similar.keys())
            keys.sort()

            file = open('../Similar_Nodes/similar_{}_{}.txt'.format(ego_node, i), 'w')
            friends = {}
            non_friends = {}
            for key in keys:
                friends[key] = set()
                non_friends[key] = set()

                for node in similar[key]:
                    if key in adjacent_test.keys() and node in adjacent_test[key]:
                        friends[key].add(node)
                    else:
                        non_friends[key].add(node)
                file.write('{}\n'.format(key))

                for node in friends[key]:
                    file.write('{} '.format(node))
                file.write('\n')

                for node in non_friends[key]:
                    file.write('{} '.format(node))
                file.write('\n\n')
            file.close()