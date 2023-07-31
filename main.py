import sys
import networkx as nx
import math as m
import csv
from matplotlib import pyplot as plt

RUN_KEY = '-t'
FILE_EXTENSION = '.gml'
CRITERION_KEY = '-k'
CRITERION_VAL1 = '1'
CRITERION_VAL2 = '2'

DEGREE_TO_RADIAN = 180 / m.pi
EARTH_RADIUS = 6371
MAX_DISTANT = EARTH_RADIUS * m.pi
DEGREE_TO_KM = MAX_DISTANT / 360
DELAY = 4.8


def make_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


# с наименьшей максимальной длиной пути от узла контроллера до вершины
def get_min_span_tree_1(span_tree, n, edges, max_path, i):
    nodes = list(span_tree.nodes())
    if len(nodes) == n:
        return span_tree

    answer = nx.Graph()
    answer.add_weighted_edges_from([(0, 1, MAX_DISTANT * n)])
    for edge in edges:
        if nodes.__contains__(edge[0]) ^ nodes.__contains__(edge[1]):
            new_span_tree = span_tree.copy()
            new_span_tree.add_weighted_edges_from([edge])
            new_edges = edges.copy()
            new_edges.remove(edge)

            graph = get_min_span_tree_1(new_span_tree, n, new_edges, max_path, i+1)
            graph_nodes = graph.nodes()
            minimum = n * MAX_DISTANT
            for node1 in graph_nodes:
                maximum = 0
                for node2 in graph_nodes:
                    maximum = max(maximum, nx.dijkstra_path_length(graph, node1, node2))
                minimum = min(minimum, maximum)
            if max_path > minimum:
                max_path = minimum
                answer = graph

    return answer


# с наименьшей суммарной длиной рёбер ~ алгоритм Краскала
def get_min_span_tree_2(edges):
    span_tree = nx.Graph()

    connected_nodes = set()
    isolated_nodes = {}
    for edge in edges:
        if not (edge[0] in connected_nodes and edge[1] in connected_nodes):
            if edge[0] not in connected_nodes and edge[1] not in connected_nodes:
                isolated_nodes[edge[0]] = [edge[0], edge[1]]
                isolated_nodes[edge[1]] = isolated_nodes[edge[0]]
            elif not isolated_nodes.get(edge[0]):
                isolated_nodes[edge[1]].append(edge[0])
                isolated_nodes[edge[0]] = isolated_nodes[edge[1]]
            else:
                isolated_nodes[edge[0]].append(edge[1])
                isolated_nodes[edge[1]] = isolated_nodes[edge[0]]

            span_tree.add_weighted_edges_from([edge])
            connected_nodes.add(edge[0])
            connected_nodes.add(edge[1])
    for edge in edges:
        if edge[1] not in isolated_nodes[edge[0]]:
            span_tree.add_weighted_edges_from([edge])

            save = isolated_nodes[edge[0]]
            isolated_nodes[edge[0]] += isolated_nodes[edge[1]]
            isolated_nodes[edge[1]] += save

    return span_tree


