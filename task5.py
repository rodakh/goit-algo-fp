import uuid
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        if node.id not in pos:
            graph.add_node(node.id, label=node.val)
            pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def draw_tree_with_color(tree, pos, colors):
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=nx.get_node_attributes(tree, 'label'),
            with_labels=True, node_size=2500, node_color=colors, font_weight='bold', font_size=8)
    plt.show()


def generate_colors(n):
    cmap = plt.cm.Blues
    return [mcolors.rgb2hex(cmap(i)) for i in np.linspace(0.2, 0.8, n)]


def dfs(tree_root, graph, pos, order=[], colors=[]):
    if tree_root is not None:
        order.append(tree_root.id)
        colors.append(generate_colors(len(order))[len(order) - 1])
        dfs(tree_root.left, graph, pos, order, colors)
        dfs(tree_root.right, graph, pos, order, colors)
    return order, colors


def bfs(tree_root, graph, pos):
    queue = [tree_root]
    order, colors = [], []
    while queue:
        current = queue.pop(0)
        order.append(current.id)
        colors.append(generate_colors(len(order))[len(order) - 1])
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return order, colors


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = nx.DiGraph()
pos = {}
add_edges(tree, root, pos)

order_dfs, colors_dfs = dfs(root, tree, pos)
draw_tree_with_color(tree, pos,
                     [colors_dfs[order_dfs.index(node)] if node in order_dfs else "#ffffff" for node in tree.nodes])

order_bfs, colors_bfs = bfs(root, tree, pos)
draw_tree_with_color(tree, pos,
                     [colors_bfs[order_bfs.index(node)] if node in order_bfs else "#ffffff" for node in tree.nodes])
