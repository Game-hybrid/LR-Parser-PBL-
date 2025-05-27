from graphviz import Digraph

def visualize_asts(ast_list):
    dot = Digraph()
    counter = {"id": 0}

    def visit(n):
        if n is None:
            return ""
        node_id = f"n{counter['id']}"
        counter["id"] += 1
        label = f"{n.type}\n{n.value}" if n.value else n.type
        dot.node(node_id, label, shape="ellipse", style="filled", fillcolor="#e3f2fd")
        if n.left:
            left_id = visit(n.left)
            dot.edge(node_id, left_id)
        if n.right:
            right_id = visit(n.right)
            dot.edge(node_id, right_id)
        return node_id

    for ast in ast_list:
        visit(ast)

    return dot.pipe(format='svg').decode('utf-8')