def main():
    if __name__ == "__main__":
        argv_len = len(sys.argv)
        if argv_len > 1:
            if sys.argv[1] == RUN_KEY:
                if argv_len > 2:
                    if sys.argv[2].find(FILE_EXTENSION) != -1:
                        # парсинг файла
                        graph = nx.read_gml(sys.argv[2], 'id')
                        labels = list(nx.read_gml(sys.argv[2], 'label').nodes())
                        longs = list(nx.read_gml(sys.argv[2], 'Longitude').nodes())
                        lats = list(nx.read_gml(sys.argv[2], 'Latitude').nodes())
                        longs_rad = []
                        lats_rad = []
                        for i in range(len(labels)):
                            longs_rad.append(longs[i] * DEGREE_TO_RADIAN)
                            lats_rad.append(lats[i] * DEGREE_TO_RADIAN)

                        # формирование файла топологии графа
                        data = [['Node 1 (id)', 'Node 1 (label)', 'Node 1 (longitude)', 'Node 1 (latitude)',
                                 'Node 2 (id)', 'Node 2 (label)', 'Node 2 (longitude)', 'Node 2 (latitude)',
                                 'Distance (km)', 'Delay (mks)']]
                        # проверка на необходимость иметь массив взвешенных рёбер
                        need_span_tree = argv_len > 3 and sys.argv[3] == CRITERION_KEY and argv_len > 4 and (
                                sys.argv[4] == CRITERION_VAL1 or sys.argv[4] == CRITERION_VAL2)
                        weighted_edges = []
                        for node in graph.nodes():
                            for edge in graph.edges():
                                if edge[1] == node:
                                    id1 = edge[0]
                                    id2 = edge[1]
                                    for string in data:
                                        if string[0] == id1 and string[4] == id2:
                                            new_string = string.copy()
                                            for i in range(4):
                                                swapper = new_string[i]
                                                new_string[i] = new_string[i + 4]
                                                new_string[i + 4] = swapper
                                            data.append(new_string)
                                            break
                            for edge in graph.edges():
                                if edge[0] == node:
                                    id1 = edge[0]
                                    id2 = edge[1]
                                    long1 = longs_rad[id1]
                                    long2 = longs_rad[id2]
                                    lat1 = lats_rad[id1]
                                    lat2 = lats_rad[id2]
                                    # если рассматривать Землю как сферу (будут несоответствия с длинами на графе)
                                    distance = m.asin(m.sqrt(
                                        m.pow(m.sin((lat1 - lat2) / 2), 2) * m.cos(long1) * m.cos(long2) + m.pow(
                                            m.sin((long1 - long2) / 2), 2))) * 2 * EARTH_RADIUS
                                    # если рассматривать развертку Земли как плоскость
                                    distance = m.sqrt(
                                        m.pow((longs[id1] - longs[id2]), 2) + m.pow((lats[id1] - lats[id2]),
                                                                                    2)) * DEGREE_TO_KM
                                    data.append([id1, labels[id1], longs[id1], lats[id1],
                                                 id2, labels[id2], longs[id2], lats[id2],
                                                 distance, distance * DELAY])
                                    if need_span_tree:
                                        weighted_edges.append(edge + (distance,))
                        make_csv(sys.argv[2].replace('.gml', '_topo.csv'), data)

                        if argv_len > 3:
                            if sys.argv[3] == CRITERION_KEY:
                                if argv_len > 4:
                                    # формирование остовного дерева
                                    if sys.argv[4] == CRITERION_VAL1:
                                        weighted_edges.sort(key=lambda x: x[2])
                                        nodes_num = len(graph.nodes())

                                        span_tree = nx.Graph()
                                        span_tree.add_node(0)
                                        span_tree = get_min_span_tree_1(span_tree, nodes_num, weighted_edges,
                                                                        nodes_num * MAX_DISTANT, 0)
                                    elif sys.argv[4] == CRITERION_VAL2:
                                        weighted_edges.sort(key=lambda x: x[2])

                                        span_tree = get_min_span_tree_2(weighted_edges)
                                    else:
                                        print('Invalid criterion value (it needs 1 or 2)')
                                        return

                                    # поиск оптимального узла для размещения контроллера
                                    nodes = span_tree.nodes()
                                    ctrl_index = 0
                                    minimum = len(nodes) * MAX_DISTANT
                                    for node1 in nodes:
                                        maximum = 0
                                        for node2 in nodes:
                                            maximum = max(maximum, nx.dijkstra_path_length(span_tree, node1, node2))
                                        if maximum < minimum:
                                            minimum = maximum
                                            ctrl_index = node1

                                    # формирование файла топологии остовного дерева
                                    data = [['Node 1 (id)', 'Node 2 (id)', 'Path', 'Delay (mks)']]
                                    for i in range(ctrl_index):
                                        data.append([ctrl_index, i, nx.dijkstra_path(span_tree, ctrl_index, i),
                                                     nx.dijkstra_path_length(span_tree, ctrl_index, i) * DELAY])
                                    for i in range(ctrl_index + 1, len(list(span_tree.nodes()))):
                                        data.append([ctrl_index, i, nx.dijkstra_path(span_tree, ctrl_index, i),
                                                     nx.dijkstra_path_length(span_tree, ctrl_index, i) * DELAY])
                                    make_csv(sys.argv[2].replace('.gml', '_routes.csv'), data)

                                    # отрисовка графа
                                    for i in range(len(longs)):
                                        plt.annotate(i, xy=(longs[i], lats[i]))
                                        plt.scatter(longs[i], lats[i], c='black')
                                    for edge in graph.edges():
                                        plt.plot([longs[edge[0]], longs[edge[1]]], [lats[edge[0]], lats[edge[1]]],
                                                 c='blue')
                                    for edge in span_tree.edges():
                                        plt.plot([longs[edge[0]], longs[edge[1]]], [lats[edge[0]], lats[edge[1]]],
                                                 c='red')
                                    plt.scatter(longs[ctrl_index], lats[ctrl_index], c='red')
                                    plt.show()
                                else:
                                    print('No criterion value')
                            else:
                                print('Invalid additional key (it needs -k)')
                    else:
                        print('Invalid file (it needs *.gml)')
                else:
                    print('No file')
            else:
                print('Invalid run-key (it needs -t)')


main()
