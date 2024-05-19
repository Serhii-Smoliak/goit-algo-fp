import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_labels = {node: tree.nodes[node]['label'] for node in tree.nodes}
    node_colors = [tree.nodes[node]['color'] for node in tree.nodes]

    plt.figure(figsize=(8, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors, font_color='white')
    plt.tight_layout()
    plt.show()


def dfs(node):
    if node is not None:
        stack = [(node, 0)]
        step = 0
        while stack:
            current, level = stack.pop()
            color = mcolors.to_hex(mcolors.hsv_to_rgb((0.46, 1.0, step / 6.0)))
            current.color = color

            step += 1
            if current.right:
                stack.append((current.right, level + 1))
            if current.left:
                stack.append((current.left, level + 1))


def bfs(node):
    if node is not None:
        queue = deque([(node, 0)])
        step = 0
        while queue:
            current, level = queue.popleft()
            shade = min((step + 2) / 5.0, 1.0)
            color = mcolors.to_hex(mcolors.hsv_to_rgb((0.46, 1.0, step / 6.0)))
            current.color = color

            step += 1
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))


def insert_to_heap(root, key):
    new_node = Node(key)
    queue = [root]
    while queue:
        temp = queue.pop(0)
        if not temp.left:
            temp.left = new_node
            return
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = new_node
            return
        else:
            queue.append(temp.right)


def build_heap(elements):
    if not elements:
        return None
    root = Node(elements[0])
    for element in elements[1:]:
        insert_to_heap(root, element)
    return root


def main():
    elements = [10, 15, 30, 40, 50, 100, 40]
    root = build_heap(elements)
    dfs(root)
    draw_tree(root, title="DFS")

    def reset_colors(node):
        if node is not None:
            node.color = "skyblue"
            reset_colors(node.left)
            reset_colors(node.right)

    reset_colors(root)
    bfs(root)
    draw_tree(root, title="BFS")


if __name__ == "__main__":
    main()
