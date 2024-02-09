import uuid
import networkx as nx
import matplotlib.pyplot as plt


# Клас Node представляє окремий вузол у бінарному дереві.
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # посилання на лівого нащадка
        self.right = None  # посилання на правого нащадка
        self.val = key  # значення, яке зберігає вузол
        self.color = color  # колір вузла для візуалізації
        self.id = str(uuid.uuid4())  # унікальний ідентифікатор вузла для ідентифікації у графі


# Функція add_edges додає вузли та ребра до графа згідно зі структурою бінарного дерева.
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додавання вузла до графа з використанням його id, кольору та мітки
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            # Додавання ребра між поточним вузлом та його лівим нащадком
            graph.add_edge(node.id, node.left.id)
            # Розрахунок позиції лівого нащадка
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            # Рекурсивний виклик для лівого нащадка
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            # Додавання ребра між поточним вузлом та його правим нащадком
            graph.add_edge(node.id, node.right.id)
            # Розрахунок позиції правого нащадка
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            # Рекурсивний виклик для правого нащадка
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


# Функція draw_heap візуалізує бінарну купу, представлену у вигляді масиву, як бінарне дерево.
def draw_heap(heap):
    # Створення вузлів дерева на основі значень у масиві купи
    nodes = [Node(val) for val in heap]
    # Присвоєння лівих і правих нащадків кожному вузлу
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    # Візуалізація дерева
    draw_tree(nodes[0])


# Функція draw_tree візуалізує бінарне дерево.
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створення спрямованого графа
    pos = {tree_root.id: (0, 0)}  # Визначення початкової позиції кореня
    # Додавання вузлів та ребер до графа
    tree = add_edges(tree, tree_root, pos)
    # Визначення кольорів та міток для вузлів
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # Візуалізація графа
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Приклад бінарної купи як масиву
heap = [1, 3, 2, 7, 6, 5, 4]

# Відображення бінарної купи
draw_heap(heap)
